from tkinter import *
import time
import datetime
root = Tk()
root.geometry("290x120+0+0")
root.title('Digital Clock ')

root.configure(background ="black")
root.resizable(0,0)



def start():
    text = time.strftime("     %I : %M : %S  %p")
    label.config(text=text)
    x = datetime.datetime.now()
    text2 = x.strftime("%d %B %Y")
    date.config(text=text2)
    label.after(1000, start)
    date.after(86400000,start)


label = Label(root, font=("Verdana", 20, 'bold'), fg='red', bg="black")
label.grid(row=0, column=1)
dest = Label (root, text="Hour  Minute  Second" , font=("Verdana",12, 'bold'), fg='SpringGreen2', bg="black",height=1)
dest.grid(row= 1,column =1)
date = Label(root, font=("Verdana", 20, 'bold'), fg='red', bg="black",height=2 )
date.grid(row=4, column=1)
start()
root.mainloop()









