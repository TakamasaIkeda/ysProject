import socket 

host = "localhost"
port = 5678
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 


while 1:
    print "Type message you want to send to %s..." % (host) 
    msg = raw_input() 
    if msg == "":
        s.close() 
        break
    s.sendall(msg) 
