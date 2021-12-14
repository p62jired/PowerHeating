import socket
import time
import json
import asyncio
import threading
from csv import writer

filePath = "/home/pi/project/html/logger.json"
msgFromClient       = "1"
bytesToSend         = str.encode(msgFromClient)
bufferSize          = 1024
errorTempList = ["n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a",\
"n/a","n/a","n/a","n/a","n/a","n/a","n/a","n/a",]
sensorError = 1372.0

server_1_AddressPort = ("192.168.0.100", 2001)
server_2_AddressPort = ("192.168.0.101", 2001)
server_3_AddressPort = ("192.168.0.102", 2001)
server_4_AddressPort = ("192.168.0.103", 2001)


loggerIntervalInSec = 10
jsonFilePath = "/var/lib/docker/volumes/iot-stack-tutorial_noderedData/_data/bind.json"


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
UDPClientSocket.settimeout(0.5)
# dataFromFile = json.load(open(filePath, 'r'))
# print(type(dataFromFile))  
with open(filePath, 'r') as f:
    dataFromFile = json.load(f)
    print(dataFromFile)

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

async def logger1(serverAddressPort):
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

async def logger2(serverAddressPort):
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

async def logger3(serverAddressPort):
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

async def logger4(serverAddressPort):
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



def looper1():    
    # i as interval in seconds    
    threading.Timer(2, looper1).start()    
    # put your action here
    print("in looper 1")
    asyncio.run(logger1(server_1_AddressPort))
    asyncio.run(logger2(server_2_AddressPort))
    asyncio.run(logger3(server_3_AddressPort))
    asyncio.run(logger4(server_4_AddressPort))

def looper2():    
    # i as interval in seconds    
    threading.Timer(loggerIntervalInSec, looper2).start()    
    # put your action here
    print("in looper 2")
    asyncio.run(logInToCSV(jsonFilePath))

#Load JSON struct from JSON file into global variable
async def logInToCSV(jsonFilePath):

    with open(jsonFilePath) as jsonFile:
        jsonSystem = json.load(jsonFile)

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
looper1()
looper2()
 