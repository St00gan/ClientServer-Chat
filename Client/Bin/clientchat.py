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
ipset = input("Do you want to manually set IP of server? (Y/N): ")
if (ipset == "Y") or (ipset == "y"):
    print(ipset)
    ip = input("What do you want to set the ip to?: ")
elif ipset == 'home':
    ip='127.0.1.1'
elif ipset == 'class':
    ip='172.16.107.106'
else:
    True
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
                print('\r'+msg)
                print(prefix, end='')
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
