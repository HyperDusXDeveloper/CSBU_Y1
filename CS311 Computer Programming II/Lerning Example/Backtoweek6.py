from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def createwindow():
    master = Tk()
    master.geometry('1300x800')
    master.option_add("*font", "tahoma 14")
    master.title("Week6 : Sweet Home Cafe' Application by natchanon Saileamonpiwat")
    master.configure(bg='light pink')
    master.grid_rowconfigure(0,weight=1)
    master.grid_columnconfigure(0,weight=1)
    master.grid_columnconfigure(1,weight=5)
    return (master)

def layout(mater) :
    #left
    left.grid_rowconfigure((0,1,2),weight=1)
    left.grid_columnconfigure((0),weight=1)
    left.grid(row=0,column=0,sticky='news')
    Button(left,text='Product Menu',compound='top',image=cakebutton,width=150,command=productclick).grid(row=0,column=0,sticky='news')
    Button(left,text='Check Out',compound='top',image=checkoutbutton,width=150,command=checkoutclick).grid(row=1,column=0,sticky='news')
    Button(left,text='Exit Program',compound='left',image=exitbutton,width=150,command=exit).grid(row=2 , column=0,sticky='news')

def productclick():
    checkoutframe.grid_forget()
    productframe.grid_rowconfigure((0,1,2),weight=1)
    productframe.grid_columnconfigure((0,1,2),weight=1)
    productframe.grid(row=0,column=1,sticky='news')

    cakeimage = [cake1,cake2,cake3]
    drinkimage = [drink1,drink2,drink3]
    coffeeimage = [coffee1,coffee2,coffee3]
    for i,cake in enumerate(cakemenu) :
        Label(productframe,bg='#FFDBF3',text=f'{cake}Price : {price1[i]}',image=cakeimage[i],compound='right').grid(row=i,column=0)
        Spinbox(productframe,from_=0, to=200,font=('tahoma',16,'bold'),width=9,justify='center',textvariable=cakespy[i]).grid(row=i,column=0,sticky=S,pady=30)
        cakeimage = [cake1,cake2,cake3]
    for i,drink in enumerate(drinkmenu) :
        Label(productframe,bg='#FFDBF3',text=f'{drink}Price : {price1[i]}',image=drinkimage[i],compound='right').grid(row=i,column=1)
        Spinbox(productframe,from_=0, to=200,font=('tahoma',16,'bold'),width=9,justify='center',textvariable=drinkspy[i]).grid(row=i,column=1,sticky=S,pady=30)
    for i,coffee in enumerate(coffeemenu) :
        Label(productframe,bg='#FFDBF3',text=f'{coffee}Price : {price1[i]}',image=coffeeimage[i],compound='right').grid(row=i,column=2)
        Spinbox(productframe,from_=0, to=200,font=('tahoma',16,'bold'),width=9,justify='center',textvariable=coffeespy[i]).grid(row=i,column=2,sticky=S,pady=30)

def checkoutclick():
    global sumcake,sumdrink,sumcoffee,total,t
    sumcake,sumdrink,sumcoffee = 0,0,0
    checkoutframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    checkoutframe.grid_columnconfigure((0,1),weight=1)
    checkoutframe.grid(row=0,column=1,sticky='news')
    for i,cake in enumerate(price1) :
        sumcake += cakespy[i].get() * price1[i]
        sumdrink += drinkspy[i].get() * price2[i]
        sumcoffee += coffeespy[i].get() * price3[i]
    total = sumcake + sumdrink + sumcoffee
    Label(checkoutframe,text='~ Thank you for order ~',font=('comic sans ms',30,'bold'),bg='#EAE0E0').grid(row=0,columnspan=2)
    Label(checkoutframe,text=f'Cake price : {sumcake:,.2f}',bg='#EAE0E0',font=('tahoma',16)).grid(row=1,sticky='news',columnspan=2)
    Label(checkoutframe,text=f'Drink price : {sumdrink:,.2f}',bg='#EAE0E0',font=('tahoma',16)).grid(row=2,sticky='news',columnspan=2)
    Label(checkoutframe,text=f'Coffee price : {sumdrink:,.2f}',bg='#EAE0E0',font=('tahoma',16)).grid(row=3,sticky='news',columnspan=2)
    t = Label(checkoutframe,text=f'Tota price : {total:,.2f} Baht',font=('comic sans ms',20,'bold'),bg='#AB886D')
    t.grid(row=4,sticky='news',columnspan=2)
    Button(checkoutframe,text='THB',compound='right',image=cancelbutton,command=THB,bg='black',fg='white').grid(row=5 ,column=0,sticky='news')
    Button(checkoutframe,text='USD',compound='right',image=cancelbutton,command=USD,bg='black',fg='white').grid(row=5 ,column=1,sticky='news')
    
def THB():
    t["text"] = f'Tota price : {total:,.2f} THB'
def USD():
    t["text"] = f'Tota price : {total/35:,.2f} USD'
master = createwindow()
left = Frame(master,bg='#AB886D')
right = Frame(master,bg='white')
productframe = Frame(master,bg='#FFDBF3',height=300)
checkoutframe = Frame(master,bg='#EAE0E0')
#IMG BUTTON
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
cakemenu = [' Strawberry Cake \n'," Cheese   Cake  \n","Newyork Cheese Cake\n"]
drinkmenu = [' Orange   Mixed \n',' Lemonade Mixed \n'," Mojito  Miexd  Berry \n"]
coffeemenu = ["Hot Latte\n","Hot Cappuccino\n","Hot Caramel Latte\n"]
price1 = [145,120,130]
price2 = [120,100,90]
price3 = [110,160,50]
cakespy = [IntVar() for x in price1]
drinkspy = [IntVar() for x in price2]
coffeespy = [IntVar() for x in price3]
layout(master)
master.mainloop()