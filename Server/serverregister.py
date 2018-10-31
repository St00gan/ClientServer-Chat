import socket
import threading
import os.path

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
ip = str(socket.gethostbyname(socket.gethostname()))
port = 4243

clients = {}

s.bind((ip, port))
s.listen()
print('Registration Server Ready...')
print('Ip Address of the Server::%s'%ip)

def handleClient(client, uname):
    clientConnected = True
    keys = clients.keys()
    while clientConnected:
        try:
            msg = client.recv(1024).decode('ascii')
            
        except:
            clients.pop(uname)
            print(uname + ' has been logged out')
            clientConnected = False
def serverrun():           
    while serverRunning:
        try:
            client, address = s.accept()
            uname = client.recv(1024).decode('ascii')
            passuser = uname.split(",")
            filename = passuser[1]+"hashed.txt"
            fh = open(filename,"w")
            fh.writelines((passuser[0])+"\n")
            fh.writelines((passuser[1]))
            fh.close()
            client.send(("register").encode('ascii'))
        except:
            print("CONNECTION ERROR")
            break
        if(client not in clients):
            clients[uname] = client
            threading.Thread(target = handleClient, args = (client, uname, )).start()
serverrun()
