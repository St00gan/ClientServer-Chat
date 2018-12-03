import socket
import getpass
import hashlib
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4242
fh = open("data/ip.txt", "r+")
ip2 = fh.read()
ipchange = input("Do you want to manually set IP of server? (Y/N): ")
if ipchange == "Y" or "y":
    ip2 = input("What do you want to set the ip to?: ")
else:
    ip2 = ip2
fh.close()
try:
    s2.connect((ip2, port))
except:
    print('PASSWORD SERVER IS OFFLINE RIGHT NOW')
    exit()
user = input("Username: ")
fh = open("data/user.txt", "w")
fh.writelines(user)
fh.close()
pswd = getpass.getpass('Password:').encode("ascii")
pswd = hashlib.md5(pswd)
pswd = pswd.hexdigest()
password = ((str(pswd)) + "," + (str(user)))
try:
    msg = password
    s2.send(msg.encode('ascii'))
except:
    print('PASSWORD SERVER IS OFFLINE RIGHT NOW')
    exit()
returned = s2.recv(1024).decode('ascii')
if returned == "success":
    print("Login Success")
else:
    print("Login Failed")
fh = open("data/login.txt", "w")
fh.writelines(returned)
fh.close()
