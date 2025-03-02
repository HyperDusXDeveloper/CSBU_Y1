from tkinter import *
from tkinter import messagebox

def create_window():
    master = Tk()
    master.title("Week7 - Dream Cafe' Application by Natchanon Saileamonpiwat")
    master.geometry('900x800')
    master.option_add("*font", "tahoma 16")
    master.configure(bg='#EDDFE0')
    master.grid_rowconfigure(0,weight=2)
    master.grid_rowconfigure(1,weight=2)
    master.grid_rowconfigure(2,weight=1)
    master.grid_rowconfigure(3,weight=2)
    master.grid_columnconfigure((0,1,2),weight=1)
    return (master)

def layout(master) :

    #TOP
    top.grid(row=0,columnspan=3,sticky='news')
    top.grid_rowconfigure((0,1,2),weight=1)
    top.grid_columnconfigure((0,1,2),weight=1)

    #CENTER CENTER
    centerc.grid(row=2,sticky='news',columnspan=3)
    centerc.grid_rowconfigure((0,1),weight=1)
    centerc.grid_columnconfigure((0,2),weight=1)
    centerc.grid_columnconfigure(1,weight=3)

    #BOTTOM
    bottom.grid(row=4,sticky='news',columnspan=3)
    bottom.grid_rowconfigure(0,weight=1)
    bottom.grid_columnconfigure((0,1,2),weight=1)
    
#FRAME

def topframe(top) :
    Button(top,text='Cake Menu',image=img1,compound="top",command=cakeclick).grid(row=0,rowspan=3,column=2,sticky='news')
    Button(top,text='Drink Menu',image=img2,compound="top",command=drinkclick).grid(row=0,rowspan=3,column=0,sticky='news')
    Button(top,text='Coffee Menu',image=coffee1,compound="top",command=coffeeclick).grid(row=0,rowspan=3,column=1,sticky='news')

def centercframe(centerc) :
    #TITLE
    Label(centerc,bg='#AB886D',image=img1).grid(row=0,column=0,rowspan=2,sticky=W,padx=20)
    Label(centerc,bg='#AB886D',image=img2).grid(row=0,column=2,rowspan=2,sticky=E,padx=20)
    Label(centerc,bg='#AB886D',text="Dream Cafe CumPee' Shop",font=('tahoma',28,'bold')).grid(row=0,columnspan=3,sticky='S')
    Label(centerc,bg='#AB886D',text="Customers Like our family").grid(row=1,columnspan=3,sticky=N,pady=10)

def bottomframe(bottom) :
    Button(bottom,text='Reset All',width=15,command=resetall,bg="#3F3FE9",fg="white").grid(row=0,column=0,sticky=E,padx=2,ipady=10,pady=20)
    Button(bottom,text='Check Out',width=15,command=checkout,bg="#FF8400",fg="white").grid(row=0,column=1,padx=2,ipady=10,pady=20)
    Button(bottom,text='Exit Program',width=15,command=exit,bg="#26B61C",fg="white").grid(row=0,column=2,sticky=W,padx=2,ipady=10,pady=20)

def cakeclick() :
        centertl.grid(row=1,column=0,sticky='news')
        centertl.grid_columnconfigure(0,weight=1)
        centertl.grid_rowconfigure(0,weight=1)
        Radiobutton(centertl,bg='#FFE3E3',text='Cake menu1\n(Price : 120 B)',image=cake1,compound='top',value=0,variable=menuspy).grid(row=0,column=0)
        centertr.grid(row=1,column=2,sticky='news')
        centertr.grid_rowconfigure(0,weight=1)
        centertr.grid_columnconfigure(0,weight=1)
        Spinbox(centertr,from_=0,to=100,width=10,bg='black',fg='white',textvariable=menuamt).grid(row=0,column=0)

def drinkclick() :
        centertc.grid(row=1,column=1,sticky='news')
        centertc.grid_columnconfigure(0,weight=1)
        centertc.grid_rowconfigure(0,weight=1)
        Radiobutton(centertc,bg='#FFF7D1',text='Drink menu1\n(Price : 75 B)',image=drink1,compound='top',value=1,variable=menuspy).grid(row=0,column=0)

