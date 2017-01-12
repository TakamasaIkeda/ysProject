import socket

host = ''
port = 5678


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((host,port)) 
s.listen(1) 
print "waiting for connections..."

clientsock, clientaddr = s.accept() 
print "rcv addr:" + str(clientaddr)

while 1:
    rcvmsg = clientsock.recv(1024) 
    print "you received a message > %s" % (rcvmsg) 
    if rcvmsg == "":
        print "connection close" 
        break
clientsock.close() 
