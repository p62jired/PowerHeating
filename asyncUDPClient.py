
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

async def logger(index, addrPort):
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
       
while True:
    asyncio.run(logger1())
    asyncio.run(logger2())
    asyncio.run(logger3())
    asyncio.run(logger4())
    time.sleep(2)

