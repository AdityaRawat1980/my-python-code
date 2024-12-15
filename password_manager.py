from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wd") as key_file:
        key_file.write(key) 
         

def load_key():
    file= open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("what is the master password ? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)
def view():
    with open('password.txt','r') as f :
        for line in f.readlines():
            data=line.rstrip()# as above used \n it give a space of line in code while reading also called as carriage rerturn so we have to strip it with the help of rstrip to remove
            if not data:
                continue
            user, passw = data.split("|") # hear user get the first accure element and password get the socond one  
            print("User","=",user,"---(●'◡'●)---","password","=",str(fer.decrypt(passw.encode())))
def add():
    # app = input(" Enter your application name for saveing the password:- ")
    name = input("Account name:- ")
    pwd = input("password:- ")
    with open("password.txt","a") as f : # if you open a file with file function so you have to close the manualy but with function will automatically close the file when the work is complited on that file
        # hear we are using the appnd mode for insert the data into it it mainly append the data at the end of file or if file is does not exist so it creat a new file
        # f.write("____________________" + app + "____________________" + "\n")
        f.write(name + "|" + str(fer.encrypt(pwd.encode()))) # hear we saprate the name and with the use of pipe opprater

while True:
    mode = input("would you like to add new password or view existing ones(view /add) or for quit press 'q' ? ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else :
        print("invalid mode")
        continue
