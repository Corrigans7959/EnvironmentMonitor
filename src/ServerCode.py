'''
Created on Nov 23, 2019

@author: corrigans
'''

# main method
if __name__ == '__main__':
    pass

import socket, threading


class ClientThread(threading.Thread):
    time = 0
    date = 0
    temperature = 0
  
        
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

    def run(self):
        print ("Connection from : ", clientAddress)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:      
            data = self.csocket.recv(2048)
            msg = data.decode()
            lines = data.split("\n")
            
            my_list = [] # list
            my_list.append(msg)
            
            print(lines)
            if msg == 'bye':
                break
            print ("from client", msg)
            self.csocket.send(bytes(msg, 'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")


LOCALHOST = "10.220.40.144"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()


