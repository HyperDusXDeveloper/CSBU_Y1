from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def createwindow():
    master = Tk()
    master.geometry('500x800')
    master.option_add("*font", "tahoma 14")
    master.title("Week6 : Sweet Home Cafe' Application by natchanon Saileamonpiwat")
    master.configure(bg='light pink')
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=3)
    master.grid_columnconfigure(0,weight=1)
    return (master)

def layout(mater) :
    #left
    top.grid_rowconfigure((0),weight=1)
    top.grid_columnconfigure((0,1,2),weight=1)
    top.grid(row=0,column=0,sticky='news')
    Label(top,bg='#D6B79E',text='12:00').grid(row=0,column=2,sticky=NE,padx=20)
    Label(top,bg='black',text='Hello it me').grid(row=0,column=0,sticky=NW,padx=20)
    #center
    center.grid_rowconfigure((0),weight=1)
    center.grid_columnconfigure((0,1,2),weight=1)
    center.grid(row=1,column=0,sticky='news')

    #bottom
    bottom.grid_rowconfigure((0),weight=1)
    bottom.grid_columnconfigure((0,1,2),weight=1)
    bottom.grid(row=2,column=0,sticky='news')
master = createwindow()
top = Frame(master,bg='#AB886D')
center = Frame(master,bg='white')
bottom = Frame(master,bg='white')
#Button
cakebutton = PhotoImage(file='Lerning/image/cake-button.png')
drinkbutton = PhotoImage(file='Lerning/image/drink-button.png')
coffeebutton = PhotoImage(file='Lerning/image/coffee3.png')
checkoutbutton = PhotoImage(file='Lerning/image/checkout.png')
exitbutton = PhotoImage(file='Lerning/image/exit.png')
cancelbutton = PhotoImage(file='Lerning/image/cancel.png').subsample(2,2)
#CAKEIMG
cake1 = PhotoImage(file="Lerning/image/cake1.png")
cake2 = PhotoImage(file="Lerning/image/cake33.png")
cake3 = PhotoImage(file="Lerning/image/cake4.png")
drink1 = PhotoImage(file="Lerning/image/drink1.png")
drink2 = PhotoImage(file="Lerning/image/drink2.png")
drink3 = PhotoImage(file="Lerning/image/drink3.png")
coffee1 = PhotoImage(file="Lerning/image/coffee2.png")
coffee2 = PhotoImage(file="Lerning/image/coffee3.png")
coffee3 = PhotoImage(file="Lerning/image/coffee4.png")
    # Button(top,text='Product Menu',compound='top',image=cakebutton,width=150).grid(row=0,column=0,sticky='news')
    # Button(top,text='Check Out',compound='top',image=checkoutbutton,width=150).grid(row=1,column=0,sticky='news')
    # Button(top,text='Exit Program',compound='left',image=exitbutton,width=150).grid(row=2 , column=0,sticky='news')
layout(master)
master.mainloop()