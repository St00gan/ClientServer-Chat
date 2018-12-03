import socket
import getpass
import hashlib
fh = open("data/login.txt", "w")
fh.writelines("bad")
fh.close()
passwordsame = "f"
inc = False
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4243
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
    print('REGISTRATION SERVER IS OFFLINE RIGHT NOW')
    exit()
user = input("Username: ")
fh = open("data/user.txt", "w")
fh.writelines(user)
fh.close()
global pswd
global pswd2
pswd = ""
pswd2 = ""
def getpassword():
    global pswd
    global pswd2
    pswd = getpass.getpass('Password:')
    pswd2= getpass.getpass('Please Enter your Password again:')
while passwordsame == "f":
    if inc == True:
        print("The 2 Passwords did not match, please try again")
    getpassword()
    if pswd == pswd2:
        passwordsame = "t"
        inc = False
    elif pswd != pswd2:
        passwordsame = "f"
        inc = True
    else:
        print("Python Broke")
pswd = pswd.encode("ascii")
pswd = hashlib.md5(pswd)
pswd = pswd.hexdigest()
password = ((str(pswd)) + "," + (str(user)))
try:
    msg = password
    s2.send(msg.encode('ascii'))
except:
    print('REGISTRATION SERVER IS OFFLINE RIGHT NOW')
    exit()
returned = s2.recv(1024).decode('ascii')
if returned == "register":
    print("Registration Success")
else:
    print("Registration Failed")
fh = open("data/login.txt", "w")
fh.writelines(returned)
fh.close()
