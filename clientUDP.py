import socket
import time
import json

filePath = "html/logger.json"
#msgFromClient       = "Hello UDP Server"
msgFromClient       = "1"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.0.100", 2001)
bufferSize          = 1024
errorTempList = [-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,\
-99,-99,-99,-99,-99,-99,-99,-99,]
sensorError = 1372.0


def openJSONFile(path):  
    # Opening JSON file
    with open(path, 'r') as openfile:
        # Reading from json file
        return json.load(openfile)

#dataJSON = openJSONFile(filePath)

def writeJSONFile(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4, sort_keys=False)

# for i in range(0, len(errorTempList)):
#     #print(str(i+1))
#     #print(errorTempList[i])
#     iString = str(i+1)
#     dataJSON["1"][i] = errorTempList[i]
#     # intTemp = int.from_bytes(WordList[i], "little")
#     # tempList.append(intTemp/10)

# print(dataJSON)
# writeJSONFile(filePath, dataJSON)


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
UDPClientSocket.settimeout(0.5)
print(UDPClientSocket.gettimeout())
print(len(errorTempList))

def bytesListToWordsList(listBytes):
    chunk_size = 2
    chunked_list = list()
    for i in range(0, len(listBytes), chunk_size):
        chunked_list.append(listBytes[i:i+chunk_size])
    return chunked_list

def WordListToTempList(WordList):
    tempList = list()
    for i in range(0, len(WordList)):
        intTemp = int.from_bytes(WordList[i], "little")
        tempList.append(intTemp/10)
    return tempList

while True:
    try:
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
        data = msgFromServer[0] 
        listOfTemps = WordListToTempList(bytesListToWordsList(data))
        print(listOfTemps)
        dataJSON = openJSONFile(filePath)
        #Modify the readed JSON file with received data from UDP connection 
        for i in range(0, len(listOfTemps)):
            dataJSON["1"][i] = listOfTemps[i]
        writeJSONFile(filePath, dataJSON)
    except socket.timeout:
        print("timeout from " + serverAddressPort[0]+ "!!")

    time.sleep(4)