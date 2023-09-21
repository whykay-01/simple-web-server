from socket import *
import sys

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepare a server socket
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print('----- The server is ready to receive -----')

while True:
    connectionSocket, addr = serverSocket.accept()
    print('----- Connection established -----')
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        response = b'HTTP/1.1 200 OK\r\n\r\n'  # Encode as bytes
        connectionSocket.send(response)

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) # Encode as bytes

        connectionSocket.close()
        
    except IOError:
        # Send response message for file not found
        response = b'HTTP/1.1 404 Not Found\r\n\r\n'  # Encode as bytes
        connectionSocket.send(response)
        
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
