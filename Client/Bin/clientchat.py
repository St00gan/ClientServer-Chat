import socket
import threading
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6969
fh = open("data/user.txt","r+")
uname = fh.read()
prefix = (uname+'>> ')

fh = open("data/ip.txt", "r+")
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
            if msg.startswith(uname+'>> '):
                True
            else:
                    print('\r'+(' '*20)+'\r'+msg+'\n'+prefix, end='')
        except: 
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
time.sleep(0.01)
while clientRunning:
    usermsg = input(uname+'>> ')
    tempMsg = ("**broadcast"+uname+'>> ' + usermsg)
    msg = tempMsg
    if '**quit' in msg:
        clientRunning = False
        s.send('**quit'.encode('ascii'))
        break
    else:
        s.send(msg.encode('ascii'))
        time.sleep(0.01)
