from socket import *
import sys

from lxml import html
import requests

serverName = 'server'
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print('----- The server is ready to receive -----')

while True:
    connectionSocket, addr = serverSocket.accept()
    # decode the message from the client (normally a link to the page)
    link_to_the_page = connectionSocket.recv(1024).decode()
    
    try:
        message = None #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end 
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode()) connectionSocket.send("\r\n".encode())
        connectionSocket.close() 
        
    except IOError:
        #Send response message for file not found
        #Fill in start
        # TODO: is this sending an HTTP file?
        connectionSocket.send('404 Not Found')
        #Fill in end
        
        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data