
password = 'getacess'

def get_acess():
    pass

def no_acess():
    pass

answer = input("Welcome to the password manager! Do you want to store the password here, type 'yes' or 'no'").lower()

if answer == 'yes':
    master_pwd = input("Type your password to get access: ").lower() 
    if master_pwd == password:
        get_acess()
    else:
        no_acess()    
    mode = input("Would you like to add a new password to the system, or view (type add, view) ").lower()  
elif answer == 'no':
    quit()
else:
    print("We are sorry to see you go!")

