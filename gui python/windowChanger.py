from tkinter import *
import random 
from tkinter import messagebox



colour =['red','green', 'blue','white','grey','lightcyan','powder blue','grey32', 'grey12','pale green','gold','gold3']
random.shuffle(colour)

root = Tk()
width = 220
height =140
root.title('window changer')
root.geometry(f'{width}x{height}+500+200')
root.config(bg='powder blue')
root.resizable(False,False)




colour =['red','green', 'blue','white','grey','lightcyan','powder blue','snow4',    'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','pale green','gold','gold3']
random.shuffle(colour)



def changer(event):
    global width, height,colour
    try:
        nw =int(widthx.get())
        nh=int(heighty.get())
        if nw >= width and nh>=height:
            root.geometry(f'{nw}x{nh}+500+200')
            root.config(bg=colour[3])
            widthlabel.configure(bg=colour[3])
            heightlabel.configure(bg=colour[3])

        elif nw < width and nh < height:
            messagebox.showwarning('magnitude error','Enter the value of width and height more than 220 and 140 respectively !')
            
        else:
            pass
    except:
        messagebox.showinfo('Error','First enter the value of width and height and then hit Enter Button')
    finally:
        widthx.delete(0,END)
        heighty.delete(0,END)
        root.resizable(False, False)
        widthx.focus_set()
        random.shuffle(colour)


widthlabel = Label(root,text='Enter width :',font= ('airal',12,'bold'),bg='powder blue',fg='black')
widthlabel.grid(row=0,column=1)


widthx= Entry(root,width=10)
widthx.grid(row=0,column=3)
widthx.focus_set()

heightlabel = Label(root,text='Enter height :',font= ('airal',12,'bold'),bg='powder blue',fg='black')
heightlabel.grid(row=1,column=1)


heighty= Entry(root,width=10)
heighty.grid(row=1, column=3)




root.bind('<Return>', changer)

    
    
root.mainloop()

