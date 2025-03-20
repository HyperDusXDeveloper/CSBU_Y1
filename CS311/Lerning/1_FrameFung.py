from tkinter import *
from tkinter import ttk

def createwindow():
    master = Tk()
    master.geometry('1000x800+300+100')
    master.option_add("*font", "tahoma 14")
    master.title("Week6 : Sweet Home Cafe' Application by natchanon Saileamonpiwat")
    master.configure(bg='light pink')
    master.grid_rowconfigure(0,weight=2)
    master.grid_rowconfigure(1,weight=4)
    master.grid_rowconfigure(2,weight=1)
    master.grid_columnconfigure((0,1,2),weight=1)
    return (master)

def layout(mater) :

    #top
    top.grid_rowconfigure((0,1,2),weight=1)
    top.grid_columnconfigure((0,1,2),weight=1,minsize=266)
    top.grid(row=0,column=0,columnspan=3,sticky='news')

    #center
    center.grid_rowconfigure((0,1,2),weight=1)
    center.grid_columnconfigure((0,1,2),weight=1 , minsize=266)
    center.grid(row=1,column=0,columnspan=3,sticky='news')

    #bottom
    bottom.grid_rowconfigure(0,weight=1)
    bottom.grid_columnconfigure(0,weight=1)
    bottom.grid(row=2,column=0,columnspan=3,sticky='news')


def topframe(top) :
    Label(top,bg='#AB886D',image=cakebutton).grid(row=0,column=0,rowspan=2,columnspan=3,sticky=W,padx=40)
    Label(top,bg='#AB886D',image=drinkbutton).grid(row=0,column=2,rowspan=2,columnspan=3,sticky=E,padx=40)
    Label(top,bg='#AB886D',text="Dream Cafe Shop",font=('tahoma',28,'bold')).grid(row=0,column=0,columnspan=3,sticky=S)
    Label(top,bg='#AB886D',text="Customers Like our family").grid(row=1,column=0,sticky=N,columnspan=3)
    Button(top,text='Cake Menu',compound='left',image=cakebutton,command=cakebottonclick).grid(row=2 , column=0,sticky='news')
    Button(top,text='Drink Menu',compound='left',image=drinkbutton,command=drinkbottonclick).grid(row=2,column=1,sticky='news')
    Button(top,text='Coffee Menu ',compound='left',image=coffeebutton,command=coffeebottonclick).grid(row=2,column=2,sticky='news')
def bottomframe(bottom) :
    Button(bottom,text='Reset All',compound='right',image=cancelbutton,width=150,command=resetsubmit).grid(row=0,column=0,ipady=10,sticky=W,padx=140)
    Button(bottom,text='Check Out',compound='right',image=checkoutbutton,width=150,command=checkout).grid(row=0,column=0,ipady=10)
    Button(bottom,text='Exit Program',compound='right',image=cancelbutton,width=150,command=exit).grid(row=0 , column=0,ipady=10,sticky=E,padx=140)

def cakebottonclick():
    cakeframe.grid_rowconfigure((0,1,2),weight=1)
    cakeframe.grid_columnconfigure((0),weight=1)
    cakeframe.grid(row=1,column=0,sticky='news')
    cakeframe.grid_propagate(False)
    cakeimage = [cake1,cake2,cake3]
    for i,cake in enumerate(cakemenu) :
        Label(cakeframe,bg='#FFDBF3',text=f'{cake}Price :{price1[i]}',image=cakeimage[i],compound='left').grid(row=i,column=0,sticky=N,pady=10)
        Entry(cakeframe,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=cakespy[i]).grid(row=i,column=0,sticky=S,pady=10)
    
def drinkbottonclick():
    drinkframe.grid_rowconfigure((0,1,2),weight=1)
    drinkframe.grid_columnconfigure((0),weight=1)
    drinkframe.grid(row=1,column=1,sticky='news')
    drinkframe.grid_propagate(False)
    cakeimage = [drink1,drink2,drink3]
    for i,drink in enumerate(drinkmenu) :
        Label(drinkframe,bg='#A5F9FF',text=f'{drink}Price :{price2[i]}',image=cakeimage[i],compound='left').grid(row=i,column=0,sticky=N,pady=10)
        Entry(drinkframe,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=drinkspy[i]).grid(row=i,column=0,sticky=S,pady=10)

