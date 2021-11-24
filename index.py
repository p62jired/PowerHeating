import time
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import json
from csv import writer
import logging

#/////////////Debugging Modbus Tool//////////////////
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
#/////////////////////////////////////////////////////

#/////////////Parameter///////////////////////////////
modbusReqTime = 0.3
jsonFilePath = "/var/lib/docker/volumes/iot-stack-tutorial_noderedData/_data/bind.json"
isInterrupModbusEnable = False
isReadingTRSEnable = True
isReadingGatewayEnable = True
isReadingISR1 = False
isReadingISR2 = True
isDataLoggerEnabled = True
client = ModbusSerialClient(
    method='rtu',
    #port='/dev/ttyS0',
    port='/dev/ttyUSB0',
    baudrate=9600,
    timeout=1,
    parity='N',
    stopbits=1,
    bytesize=8
)
#/////////////////////////////////////////////////////

#/////////////Global Scope////////////////////////////
tModbus_start = time.perf_counter()
tModbus_current = time.perf_counter()
tLoggerStart = time.perf_counter()
heartBeat = 0
#/////////////////////////////////////////////////////

#Load JSON struct from JSON file into global variable
with open(jsonFilePath) as jsonFile:
    jsonSystem = json.load(jsonFile)
    jsonFile.close()

# Return value of trying to connect to Modbus Server/Slave
def isModbusConnection():
    return client.connect()

# Return JSON object from a holding register with the below content
def readModbusResgister(slaveNr, registerAdrrs, decoderVal):
    time.sleep(modbusReqTime)
    if isModbusConnection(): 
        try:
            res = client.read_holding_registers(address=registerAdrrs, count=0x01, unit=slaveNr)
            decoder = BinaryPayloadDecoder.fromRegisters(res.registers, byteorder=Endian.Big)
            if decoderVal > 1:
                client.close()
                return decoder.decode_16bit_int()/decoderVal
            client.close()
            return decoder.decode_16bit_int()
        except:
            print("An exception occurred")
            client.close()
            return -990
    client.close()
    print("not ModbusConnection")
    return -990

def readInputModbusResgister(slaveNr, registerAdrrs, decoderVal):
    time.sleep(modbusReqTime)
    if isModbusConnection(): 
        try:
            res = client.read_input_registers(address=registerAdrrs, count=0x01, unit=slaveNr)
            decoder = BinaryPayloadDecoder.fromRegisters(res.registers, byteorder=Endian.Big)
            if decoderVal > 1:
                client.close()
                return decoder.decode_16bit_int()/decoderVal
            client.close()
            return decoder.decode_16bit_int()
        except:
            print("An exception occurred")
            client.close()
            return -990
    client.close()
    print("not ModbusConnection")
    return -990    

def writetoJSON(strFileName):

    with open(strFileName) as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    jsonObject = jsonSystem
    # Open (or create) an orders_new.json file
    # and store the new version of the data.

    with open(strFileName, 'w') as file:
        json.dump(jsonObject, file, indent=4, sort_keys=True)

def readModbusFromWD():
    #Air Temperature
    print(readInputModbusResgister(70, 19, 10))
    jsonSystem["Lufttemperatur"]= readInputModbusResgister(70, 19, 10)
    #Wind velocity
    print(readInputModbusResgister(70, 45, 1))
    jsonSystem["Windgeschwindigkeit"]= readInputModbusResgister(70, 45, 1)
    #Amount of precipitation
    print(readInputModbusResgister(70, 59, 1))
    jsonSystem["Niederschlagsmenge"]= readInputModbusResgister(70, 59, 1)
    #Niederschlagsart
    #0 = kein Niederschlag
    #60 = flüssiger Niederschlag, z.B. Regen
    #70 = fester Niederschlag, z.B. Schnee
    #90: Hagel
    print(readInputModbusResgister(70, 121, 1))
    jsonSystem["Niederschlagsart"]= readInputModbusResgister(70, 121, 1)

    #UV-Index
    print(readInputModbusResgister(70, 134, 1))
    jsonSystem["UV-Index"]= readInputModbusResgister(70, 134, 1)


