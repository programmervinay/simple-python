from cryptography.fernet import Fernet
import os 
from time import sleep
from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import Image,ImageTk
import clipboard


# making the tkinter window 
root = Tk()
root.title("Password Manager")
root.geometry("800x400+300+200")
root.resizable(0,0)



# key = Fernet.generate_key()
fernet = Fernet(b'7zomxpbbjngnVbbKxfYotrlQaeFxCqS9dOEdk4v0Qus=')



#! THIS IS THE HELP SECTION 
def Help():
    messagebox.showinfo("Help box" ,">  To find the master key , contact to Vinay Prajapati\n >  to view the all saved passwords , type 'view' after enntering into the Home section\n>  to add the passwords , type 'add' after enntering into the Home section \n")


#! THIS IS THE ABOUT SECTION
def about():
    messagebox.showinfo("About this application","This Password manager is the best for you . \nIt help you to remember all the passwords and it is totally safe with Hash Technology.\n Totally End- TO - End Encryption  <--")

def Home(*args):

    global master_key_entry,add_btn,see_btn

    root.title("Home")
    password=str(master_key_entry.get().lower())

    if password=="karvin": 
        login_btn.pack_forget()
        Vinay.pack_forget()
        master_key_label.pack_forget()
        master_key_entry.pack_forget()
        #!add new password button 
        add_btn=Button(root,text="Add new Password",fg = "black",bg="floral white",font =("arial",20,"bold"),command=add_password_func)
        add_btn.pack(pady=5,padx=12)
        #!see the password button
        see_btn=Button(root,text="See Password",fg = "black",bg="floral white",font =("arial",20,"bold"),command=see_password_func)
        see_btn.pack(pady=8,padx=12)


    else:
        messagebox.showinfo("Wrong Password","Your Entered Password is wrong")
        master_key_entry.delete(0,END)
        master_key_entry.focus_set()


def add_password_func(*args):
    global name_entry ,name_label,pass_label,pwd_entry,submit,root_title
    def add_back():
        name_label.pack_forget()
        name_entry.pack_forget()
        pass_label.pack_forget()
        pwd_entry.pack_forget()
        Submit.pack_forget()
        back_btn.pack_forget()
        Home()
    add_btn.pack_forget()
    see_btn.pack_forget()
    root_title="Add Password"
    root.title(root_title)
    def retry():
        messagebox.showinfo("Error","First Enter the user name and the password and then click on the submit button")
        name_entry.delete(0,END)
        pwd_entry.delete(0,END)
        name_entry.focus_set()
    def file_manager():
        if len(name_entry.get())==0 or len(pwd_entry.get())==0:
            retry()

        else: 
            name= name_entry.get()
            pwd=pwd_entry.get()
            if not os.path.exists("C:\KARVIN_password_manager"):
                os.makedirs("C:\KARVIN_password_manager")
            file_Path = os.path.join("C:\KARVIN_password_manager","password.txt")
            with open (file_Path,"a") as f:	
                f.write(name + "|" + fernet.encrypt(pwd.encode()).decode() + "\n")
                f.close()
            messagebox.showinfo("PASSWORD ADDED","Your password is now submitted with encryption")
            name_entry.delete(0,END)
            pwd_entry.delete(0,END)
            name_entry.focus_set()

    # name=input("Enter the Account name: ").lower()  
    name_label= Label(root,text="Enter the User name : ",font=("arial",17,"bold"))
    name_label.pack(padx=1,pady=5)
    name_entry=Entry(root,width=20,fg="black",font=("arial",18,"italic"))
    name_entry.pack(padx=5,pady=5)
    # pwd=input("Enter the password : ")
    pass_label= Label(root,text="Enter the User's Password : ",font=("arial",17,"bold"))
    pass_label.pack(padx=1,pady=12)
    pwd_entry=Entry(root,width=20,fg="black",font=("arial",18,"italic"))
    pwd_entry.pack(padx=1,pady=12)
    name=name_entry.get()
    pwd=pwd_entry.get()
    Submit=Button(root,text="Submit Password",fg = "black",bg="floral white",font =("arial",20,"bold"),command=file_manager)
    Submit.pack(pady=8,padx=12)
    back_btn= Button(root,text="Back",fg="red",font=("arial",15,"bold"),command=add_back)
    back_btn.pack(side=BOTTOM,padx=5,pady=1)
    

