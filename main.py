#import socket module
from socket import *
import sys # In order to terminate the program

from lxml import html
import requests


serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
#Fill in end

while True:
    #Establish the connection 
    print('Ready to serve...') 
    # TODO: Fill in
    connectionSocket, addr = None, None
    try:
        message = #Fill in start #Fill in end filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode()) connectionSocket.send("\r\n".encode())
        connectionSocket.close() 
        
    except IOError:
        #Send response message for file not found
            #Fill in start
        #Fill in end
        #Close client socket
                #Fill in start
        #Fill in end
        pass
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data