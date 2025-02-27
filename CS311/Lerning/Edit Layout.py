from tkinter import *
from tkinter import ttk

def createwindow():
    master = Tk()
    master.geometry('800x700+300+100')
    master.option_add("*font", "tahoma 14")
    master.title("Homework Week6 : Sweet Home Cafe'Application by Natchanon Saileamonpiwat")
    master.configure(bg='light pink')
    master.grid_rowconfigure(0,weight=1)
    master.grid_rowconfigure(1,weight=4)
    master.grid_rowconfigure(2,weight=1)
    master.grid_columnconfigure(0,weight=1)
    master.grid_columnconfigure(1,weight=5)
    return (master)

def layout(mater) :
    #Left 
    left.grid_rowconfigure((0,1),weight=1)
    left.grid_columnconfigure((0),weight=1)
    left.grid(column=0,rowspan=3,sticky='news')

    bottom.grid_rowconfigure((1),weight=1)
    bottom.grid_columnconfigure((0),weight=1)
    bottom.grid(columnspan=2,rowspan=3,sticky='news')


def leftframe(left,bottom) :
    #Show Button .grid
    Button(left,text='Product Menu',image=icon1,compound='top',command=productmenu).grid(row=0 , columnspan=2,sticky='news')
    Button(left,text='Checkout',image=icon2,compound='top',command=checkoutclick).grid(row=1 , columnspan=2,sticky='news')
    Button(bottom,text='Close Program',image=icon5,compound='left',command=exit).grid(rowspan=3 , column=0,sticky='news')

def productmenu() :
    checkoutframe.grid_forget()
    pmenu.grid_columnconfigure((0,1,2),weight=1)
    pmenu.grid_rowconfigure((0,1,2),weight=1)
    pmenu.grid(row=0 , rowspan=3,column=1,sticky='news')
    
    #Cake left
    cakeimage = [cake1,cake2,cake3]
    for i,cake in enumerate(cakemenu) :
        Label(pmenu, bg='#C6E7FF', image=cakeimage[i], compound='right', text=f'{cake}\n Price : {price1[i]}').grid(row=i , column=1,sticky='news')
        Spinbox(pmenu, from_=0, to=200, width=10, textvariable=cakespy[i]).grid(row=i, column=1 , sticky='s',pady=15)

    # Drink Right
    drinkimage = [drink1,drink2,drink3]
    for i,drink in enumerate(drinkmenu) :
        Label(pmenu,bg='#C6E7FF',image=drinkimage[i],compound='right',text=f'{drink}\n Price : {price2[i]}').grid(row=i ,column=2)
        Spinbox(pmenu,from_=0,to=200,width=10,textvariable=drinkspy[i]).grid(row=i,column=2,sticky='s',pady=15)

def checkoutclick() :
    global sumcake,sumdrink
    sumcake,sumdrink = 0,0

    pmenu.grid_forget()

    checkoutframe.grid_columnconfigure(0,weight=1)
    checkoutframe.grid_rowconfigure((0,3),weight=2)
    checkoutframe.grid_rowconfigure((1,2),weight=1)
    checkoutframe.grid(row=0,rowspan=3,column=1,sticky='news')

    for i,productm in enumerate(price1) :
        #Cake / Drink " Price "
        sumcake += cakespy[i].get() * price1[i]
        sumdrink += drinkspy[i].get() * price2[i]

    #Total Cake + Drink "Price"
    total = sumcake + sumdrink

    #Print Output
    Label(checkoutframe,text='~ Summary of Cake/Drink Menu ~',font=('comic sans ms',20,'bold'),fg='blue',bg='#EBC7E6').grid(row=0)
    Label(checkoutframe,text=f'Total cake price = {sumcake:,.2f}',bg='#FFB38E').grid(row=1,sticky='news')
    Label(checkoutframe,text=f'Total drink price = {sumdrink:,.2f}',bg='#C6E7FF').grid(row=2,sticky='news')
    Label(checkoutframe,text=f'Total price of your order =  {total:,.2f} Baht',font=('comic sans ms',20,'bold'),fg='blue',bg='#EBC7E6').grid(row=3)

#Master Loop
master = createwindow()

#IMG ICON
drink1 = PhotoImage(file="Week6 CS311/image/drink1.png")
drink2 = PhotoImage(file="Week6 CS311/image/drink2.png")
drink3 = PhotoImage(file='Week6 CS311/image/drink3.png')
cake1 = PhotoImage(file="Week6 CS311/image/cake1.png")
cake2 = PhotoImage(file="Week6 CS311/image/cake2.png")
cake3 = PhotoImage(file="Week6 CS311/image/cake3.png")
icon1 = PhotoImage(file='Week6 CS311/image/cake-button.png')
icon2 = PhotoImage(file='Week6 CS311/image/drink-button.png')
icon3 = PhotoImage(file="Week6 CS311/image/checkout.png")
icon4 = PhotoImage(file="Week6 CS311/image/cancel.png")
icon5 = PhotoImage(file="Week6 CS311/image/exit.png")

#Information Cake / Drink
cakemenu = [' Strawberry Cake \n'," Cheese  Cake  \n","Newyork Cheese Cake\n"]
drinkmenu = ['| Orange  Mixed |\n',' Lemonade Mixed \n',"| Mojito  Miexd  Berry |\n"]
price1 = [145,120,130]
price2 = [120,100,90]

# Spy Cake / Drink
cakespy = [IntVar() for x in price1]
drinkspy = [IntVar() for x in price2]

left = Frame(master,bg='#FBFBFB')
bottom = Frame(master,bg='#FFDDAE')
pmenu = Frame(master,bg='#D4F6FF')
dleft = Frame(master,bg='#FFECC8')
pmenu = Frame(master,bg='#C6E7FF')
dright = Frame(master,bg='#FFD09B')
checkoutframe = Frame(master,bg='#EBC7E6')

layout(master)
leftframe(left,bottom)
master.mainloop()