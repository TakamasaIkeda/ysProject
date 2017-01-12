#!/usr/bin/python
#-*- coding: utf-8 -*-
from listenAcceleration import ListenAcceleration
import threading

def main():
    address = ""
    port = 5678

    al = ListenAcceleration()
    al.setAddress(address, port) 
    al.sockServer() 

    while 1:
        try:
            client, addr = al.serversock.accept() 
        except:
            break
        print "[*]Accepted connection from: %s:%d" % (addr[0], addr[1]) 
        handler = threading.Thread(target=al.handle_client, args=[client,]) 
        handler.start() 

if __name__ == "__main__":
    main() 