def coffeebottonclick():
    coffeeframe.grid_rowconfigure((0,1,2),weight=1)
    coffeeframe.grid_columnconfigure((0),weight=1)
    coffeeframe.grid(row=1,column=2,sticky='news')
    coffeeframe.grid_propagate(False)
    cakeimage = [coffee1,coffee2,coffee3]
    for i,coffee in enumerate(coffeemenu) :
        Label(coffeeframe,bg='#D6B79E',text=f'{coffee}Price :{price3[i]}',image=cakeimage[i],compound='left').grid(row=i,column=0,sticky=N,pady=10)
        Entry(coffeeframe,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=coffeespy[i]).grid(row=i,column=0,sticky=S,pady=10)

def resetsubmit():
    center['bg'] = 'black'
    checkoutframe.grid_forget()
    cakeframe.grid_forget()
    drinkframe.grid_forget()
    coffeeframe.grid_forget()
    checkoutframe.grid_forget()
    for i,price in enumerate(price1) : 
        cakespy[i].set(0)
        drinkspy[i].set(0)
        coffeespy[i].set(0)
        
def checkout():
    global sumcake,sumdrink,sumcoffee
    sumcake,sumdrink,sumcoffee = 0,0,0
    cakeframe.grid_forget()
    drinkframe.grid_forget()
    coffeeframe.grid_forget()
    checkoutframe.grid_rowconfigure((0,1,2,3,4),weight=1)
    checkoutframe.grid_columnconfigure((0),weight=1)
    checkoutframe.grid(row=1,column=0,columnspan=3,sticky='news')
    for i,cake in enumerate(price1) :
        sumcake += cakespy[i].get() * price1[i]
        sumdrink += drinkspy[i].get() * price2[i]
        sumcoffee += coffeespy[i].get() * price3[i]
    total = sumcake + sumdrink + sumcoffee
    Label(checkoutframe,text='~ Thank you for order ~',font=('tahoma',30,'bold'),bg='#EAE0E0').grid(row=0)
    Label(checkoutframe,text=f'Cake price : {sumcake:,.2f}',bg='#EAE0E0',font=('tahoma',16)).grid(row=1,sticky='news')
    Label(checkoutframe,text=f'Drink price : {sumdrink:,.2f}',bg='#EAE0E0',font=('tahoma',16)).grid(row=2,sticky='news')
    Label(checkoutframe,text=f'Coffee price : {sumdrink:,.2f}',bg='#EAE0E0',font=('tahoma',16)).grid(row=3,sticky='news')
    Label(checkoutframe,text=f'Tota price : {total:,.2f} Baht',font=('tahoma',16),bg='#AB886D').grid(row=4,sticky='news')

    checkoutframebottom.grid_rowconfigure((0),weight=1)
    checkoutframebottom.grid_columnconfigure((0),weight=1)
    checkoutframebottom.grid(row=2,column=0,columnspan=3,sticky='news')
    Button(checkoutframebottom,text='Exit',compound='right',image=cancelbutton,width=150,command=exit).grid(row=0,column=0,ipady=10,sticky=W,padx=200)
    Button(checkoutframebottom,text='Back to',compound='right',image=amway,width=250,command=backtomenu).grid(row=0 , column=0,ipady=10,sticky=E,padx=180)
def backtomenu():
    checkoutframe.grid_forget()
    checkoutframebottom.grid_forget()
    top.grid(row=0,column=0,columnspan=3,sticky='news')
    bottom.grid(row=2,column=0,columnspan=3,sticky='news')

