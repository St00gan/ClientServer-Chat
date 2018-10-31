import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6969
fh = open("user.txt","r")
uname = fh.read()

fh = open("ip.txt", "r")
ip = fh.read()
ipchange = input("Do you want to manually set IP of server? (Y/N): ")
if ipchange == "Y" or "y":
    ip = input("What do you want to set the ip to?: ")
else:
    ip = ip
fh.close()

s.connect((ip, port))
s.send(uname.encode('ascii'))

clientRunning = True

def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(1024).decode('ascii')
            if msg.startswith(uname+">>"):
                msg = msg
            else:
                print(msg)
        except:
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
while clientRunning:
    usermsg = input(uname+">> ")
    tempMsg = ("**broadcast " + usermsg)
    msg = uname + '>>' + tempMsg
    if '**quit' in msg:
        clientRunning = False
        s.send('**quit'.encode('ascii'))
        break
    else:
        s.send(msg.encode('ascii'))
