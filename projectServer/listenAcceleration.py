#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket
import threading
import pickle
from pourToSql import *

class ListenAcceleration:

    def __init__(self): 
        self.address = ""
        self.port = 0
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    #set host information(for capsulation)
    def setAddress(self, address, port): 
        self.address = address
        self.port = port

    #return host information
    def getAddress(self): 
        return self.address, self.port

    #untill bind, listen
    def sockServer(self):
        host = (self.address, self.port) 

        self.serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.serversock.bind(host) 
        self.serversock.listen(5) 
        print ("[*]Listening on address:\"%s \" port: %d" % (self.address, self.port))

    #handle the socket connection
    def handle_client(self, client_socket):
        bufsize = 1048576
        request = client_socket.recv(bufsize) 
        data = pickle.loads(request)
        print "[*]Received: %s" % data
        client_socket.close()
        print "Connection of %s is DONE" % (threading.currentThread().getName())

        pour2SQL(data)  