def readModbusFromTRD():
    #Read from TRS-03 4 AI
    for x in range(4):
        #print("Sensor " + str(x + 1 ))
        jsonSystem["TempsTRS"][x]= readModbusResgister(1, 4609 + x, 10)
        #print(jsonSystem["TempsTRS"][x])

def readModbusFromGateway():
    #Read SFSRailTemp object
    #The number of Gateway records per ISR are from 0 to 485. Therefore, 
    #ISR device number 2 begins with record number 286. 
    # We take this number as an index for successive ISRs.
    #For example, if we want to read register 177 (set point temperature) in ISR number 2, 
    #the resulting register would be 463 (286 + 177) = 0x1cf
    jsonSystem["SFSRailTemp"] = readModbusResgister(62, 64, 10)
    #print(jsonSystem["SFSRailTemp"])
    jsonSystem["SignalForRegulate"] = readModbusResgister(62, 282, 1)
    #print(jsonSystem["SignalForRegulate"])
    jsonSystem["ISR"][1]["ISRRailTemp"] = readModbusResgister(62, 346, 10)
    if isReadingISR1:
        #ContactorOn ISR 1
        jsonSystem["ISR"][0]["ContactorOn"][0] = readModbusResgister(62, 80, 1)
        jsonSystem["ISR"][0]["ContactorOn"][1] = readModbusResgister(62, 81, 1)
        jsonSystem["ISR"][0]["ContactorOn"][2] = readModbusResgister(62, 82, 1)
        #Collecting Error ISR 1
        jsonSystem["ISR"][0]["CollectingError"][0] = readModbusResgister(62, 91, 1)
        jsonSystem["ISR"][0]["CollectingError"][1] = readModbusResgister(62, 92, 1)
        jsonSystem["ISR"][0]["CollectingError"][2] = readModbusResgister(62, 93, 1)
    
    if isReadingISR2:
        #ContactorOn ISR 2
        jsonSystem["ISR"][1]["ContactorOn"][0] = readModbusResgister(62, 366, 1)
        jsonSystem["ISR"][1]["ContactorOn"][1] = readModbusResgister(62, 367, 1)
        jsonSystem["ISR"][1]["ContactorOn"][2] = readModbusResgister(62, 368, 1)
        #Collecting Error ISR 2
        jsonSystem["ISR"][1]["CollectingError"][0] = readModbusResgister(62, 377, 1)
        jsonSystem["ISR"][1]["CollectingError"][1] = readModbusResgister(62, 378, 1)
        jsonSystem["ISR"][1]["CollectingError"][2] = readModbusResgister(62, 379, 1)
        # #HeatingCurrent ISR 2
        jsonSystem["ISR"][1]["HeatingCurrent"][0] = readModbusResgister(62, 331, 100)
        #print(jsonSystem["ISR"][1]["HeatingCurrent"][0]) 
        jsonSystem["ISR"][1]["HeatingCurrent"][1] = readModbusResgister(62, 332, 100)
        #print(jsonSystem["ISR"][1]["HeatingCurrent"][1]) 
        jsonSystem["ISR"][1]["HeatingCurrent"][2] = readModbusResgister(62, 333, 100)
        #print(jsonSystem["ISR"][1]["HeatingCurrent"][2])

while True:
    if isReadingGatewayEnable:
        readModbusFromGateway()
        writetoJSON(jsonFilePath)
    if isReadingTRSEnable:
        readModbusFromTRD()
        writetoJSON(jsonFilePath)   
    jsonSystem["ModbusPause"] = 0
    jsonSystem["HeartBeat"] = heartBeat
    heartBeat += 1
    #print("HeartBeat: " + str(heartBeat))
    if heartBeat == 10:
         heartBeat = 0

    if isDataLoggerEnabled:
        time.sleep(0.5)
        readModbusFromWD()
    if isInterrupModbusEnable:
        #print(f"Modbus readed in {tModbus_current - tModbus_start:0.4f} seconds")
        tModbus_current = time.perf_counter()
        if tModbus_current-tModbus_start > 3600:
            jsonSystem["ModbusPause"] = 1
            time.sleep(120)
            tModbus_start = time.perf_counter()
            tModbus_current = time.perf_counter()