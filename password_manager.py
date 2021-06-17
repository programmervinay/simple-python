from cryptography.fernet import Fernet
import os 
from time import sleep

# key = Fernet.generate_key()
fernet = Fernet(b'7zomxpbbjngnVbbKxfYotrlQaeFxCqS9dOEdk4v0Qus=')
def about():
    print("This Password manager is the best for you . \nIt help you to remember all the passwords and it is totally safe with Hash Technology.\n Totally End- TO - End Encryption \n\n\n Hit Enter to go back  <--")
    l= input()
    if l=="":
        clear()
        start()


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def add():
    name=input("Enter the Account name: ").lower()  
    pwd=input("Enter the password : ")
    
    if not os.path.exists("C:\KARVIN_password_manager"):
        os.makedirs("C:\KARVIN_password_manager")
    file_Path = os.path.join("C:\KARVIN_password_manager","password.txt")
    with open (file_Path,"a") as f:	
        f.write(name + "|" + fernet.encrypt(pwd.encode()).decode() + "\n")
        f.close()

def view():
    input_account_name = input("Enter the account name to find password : ").lower()
    flag =0
    f=  open("C:\KARVIN_password_manager\password.txt",'r') 
    for line in f.readlines():
        data = line.rstrip()
        user, passw = data.split("|")
        if input_account_name in user:         
            flag=1
            break
    if flag==0:
        print("User name not found:( ")
    else:
        try:
            print("\n__________User : ",user,"| Password : ",fernet.decrypt(passw.encode()).decode(),"_____________\n")
        except:
            print("not found")
def help():
    print(">  To find the master key , contact to Vinay Prajapati")
    print(">  to view the all saved passwords , type 'view' after enntering into the Home section ")
    print(">  to add the passwords , type 'add' after enntering into the Home section ")
    print("Hit Enter to go back to start menu")
    l= input()
    if l=="":
        clear()
        start()




def start():
    print(">>>>>>>>>>>>>  WELCOME TO THE PASSWORD MANAGER <<<<<<<<<<<<<<<<<")
    print('           made by Vinay Prajapati')
    print("\n\n~ ~ ~ ~ ~ ~ MENUS ~ ~ ~ ~ ~ ~")
    print("1. Home \n 2. About \n 3. Help\n 4. QUIT ")
    what_w = int (input("\nEnter the option number that you want to do (1/2/3/4): "))
    if what_w==1:
        masterkey="karvin"
        check=input("\nEnter the  master key to open the password manager : ")
        if check==masterkey:
            while True:
                take=input("\nEnter what you want either view passwords / add password / quit : ").lower()
                if "add" in take:
                    add()
                elif "view" in take:
                    view()
                elif "q"in take:
                    exit()
                else:
                    clear()
                    start()
        else :
            print("You Entered Wrong Master Password :( ")
            ques=input("Want to try again (yes/no) : ")
            if "yes" in ques or "y"in ques:
                sleep(1)
                clear()
                start()
            else:
                help()
    elif what_w==2:
        clear()
        about()
    elif what_w==3:
        help()
    else:
        exit()


    
            
start()