def see_password_func():
    global see_name_entry,see_name_label,see_the_pass
    

    def see_back():
        try: 
            your_password.pack_forget()
            your_pass_button_1.pack_forget()
        except: 
            pass
        finally: 
            see_name_entry.pack_forget()
            see_name_label.pack_forget()
            see_the_pass.pack_forget()
            back_btn.pack_forget()
            Home()

    root_title="View Password"
    root.title(root_title)
    def see_pass(): 
        global your_password,your_pass_button_1
        input_account_name=see_name_entry.get().lower()
        def copy_text_bulider():
            clipboard.copy(f"{fernet.decrypt(passw.encode()).decode()}")
        flag =0
        f=  open("C:\KARVIN_password_manager\password.txt",'r') 
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            if (input_account_name) in user.lower():         
                flag=1
                break
        if flag==0:
            see_name_entry.delete(0,END)
            messagebox.showinfo("Error","User name not found :(")
        else:
            try:
                info=f"User name : {user}  ||  Password : {fernet.decrypt(passw.encode()).decode()}"
                your_password = Label(root,text=info,font=("arial",16,"bold"),fg="purple4")
                see_name_entry.delete(0,END)
                your_password.pack(padx=5,pady=8)
                your_pass_button_1= Button(root,text="Copy Password",fg="violetred1",font= ("arial",16,"bold"),command=copy_text_bulider)
                your_pass_button_1.pack(padx=5,pady=9)
            except:
                messagebox.showinfo("Error","Password not found !")
                see_name_entry.delete(0,END)    
                    

    add_btn.pack_forget()
    see_btn.pack_forget()
    see_name_label= Label(root,text="Enter the User name : ",font=("arial",17,"bold"))
    see_name_label.pack(padx=1,pady=5)
    see_name_entry=Entry(root,width=20,fg="black",font=("arial",18,"italic"))
    see_name_entry.pack(padx=5,pady=5)
    see_name_entry.focus_set()
    see_the_pass= Button(root,text="Search",font=("arial",19,"bold"),command=see_pass)
    see_the_pass.pack(padx=5,pady=1)

    back_btn= Button(root,text="Back",fg="red",font=("arial",15,"bold"),command=see_back)
    back_btn.pack(side=BOTTOM,padx=5,pady=1)

def open_yt():
    webbrowser.open("bit.ly/tlearnings",new=1)
def open_blog():
    webbrowser.open("bit.ly/tl-blogs",new=1)    


title_name = Label(root,text= ">>>>>>> PASSWORD MANAGER <<<<<<<", font=("arial",18,"bold"),fg="black")
title_name.pack(padx=12,pady=3)

#! MENU BAR FORMATION 
menubar= Menu(root)
m2= Menu(menubar,tearoff=0)     #!ABOUT MENU
m2.add_command(label="About",command= about)
menubar.add_cascade(label="About",menu=m2)
m3= Menu(menubar,tearoff=0)     #! HELP MENU
m3.add_command(label="Help",command= Help)
m3.add_command(label="Exit",command= root.quit)
menubar.add_cascade(label="Help",menu=m3)
m3= Menu(menubar,tearoff=0)     #! SELF-MOTIVATED  MENU
m3.add_command(label="YouTube Channel",command= open_yt)
m3.add_command(label="Our Blogs",command= open_blog)
menubar.add_cascade(label="Knowledge Pack",menu=m3)
root.config(menu=menubar)
master_key_label = Label(root,text= "Enter the Master Key ", font=("arial",18,"bold"),fg="black")
master_key_label.pack(padx=1,pady=12)

master_key_entry=Entry(root,width=20,fg="black",font=("arial",18,"italic"))
master_key_entry.pack(padx=5,pady=12)
master_key_entry.focus_set()
login_btn=Button(root,text="Login",fg = "black",bg="floral white",font =("arial",20,"bold"),command=Home)
login_btn.pack(pady=12,padx=0)

image=Image.open("D:\\python programming\\initial project\\vinay.png")
new_image =image.resize((340,205), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(new_image)

Vinay=Label(image=photo)
Vinay.pack(side=BOTTOM)




root.mainloop()
