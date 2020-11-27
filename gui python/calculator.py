from tkinter import *
import tkinter.messagebox as tmsg
root= Tk()
root.geometry("305x490")
root.minsize (305,490)
root.maxsize (305,490)
root['bg']="grey15"
root.title("Quick Calculator ")


def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            vlaue= int (scvalue.get())
        else :
            try:
                value = eval(screen.get())
            except Exception as e :
                    value="Error"

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

 
def  myfunc():
 
    tmsg.showinfo("About", "This calculator is made by Vinay prajapaati")


menu1=Menu(root)
about=Menu(menu1,tearoff=0)
about.add_command(label="About",command=myfunc, activebackground="blue",activeforeground="white")
about.add_separator()
about.add_command(label="Exit",command=root.destroy, activebackground="red",activeforeground="white")
root.config(menu=menu1)
menu1.add_cascade(label="Options",menu=about)



scvalue=StringVar()
scvalue.set (" ")
screen= Entry (root , textvar=scvalue, font="lucida 20 bold",borderwidth=5 , relief= SUNKEN)
screen.pack(padx=1,pady=10)


f= Frame(root, bg="grey")
b = Button(f,text= "9",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "8",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "7",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "-",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
f.pack()



f= Frame(root, bg="grey")

b = Button(f,text= "6",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "5",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "4",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "+",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
f.pack()




f= Frame(root, bg="grey")
b = Button(f,text= "3",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "2",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "1",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "*",font="lucida 32 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
f.pack()


f= Frame(root, bg="grey")
b = Button(f,text= "0",font="lucida 30 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= ".",font="lucida 33 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "/",font="lucida 34 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b = Button(f,text= "=",font="lucida 26 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
f.pack()



f=Frame(root, bg="grey")
b = Button(f,text= "C",font="lucida 30 bold")
b.pack(side=RIGHT,padx=10)
b.bind("<Button-1>",click)

f.pack()



root.mainloop()
