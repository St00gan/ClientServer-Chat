import socket
import threading
import os.path

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
ip = str(socket.gethostbyname(socket.gethostname()))
port = 4242

clients = {}

s.bind((ip, port))
s.listen()
print('Password Server Ready...')
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
        client, address = s.accept()
        uname = client.recv(1024).decode('ascii')
        passuser = uname.split(",")
        filename = passuser[1]+"hashed.txt"
        if (os.path.isfile(filename)):
            fh = open(filename,"r")
            real = list(fh)
            realpass = str(real[0])
            userpass = str(passuser[0])
            realpass = realpass[:32]
            userpass = userpass[:32]
            uname = str(passuser[1])
            if (realpass == userpass):
                login = True
                print(uname+" succesfully logged in with "+userpass)
                client.send(("success").encode('ascii'))
            elif (realpass != userpass):
                login = False
                print (uname+" was not able to log in with " + realpass + " as what they typed was " + userpass)
                client.send(("failed").encode('ascii'))
                serverrun()
            else:
                print("Unexpected Server Error")
        else:
            fh = open(filename,"w")
            fh.writelines((passuser[0])+"\n")
            fh.writelines((passuser[1]))
            fh.close()
            login = True
            client.send(("success").encode('ascii'))
        if(client not in clients):
            clients[uname] = client
            threading.Thread(target = handleClient, args = (client, uname, )).start()
serverrun()
