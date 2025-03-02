from tkinter import *
from tkinter import messagebox

def create_window():
    master = Tk()
    master.title("Week7 - Dream Cafe' Application by Natchanon Saileamonpiwat")
    master.geometry('800x700+300+100')
    master.option_add("*font", "tahoma 16")
    master.configure(bg='#EDDFE0')
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=5)
    master.grid_columnconfigure(0,weight=1)
    return (master)

def layout(master) :
    top.grid(row=0,sticky='news')
    top.grid_rowconfigure((0,1),weight=1)
    top.grid_columnconfigure((0,2),weight=1)
    top.grid_columnconfigure(1,weight=3)
    center.grid(row=1,sticky='news')
    center.rowconfigure((0,1,2),weight=1)
    center.columnconfigure((0,1,2,3),weight=1)
    bottom.grid(row=2,sticky='news')
    bottom.grid_rowconfigure(0,weight=1)
    bottom.grid_columnconfigure((0,1),weight=1)

def topframe(top) :
    Label(top,bg='#AB886D',image=img1).grid(row=0,column=0,rowspan=2)
    Label(top,bg='#AB886D',image=img2).grid(row=0,column=2,rowspan=2)
    Label(top,bg='#AB886D',text="Dream Cafe CumPee' Shop",font=('tahoma',28,'bold')).grid(row=0,column=1,sticky='s')
    Label(top,bg='#AB886D',text="Customers Like our family").grid(row=1,column=1,sticky='n')

def bottomframe(bottom) :
    Button(bottom,text='Exit Program '  ,width=15,command=resetclick).grid(row=0,column=0,sticky=E,padx=5,ipady=10)
    Button(bottom,text='Check Out ' ,width=15,command=checkout).grid(row=0,column=1,sticky=W,padx=5,ipady=10)

def centerframe(center) :
    Button(center,text='Cake Menu',image=img1,compound="top",command=cakeclick).grid(row=0,column=0,sticky='news')
    Button(center,text='Drink Menu',image=img2,compound="top",command=drinkclick).grid(row=1,column=3,sticky='news')
    Button(center,text='Coffee Menu',image=coffee1,compound="top",command=coffeeclick).grid(row=2,column=0,sticky='news')

def cakeclick() :
    cakeframe.grid(row=0,column=1,columnspan=3,sticky='news')
    cakeframe.grid_columnconfigure((0,1,2),weight=1)
    cakeframe.grid_rowconfigure(0,weight=1)
    Radiobutton(cakeframe,bg='#FFE3E3',text='Cake menu1\n(Price : 120 B)',image=cake1,compound='top',variable=cakespy,value=0).grid(row=0,column=0)
    Radiobutton(cakeframe,bg='#FFE3E3',text='Cake menu2\n(Price : 140 B)',image=cake2,compound='top',variable=cakespy,value=1).grid(row=0,column=1)
    Spinbox(cakeframe,from_=0,to=100,width=10,bg='black',fg='white',justify='center',textvariable=camt).grid(row=0,column=2)
    
def drinkclick() :
    drinkframe.grid(row=1,column=0,columnspan=3,sticky='news')
    drinkframe.rowconfigure(0,weight=1)
    drinkframe.columnconfigure((0,1,2),weight=1)
    Spinbox(drinkframe,from_=0,to=100,width=10,justify='center',bg='black',fg='white',textvariable=damt).grid(row=0,column=0)
    Radiobutton(drinkframe,bg='#FFF7D1',text='Drink menu1\n(Price : 75 B )',image=drink1,compound='top',variable=drinkspy,value=0).grid(row=0,column=1)
    Radiobutton(drinkframe,bg='#FFF7D1',text='Drink menu2\n(Price : 80 B )',image=drink2,compound='top',variable=drinkspy,value=1).grid(row=0,column=2)

def coffeeclick() :
    coffeeframe.grid(row=2,column=1,columnspan=3,sticky='news')
    coffeeframe.rowconfigure(0,weight=1)
    coffeeframe.columnconfigure((0,1,2),weight=1)
    Radiobutton(coffeeframe,bg='#ECDFCC',image=coffee2,text='Coffee menu1\n(Price : 50 B )',compound='top',variable=coffeespy,value=0).grid(row=0,column=0)
    Radiobutton(coffeeframe,bg='#ECDFCC',image=coffee3,text='Coffee menu2\n(Price : 60 B )',compound='top',variable=coffeespy,value=1).grid(row=0,column=1)
    Spinbox(coffeeframe,from_=0,to=100,width=10,justify='center',bg='black',fg='white',textvariable=cofamt).grid(row=0,column=2)


def checkout() :
    center2.grid(row=1,rowspan=2,sticky='news')
    bottom.grid_forget()
    center2.rowconfigure((0,1,2,3,4,5),weight=1)
    center2.columnconfigure(0,weight=1)
    cprice = camt.get() * price1[cakespy.get()]
    dprice = damt.get() * price2[drinkspy.get()]
    cofprice = cofamt.get() * price3[coffeespy.get()]
    total = cprice + dprice + cofprice
    Label(center2,bg='#EDDFE0',text='Thank you for your order ').grid(row=0)
    Label(center2,bg='#EDDFE0',text=f'Cake Price : {cprice:,.2f} Baht').grid(row=1)
    Label(center2,bg='#EDDFE0',text=f'Drink Price : {dprice:,.2f} Baht').grid(row=2)
    Label(center2,bg='#EDDFE0',text=f'Coffee Price : {cofprice:,.2f} Baht').grid(row=3)
    Label(center2,bg='#ECDFCC',text=f'Total Price : {total:,.2f}Baht').grid(row=4,sticky='news')
    Button(center2,text="Back to Menu",width=15,command=backtomenu).grid(row=5,ipady=10)


def resetclick() :
    cakeframe.grid_forget()
    drinkframe.grid_forget()
    coffeeframe.grid_forget()

    
def backtomenu() :
    center2.grid_forget()
    center.grid(row=1,sticky='news')
    bottom.grid(row=2,sticky='news')

#main
master = create_window()
top = Frame(master,bg='#AB886D')
center = Frame(master,bg='#D6C0B3')
center2 = Frame(master,bg='#EDDFE0')
bottom = Frame(master,bg='#E4E0E1')
cakeframe = Frame(center,bg='#FFE3E3')
drinkframe = Frame(center,bg='#FFF7D1')
coffeeframe = Frame(center,bg='#ECDFCC')
layout(master)
#create image variable
img1 = PhotoImage(file='Week7 CS311\image\cake-button.png')
img2 = PhotoImage(file='Week7 CS311\image\drink-button.png')
cake1 = PhotoImage(file='Week7 CS311\image\cake1.png')
cake2 = PhotoImage(file='Week7 CS311\image\cake2.png')
drink1 = PhotoImage(file='Week7 CS311\image\drink1.png')
drink2 = PhotoImage(file='Week7 CS311\image\drink2.png')
coffee1 = PhotoImage(file='Week7 CS311\image\coffee1.png')
coffee2 = PhotoImage(file="Week7 CS311\image\coffee3.png")
coffee3 = PhotoImage(file='Week7 CS311\image\coffee4.png')
#crate spy variable
cakespy = IntVar()
drinkspy = IntVar()
coffeespy = IntVar()
camt,damt,cofamt = IntVar(),IntVar(),IntVar()
bottomframe(bottom)
topframe(top)
centerframe(center)
price1 = [120,140]
price2 = [75,80]
price3 = [50,60]
master.mainloop()