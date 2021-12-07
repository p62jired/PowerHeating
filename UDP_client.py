import socket
import time

#msgFromClient       = "Hello UDP Server"
msgFromClient       = "1"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.0.100", 2001)
bufferSize          = 1024
DEBUG = 1
errorTempList = [-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,-99,\
-99,-99,-99,]
errorTemp = 1372.0
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
    print(chunked_list)
    return chunked_list

def WordListToTempList(WordList):
    tempList = list()
    for i in range(0, len(WordList)):
        intTemp = int.from_bytes(WordList[i], "little")
        tempList.append(intTemp/10)
    return tempList

while True:
    if not DEBUG:
        try:
            # Send to server using created UDP socket
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            msg = "Message from Server {}".format(msgFromServer[0])
            data = msgFromServer[0]
            print(type(msgFromServer[0]))
            info = [data[i:i + 2] for i in range(0, len(data), 2)]
            print(info)
            print(type(info[0]))
            int_val = int.from_bytes(info[1], "little")
            print(int_val)
        except socket.timeout:
            print("timeout from " + serverAddressPort[0]+ "!!")
        time.sleep(2)
        # for x in data:
        #     print(x)
    else:
        try:
            # Send to server using created UDP socket
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            msg = "Message from Server {}".format(msgFromServer[0])
            data = msgFromServer[0] 
            listOfTemps = WordListToTempList(bytesListToWordsList(data))
            print(listOfTemps)
        except socket.timeout:
            print("timeout from " + serverAddressPort[0]+ "!!")
        time.sleep(2)