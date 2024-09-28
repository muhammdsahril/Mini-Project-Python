from cryptography.fernet import Fernet

'''def writeKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyFile:
        keyFile.write(key)'''
        
def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 


key = loadKey()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user + " | Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 


while True:
    mode = input("(VIEW/ADD/QUIT(q)?) ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid Input")
        continue
    