master = createwindow()
top = Frame(master,bg='#AB886D')
center = Frame(master,bg='white')
bottom = Frame(master,bg='#FCFCFC')
cakeframe = Frame(master,bg='#FFDBF3',height=300)
drinkframe = Frame(master,bg='#A5F9FF',height=300)
coffeeframe = Frame(master,bg='#D6B79E',height=300)
checkoutframe = Frame(master,bg='#EAE0E0')
checkoutframebottom = Frame(master,bg='white')
#IMG BUTTON
cakebutton = PhotoImage(file='Lerning/image/cake-button.png')
drinkbutton = PhotoImage(file='Lerning/image/drink-button.png')
coffeebutton = PhotoImage(file='Lerning/image/coffee3.png')
checkoutbutton = PhotoImage(file='Lerning/image/checkout.png')
exitbutton = PhotoImage(file='Lerning/image/exit.png')
cancelbutton = PhotoImage(file='Lerning/image/cancel.png').subsample(2,2)
amway = PhotoImage(file='Lerning/image/Amway.png').subsample(3,3)
#CAKEIMG
cake1 = PhotoImage(file="Lerning/image/cake1.png").subsample(2,2)
cake2 = PhotoImage(file="Lerning/image/cake2.png").subsample(2,2)
cake3 = PhotoImage(file="Lerning/image/cake3.png").subsample(2,2)
drink1 = PhotoImage(file="Lerning/image/drink1.png").subsample(2,2)
drink2 = PhotoImage(file="Lerning/image/drink2.png").subsample(2,2)
drink3 = PhotoImage(file="Lerning/image/drink3.png").subsample(2,2)
coffee1 = PhotoImage(file="Lerning/image/coffee2.png").subsample(2,2)
coffee2 = PhotoImage(file="Lerning/image/coffee3.png").subsample(2,2)
coffee3 = PhotoImage(file="Lerning/image/coffee4.png").subsample(2,2)
cakemenu = [' Cake 1 \n'," Cake 2  \n","Cake 3\n"]
drinkmenu = [' Drink 1 \n'," Drink 2  \n"," Drink 3\n"]
coffeemenu = [' Coffee 1 \n'," Coffee 2 \n"," Coffee 3\n"]
price1 = [145,120,130]
price2 = [120,100,90]
price3 = [110,160,50]
cakespy = [IntVar() for x in price1]
drinkspy = [IntVar() for x in price2]
coffeespy = [IntVar() for x in price3]
layout(master)
topframe(top)
bottomframe(bottom)
master.mainloop()


# def cakebottonclick():
#     checkoutframebottom.grid_forget()
#     checkoutframe.grid_forget()
#     cakeframe.grid_rowconfigure((0,1,2,3),weight=1)
#     cakeframe.grid_columnconfigure((0,1),weight=1)
#     cakeframe.grid(row=1,column=0,sticky='news')
#     cakeimage = [cake1,cake2,cake3]
#     for i,cake in enumerate(cakemenu) :
#         Label(cakeframe,bg='#FFDBF3',text=f'{cake}Price :{price1[i]}',image=cakeimage[i],compound='left').grid(row=i,column=0,sticky=N)
#         Entry(cakeframe,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=cakespy[i]).grid(row=i,column=0,sticky='SE')

# def drinkbottonclick():
#     checkoutframebottom.grid_forget()
#     checkoutframe.grid_forget()
#     drinkframe.grid_rowconfigure((0,1,2,3),weight=1)
#     drinkframe.grid_columnconfigure((0,1),weight=1)
#     drinkframe.grid(row=1,column=1,sticky='news')
#     cakeimage = [drink1,drink2,drink3]
#     for i,drink in enumerate(drinkmenu) :
#         Label(drinkframe,bg='#A5F9FF',text=f'{drink}Price :{price2[i]}',image=cakeimage[i],compound='left').grid(row=i,column=0)
#         Entry(drinkframe,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=drinkspy[i]).grid(row=i,column=0,sticky='SE')
# def coffeebottonclick():
#     checkoutframebottom.grid_forget()
#     checkoutframe.grid_forget()
#     coffeeframe.grid_rowconfigure((0,1,2,3),weight=1)
#     coffeeframe.grid_columnconfigure((0,1),weight=1)
#     coffeeframe.grid(row=1,column=2,sticky='news')
#     cakeimage = [coffee1,coffee2,coffee3]
#     for i,coffee in enumerate(coffeemenu) :
#         Label(coffeeframe,bg='#D6B79E',text=f'{coffee}Price :{price3[i]}',image=cakeimage[i],compound='left').grid(row=i,column=0,)
#         Entry(coffeeframe,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=coffeespy[i]).grid(row=i,column=0,sticky='SE')
