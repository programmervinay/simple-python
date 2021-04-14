from tkinter import *
import random
from tkinter import messagebox
#################### root section
root = Tk()
root.geometry('800x600+400+100')
root.config(bg='powder blue')
root.title ('Typing Test App by Karvin')
root.resizable(False,False)

####################################### word list 
words = ['mango', 'laptop', 'hello', 'paper', 'karvin', 'overhead', 'liability', 'upload', 'password', 'charge', 'advertise', 'retailer', 'wholesaler', 'clause', 'order', 'treasurer', 'demand', 'affordable', 'profitable', 'client', 'fund', 'treasurer', 'sick', 'buffer', 'word-processor', 'bus', 'widget', 'binary', 'macro', 'Trojan horse', 'format', 'World', 'status', 'meeting', 'retire', 'salary', 'vice', 'discount', 'deflation', 'buy', 'estimate', 'negotiation', 'close', 'inventory', 'fire', 'overdraft', 'employee', 'recruiter', 'coupon', 'plan', 'financial', 'mailbox', 'leave', 'price', 'business-card', 'customer', 'creditcard', 'invest', 'goods', 'company', 'memo', 'ship', 'ads', 'interview', 'username', 'office', 'niche', 'quit', 'position', 'treasurer', 'money', 'budget', 'trade', 'market', 'sickleave', 'leave', 'efund', 'treasury', 'retail', 'economics', 'notebook', 'salesman', 'memo', 'economics', 'liability', 'intern']


################################ fuctions 
 
def labelslider():
    global count, sliderWords
    text= 'Welcome to Typing Test made by Vinay Prajapati'
    if (count >= len(text)):
        count=0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    heading.configure(text=sliderWords)
    heading.after(170,labelslider)

def startgame(event):
    global score, miss
    if time_left == 60:
        time()
    gameplay.configure(text='')
    if wordEntry.get() == wordlabel['text']:
        score += 1
        scorelabelcount.configure(text=score)

    else:
        miss += 1

    
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordEntry.delete(0,END)

def time():
    global time_left, score, miss
    if time_left > 10:
        pass
    else:
        timelabelcount.configure(fg='red')
    if (time_left > 0):
        time_left -= 1
        timelabelcount.configure(text=time_left)
        timelabelcount.after(1000, time)
    else:
        total_word = score + miss
        net_WPM = total_word-miss
        gross_WPM = total_word
        accuracy = net_WPM / gross_WPM * 100

        gameplay.configure(text=(f'| Correct = {score} | Wrong = {miss} | Total score = {score-miss} |'), fg='DarkGoldenrod1')
        resultlabel.configure(text=(f'| Typing Speed (in WPM) = {gross_WPM} | Accuracy = {round(accuracy,2)}% |'),fg='red')
        call = messagebox.askretrycancel('Notification', 'For play again Hit retry button')

        if (call == True):
            score=0
            time_left = 60 
            miss = 0
            timelabelcount.configure(text=time_left)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            gameplay.configure(text='Type word and Hit Enter Button',fg='dark grey')
            resultlabel.configure(text=" ")

            wordEntry.delete(0, END)




#################################### variables
score = 0
time_left = 60
count = 0
sliderWords = ''
miss=0
############################################# Label section


heading = Label(root, text='', font=('airal', 25, 'italic bold'), bg='powder blue',fg='red',width='40')
heading.place(x=10, y=10)
labelslider()

random.shuffle(words)
wordlabel = Label (root,text=words[0],font= ('airal',40,'bold'),bg='powder blue',fg='black')
wordlabel.place(x=320, y=210)

scorelabel = Label(root,text='Your score :',font= ('airal',20,'bold'),bg='powder blue',fg='black')
scorelabel.place(x=30, y=110)

scorelabelcount = Label(root, text=score, font=('airal', 20, 'bold'), bg='powder blue', fg='blue')
scorelabelcount.place(x=50, y=160)

timerlabel = Label(root, text='Time left', font=('airal', 20, 'bold'), bg='powder blue', fg='black')
timerlabel.place(x=600, y=110)


timelabelcount = Label(root, text=time_left, font=('airal', 20, 'bold'), bg='powder blue', fg='green')
timelabelcount.place(x=640, y=160)


gameplay = Label(root, text='Type word and Hit Enter Button', font=('airal', 15, ' italic bold'), bg='powder blue', fg='dark grey')
gameplay.place(x=200, y=450)

resultlabel = Label(root, text='', font=('airal', 15, ' italic bold'), bg='powder blue')
resultlabel.place(x=160,y=500)
#########################################  Entry section

wordEntry= Entry(root,font=('airal',25,'bold'),bg='powder blue',fg='blue',justify='center')

wordEntry.place(x=218,y=300)
wordEntry.focus_set()

############################## Binding enter button 
root.bind('<Return>',startgame)



root.mainloop()