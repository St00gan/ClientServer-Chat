def program():
    #Project Started 27/09/18
    #This project is meant to be a voice and text chat service that will use low system resources
    #This is gonna be an ambitious project but I want to try as I feel its important
    #Version 0.8.0
    version = "0.8.0"
    def clear():
        print('\n'*1000)
    print("Importing Requirements")
    try:
        import os
        import os.path
        import socket
        import getpass
        import threading
        import sys
    except:
        print("Modules could not be loaded, please install required modules")
        input()
        exit()
    clear()
    print("Defining Functions")
    try:
        def text():
            try:
                import clientchat
            except:
                print('The Chat system isn\'t working right now. Please try again later')
        def voice():
            try:
                import clientvoice
            except:
                print('The Voice Chat system isn\'t working right now. Please try again later')
        def settings():
            print("""What setting would you like to change?
        1. IP visibility
        2. Account Storage
        3. Refresh Program
        4. Return to Menu""")
            settingchoice = input()
            if (settingchoice == "1"):
                clear()
                visip()
                settings()
            elif (settingchoice == "2"):
                clear()
                userpasssave()
                settings()
            elif (settingchoice == "3"):
                clear()
                program()
            elif (settingchoice == "4"):
                clear()
                menu()
            else:
                clear()
                print("PLEASE USE 1,2,3 OR 4 \n")
                settings()
        def exitprog():
            exit()
        def hostsearch():
            global host_ip
            try: 
                import ipgrab
                ipname = os.path.join("data","ip.txt")
                fh = open(ipname, "r+")
                host_ip = fh.read()
                fh.close()
            except: 
                print("Unable to get IP")
                repeat = input("(Y/N) try again?: ")
                if (repeat == ("N")) or (repeat == ("n")):
                    quit
                elif (repeat == ("Y")) or (repeat == ("y")):
                    hostsearch()
                elif (repeat == ("OFFLINE")) or (repeat == ("offline")):
                    host_ip = "127.0.1.1"
        def visip():
            global host_ip
            print("Do you want your ip to be visible? (Y/N)")
            vis_ip = input()
            if (vis_ip == ("Y")) or (vis_ip == ("y")):
                host_ip = host_ip
            elif (vis_ip == ("N")) or (vis_ip == ("n")):
                host_ip = ("REDACTED")
            else:
                clear()
                print("Please use \"Y\" or \"N\"")
                visip()
        def menu():
            print("Your IPv4 address is "+host_ip)
            print("Welcome to tempchat version "+version+" "+user)
            print("This program was created by St00gan, Eden and Deepank92")
            print("""Pick an option with the numbers:
        1. Text Chats
        2. Voice Chats
        3. Settings
        4. Exit""")
            select = input()
            if (select == "1"):
                clear()
                text()
            elif (select == "2"):
                clear()
                voice()
            elif (select == "3"):
                clear()
                settings()
            elif (select == "4"):
                clear()
                exitprog()
            else:
                clear()
                print("PLEASE USE 1,2,3 OR 4 \n")
                menu()
    except:
        print("Programs could not be defined")
        input()
        exit()
    print("Obtaining your IP Address")
    hostsearch()
    clear()
    visip()
    clear()
    user = ""
    login = "bad"
    while (login == "failed") or (login == "bad") or (login == "register"):
        clear()
        print("Welcome to tempchat")
        print("Your IPv4 address is "+host_ip)
        lr = input("Do you want to 1. Login or 2. Register? (Use 1 / 2): ")
        if lr == "1":
            while (login == "bad") or (login == "register"):
                try:
                    import LoginSystem
                    fh = open("data/login.txt", "r+")
                    login = fh.read()
                    fh.close()
                    print("LOGGED IN")
                except:
                    print('The login system failed. Please try again later')
        elif lr == "2":
            while (login == "bad"):
                try:
                    import RegisterSystem
                    fh = open("data/login.txt", "r+")
                    login = fh.read()
                    fh.close()
                    print("REGISTERED")
                except:
                    print('The registration system failed. Please try again later')
    if login == "success":
        print("login success")
    clear()
    menu()
program()
