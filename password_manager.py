from cryptography.fernet import Fernet
password = 'getacess'

def get_add():
    account_name = input("What's the account name: ").lower()
    second_pwd = input("Enter the password: ")
    with open("myfile.txt", 'a') as f:
        f.write(account_name + "|" + second_pwd + "\n")

def get_view():
    with open("myfile.txt", 'r') as f:
        for line in f.readlines():
            print(line)
            user, passw = line.split("|")
            print("Username ",user, "Password ",passw)

def get_acess():
    while True:
        mode = input("Would you like to add a new password to the system, or view (type add, view) or quit (q) ").lower()
        
        if mode == 'q':
            quit()

        if mode == 'add':
            get_add()
        elif mode == 'view':
            get_view()
        else:
            print("You have entered the wrong mode, try again!")

def no_acess():
    pass

# Code starts here 
answer = input("Welcome to the password manager! Do you want to store the password here, type 'yes' or 'no'").lower()

if answer == 'yes':
    master_pwd = input("Type your password to get access: ").lower() 
    if master_pwd == password:
        get_acess()
    else:
        no_acess()    
      
elif answer == 'no':
    print("We are sorry to see you go!")
    quit()
else:
    print("We are sorry to see you go!")

