
import socket
import time
import json
import asyncio

filePath = "html/logger.json"
msgFromClient       = "1"
bytesToSend         = str.encode(msgFromClient)
bufferSize          = 1024
errorTempList = ["n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a",\
"n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a",]
sensorError = 1372.0

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
UDPClientSocket.settimeout(0.5)
dataFromFile = json.load(open(filePath, 'r'))

def writeJSONFile(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4, sort_keys=False)

def bytesListToWordsList(listBytes):
    chunk_size = 2
    chunked_list = list()
    for i in range(0, len(listBytes), chunk_size):
        chunked_list.append(listBytes[i:i+chunk_size])
    return chunked_list

def wordListToTempList(WordList):
    tempList = list()
    for i in range(0, len(WordList)):
        intTemp = int.from_bytes(WordList[i], "little")
        tempList.append(intTemp/10)
    return tempList

def listOfTempsToJSONFile(index, JSONFromFile, listOfTemps):
    for i in range(0, len(listOfTemps)):
        #dataJSON["1"][0] = listOfTemps[0]
        JSONFromFile[str(index)][i] = listOfTemps[i]
    return JSONFromFile


async def logger1():
    serverAddressPort   = ("192.168.0.100", 2001)
    index = 1
    try:
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        data = msgFromServer[0] 
        listOfTemps = wordListToTempList(bytesListToWordsList(data))
        print(listOfTemps)
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, listOfTemps)
        writeJSONFile(filePath, dataToWritte)
    except socket.timeout:
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, errorTempList)
        writeJSONFile(filePath, dataToWritte)
        print("timeout from " + serverAddressPort[0]+ "!!")

async def logger2():
    serverAddressPort   = ("192.168.0.101", 2001)
    index = 2
    try:
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        data = msgFromServer[0] 
        listOfTemps = wordListToTempList(bytesListToWordsList(data))
        print(listOfTemps)
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, listOfTemps)
        writeJSONFile(filePath, dataToWritte)
    except socket.timeout:
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, errorTempList)
        writeJSONFile(filePath, dataToWritte)
        print("timeout from " + serverAddressPort[0]+ "!!")

async def logger3():
    serverAddressPort   = ("192.168.0.102", 2001)
    index = 3
    try:
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        data = msgFromServer[0] 
        listOfTemps = wordListToTempList(bytesListToWordsList(data))
        print(listOfTemps)
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, listOfTemps)
        writeJSONFile(filePath, dataToWritte)
    except socket.timeout:
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, errorTempList)
        writeJSONFile(filePath, dataToWritte)
        print("timeout from " + serverAddressPort[0]+ "!!")

async def logger4():
    serverAddressPort   = ("192.168.0.103", 2001)
    index = 4
    try:
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        data = msgFromServer[0] 
        listOfTemps = wordListToTempList(bytesListToWordsList(data))
        print(listOfTemps)
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, listOfTemps)
        writeJSONFile(filePath, dataToWritte)
    except socket.timeout:
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, errorTempList)
        writeJSONFile(filePath, dataToWritte)
        print("timeout from " + serverAddressPort[0]+ "!!")        

def logger(index, addrPort):
    serverAddressPort   = ("192.168.0.101", 2001)
    try:
        UDPClientSocket.sendto(bytesToSend, addrPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        data = msgFromServer[0] 
        listOfTemps = wordListToTempList(bytesListToWordsList(data))
        print(listOfTemps)
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, listOfTemps)
        writeJSONFile(filePath, dataToWritte)
    except socket.timeout:
        dataToWritte = listOfTempsToJSONFile(index, dataFromFile, errorTempList)
        writeJSONFile(filePath, dataToWritte)
        print("timeout from " + serverAddressPort[0]+ "!!")


#//////Modus to CSv ******test**********************************************
#////////////////////////////////////////////////////////////////////////////
# Pre-requisite - Import the writer class from the csv module
from csv import writer
import time
loggerIntervalInSec = 5
jsonFilePath = "/var/lib/docker/volumes/iot-stack-tutorial_noderedData/_data/bind.json"
tStart = time.perf_counter()
print(tStart)
#Load JSON struct from JSON file into global variable
async def new_func(jsonFilePath, tLoggerStart):
    tLoggerCurrent = time.perf_counter()
    if tLoggerCurrent-tLoggerStart > loggerIntervalInSec:
        tLoggerStart = time.perf_counter()
        tLoggerCurrent = time.perf_counter()
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
        print("llegamos!!!!")
        
        # Pre-requisite - The CSV file should be manually closed before running this code.

        # First, open the old CSV file in append mode, hence mentioned as 'a'
        # Then, for the CSV file, create a file object
        try:
            print(jsonFilePath)
            with open(jsonFilePath) as jsonFile:
                jsonSystem = json.load(jsonFile)
                jsonFile.close()
        except Exception as error: 
            print('oops')
        isHeatingActivated =    jsonSystem["ISR"][1]["ContactorOn"][0] \
                or jsonSystem["ISR"][1]["ContactorOn"][0] \
                or jsonSystem["ISR"][1]["ContactorOn"][0]

        # The data assigned to the list 
        list_data=[time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),jsonSystem["Lufttemperatur"]\
                  ,jsonSystem["RelativeFeucht"]\
                  ,jsonSystem["Windgeschwindigkeit"],jsonSystem["Niederschlagsmenge"]\
                  ,jsonSystem["Niederschlagsart"],jsonSystem["UV-Index"]]

        if   isHeatingActivated:      
            with open('logs/logger.csv', 'a', newline='') as f_object:  
                # Pass the CSV  file object to the writer() function
                writer_object = writer(f_object)
                # Result - a writer object
                # Pass the data in the list as an argument into the writerow() function
                writer_object.writerow(list_data)  
                # Close the file object
                f_object.close()


#////////////////////////////////////////////////////////////////////////////
#//////Modus to CSv ******test**********************************************
while True:
    asyncio.run(logger1())
    asyncio.run(logger2())
    asyncio.run(logger3())
    asyncio.run(logger4())
    asyncio.run(new_func(jsonFilePath, tStart))

