import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4242
fh = open("data/user.txt","w")
fh.close()
fh = open("data/user.txt","r")
uname = fh.read()
fh.close()
fh = open("data/ip.txt", "r")
ip = fh.read()
fh.close()
s.connect((ip, port))
s.send(uname.encode('ascii'))

clientRunning = True

def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(1024).decode('ascii')
        except:
            print('PASSWORD SERVER IS OFFLINE RIGHT NOW')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
try:
    password = ()
    msg = password
    s.send(msg.encode('ascii'))
except:
    print('PASSWORD SERVER IS OFFLINE RIGHT NOW')
    exit()