def coffeeclick() :
        centerbc.grid(row=3,column=1,sticky='news')
        centerbc.grid_columnconfigure(0,weight=1)
        centerbc.grid_rowconfigure(0,weight=1)
        centerbr.grid(row=3,column=2,sticky='news')
        centerbr.grid_columnconfigure(0,weight=1)
        centerbr.grid_rowconfigure(0,weight=1)
        centerbl.grid(row=3,column=0,sticky='news')
        centerbl.grid_rowconfigure(0,weight=1)
        centerbl.grid_columnconfigure(0,weight=1)
        Radiobutton(centerbc,bg='#ECDFCC',text='Coffee menu1\n(Price : 50 B)',image=coffee3,compound='top',value=0,variable=coffeespy).grid(row=0,column=0)
        Radiobutton(centerbr,bg='#ECDFCC',text='Coffee menu2\n(Price : 60 B)',image=coffee4,compound='top',value=1,variable=coffeespy).grid(row=0,column=0)
        Spinbox(centerbl,from_=0,to=100,width=10,bg='black',fg='white',textvariable=cofamt).grid(row=0,column=0)

def resetall():
    centertl.grid_forget()
    centerbl.grid_forget()
    centertc.grid_forget()
    centerbc.grid_forget()
    centerbr.grid_forget()
    centertr.grid_forget()

def checkout():
    checkoutframetop.grid(row=1,column=0,columnspan=3,sticky='news')
    checkoutframetop.grid_rowconfigure((0,1),weight=1)
    checkoutframetop.grid_columnconfigure((0),weight=1)
    checkoutframebottom.grid(row=3,column=0,columnspan=3,sticky='news')
    checkoutframebottom.grid_rowconfigure((0,1,2),weight=1)
    checkoutframebottom.grid_columnconfigure((0),weight=1)
    checkoutframeback.grid(row=4,column=0,columnspan=3,sticky='news')
    checkoutframeback.grid_rowconfigure((0),weight=1)
    checkoutframeback.grid_columnconfigure((0),weight=1)

    menuprice = menuamt.get() * price1[menuspy.get()]
    coffeeprice = cofamt.get() * price2[coffeespy.get()]
    total = menuprice + coffeeprice

    Label(checkoutframetop,bg='white',text='Thank you for your order ',font=('tahoma',28,'bold')).grid(row=0,column=0)
    Label(checkoutframetop,bg='white',text=f'Create By Amway Shop Premium in every detail',font=('tahoma',15,'bold')).grid(row=1,column=0,sticky=N)
    Label(checkoutframebottom,bg='white',text=f'Mix Menu Price : {menuprice:,.2f} Baht',font=('tahoma',15,'bold')).grid(row=0,column=0)
    Label(checkoutframebottom,bg='white',text=f'Coffee Price : {coffeeprice:,.2f} Baht').grid(row=1,column=0,sticky='news')
    Label(checkoutframebottom,bg='#A16334',fg='white',font=('tahoma',20,'bold'),text=f'Total Price : {total:,.2f}Baht').grid(row=2,column=0,sticky='news')

    Button(checkoutframeback,text="Back to Menu",width=15,command=backtomenu,bg="black",fg="white").grid(row=0,ipady=10)

def backtomenu():
     checkoutframetop.grid_forget()
     checkoutframebottom.grid_forget()
     checkoutframeback.grid_forget()

# MASTER FRAME
master = create_window()

#TOP
top = Frame(master,bg='#AB886D')

#CENTER TOP
centertl = Frame(master,bg='#FFE3E3')
centertc = Frame(master,bg='#FFF7D1')
centertr = Frame(master,bg='#B2F7FF')
#CENTER CENTER
centerc = Frame(master,bg='#AB886D')

#CENTER BOTTOM
centerbl = Frame(master,bg='#ECDFCC')
centerbc = Frame(master,bg='#ECDFCC')
centerbr = Frame(master,bg='#ECDFCC')

#BOTTOM
bottom = Frame(master,bg='#E4E0E1')

checkoutframetop = Frame(master,bg="white")
checkoutframebottom = Frame(master,bg="white")
checkoutframeback = Frame(master,bg="white")

img1 = PhotoImage(file='Lerning/image/cake-button.png')
img2 = PhotoImage(file='Lerning/image/drink-button.png')
cake1 = PhotoImage(file='Lerning/image/cake1.png')
cake2 = PhotoImage(file='Lerning/image/cake2.png')
drink1 = PhotoImage(file='Lerning/image/drink1.png')
drink2 = PhotoImage(file='Lerning/image/drink2.png')
coffee1 = PhotoImage(file='Lerning/image/coffee1.png')
coffee2 = PhotoImage(file="Lerning/image/coffee2.png")
coffee3 = PhotoImage(file='Lerning/image/coffee3.png')
coffee4 = PhotoImage(file='Lerning/image/coffee4.png')

menuspy = IntVar()
coffeespy = IntVar()
menuamt,cofamt = IntVar(),IntVar()
price1 = [120,75]
price2 = [50,60]
layout(master)
topframe(top)
centercframe(centerc)
bottomframe(bottom)

master.mainloop()
