from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


password = input("What is the master password? ")
key = load_key() + password.encode()
fer = Fernet(key)
mode = input("Would you like to add a new password or view existing ones (view,add), press q to quit. ").lower()

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,password = data.split("|")
            print("User:", user, ", Password: ", fer.decrypt(password.encode()).decode())
def add():
  name = input("Account Name: ")
  password = input("Password: ")

  with open("passwords.txt",'a') as f:
    f.write(name + '|' + fer.encrypt(password.encode()).decode() + "\n")

  while True:
    if mode == "q":
        break
    if mode == "view":
        view()
        break
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")