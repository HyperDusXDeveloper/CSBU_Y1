from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def createwindow():
    master = Tk()
    master.geometry('1300x800')
    master.option_add("*font", "tahoma 14")
    master.title("CS311 by natchanon Saileamonpiwat,student ID 1670700044")
    master.configure(bg='light pink')
    master.grid_rowconfigure(0,weight=1)
    master.grid_columnconfigure(0,weight=1)
    master.grid_columnconfigure(1,weight=5)
    master.grid_columnconfigure(2,weight=1)
    return (master)

def layout(mater) :
    #left
    left.grid_rowconfigure((0,1,2),weight=1)
    left.grid_columnconfigure((0),weight=1)
    left.grid(row=0,column=0,sticky='news')
    Button(left,text='Rose',compound='bottom',image=flower5,command=roseclick).grid(row=0,column=0,sticky='news')
    Button(left,text='lily',compound='bottom',image=flower1,command=lilyclick).grid(row=1,column=0,sticky='news')
    Button(left,text='Orchid',compound='bottom',image=flower3,command=orchidclick).grid(row=2 , column=0,sticky='news')
    
    center.grid_rowconfigure((0),weight=1)
    center.grid_columnconfigure((0),weight=1)
    center.grid(row=0,column=1,sticky='news')

    right.grid_rowconfigure((0,1),weight=1)
    right.grid_columnconfigure((0),weight=1)
    right.grid(row=0,column=2,sticky='news')
    Button(right,text='Oder Now',compound='top').grid(row=0,column=0,sticky='news')
    Button(right,text='Check Out',compound='top',command=checkoutclick).grid(row=1,column=0,sticky='news')

def roseclick() :
    checkoutframe.grid_forget()
    orchidframe.grid_forget()
    lilyframe.grid_forget()
    roseframe.grid(row=0,column=1,sticky='news')
    roseframe.grid_columnconfigure((0,1),weight=1)
    roseframe.grid_rowconfigure((0,1,2),weight=1)
    roseimage = [flower6,flower6]
    Label(roseframe,bg='#FDDEDA',text="Rose Flower",font=('tahoma',32),fg='#E9687B').grid(row=0,column=0,columnspan=2,sticky='N',pady=40)
    for i,rose in enumerate(rosemenu) :
        Label(roseframe,bg='#FDDEDA',image=roseimage[i],compound='right').grid(row=i,column=0,sticky=SE,pady=50,padx=50)
        Checkbutton(roseframe,bg='#FDDEDA',font=('tahoma',16,'bold'),text=f'                   {rosemenu[i]} Price : {roseprice[i]}',variable=rosespy[i]).grid(row=i,column=1,sticky=W,pady=30)

def lilyclick() :
    checkoutframe.grid_forget()
    orchidframe.grid_forget()
    roseframe.grid_forget()
    lilyframe.grid(row=0,column=1,sticky='news')
    lilyframe.grid_columnconfigure((0,1),weight=1)
    lilyframe.grid_rowconfigure((0,1,2),weight=1)
    lilyimage = [flower2,flower2]
    Label(lilyframe,bg='#FDDEDA',text="Lily Flower",font=('tahoma',32),fg='#E9687B').grid(row=0,column=0,columnspan=2,sticky='N',pady=40)
    for i,rose in enumerate(rosemenu) :
        Label(lilyframe,bg='#FDDEDA',image=lilyimage[i],compound='right').grid(row=i,column=0,sticky=SE,pady=50,padx=50)
        Checkbutton(lilyframe,bg='#FDDEDA',font=('tahoma',16,'bold'),text=f'                   {lilymenu[i]} Price : {lilyprice[i]}',variable=lilyspy[i]).grid(row=i,column=1,sticky=W)

def orchidclick() :
    checkoutframe.grid_forget()
    lilyframe.grid_forget()
    roseframe.grid_forget()
    orchidframe.grid(row=0,column=1,sticky='news')
    orchidframe.grid_columnconfigure((0,1),weight=1)
    orchidframe.grid_rowconfigure((0,1,2),weight=1)
    orchidimage = [flower4,flower4]
    Label(orchidframe,bg='#FDDEDA',text="Orchid Flower",font=('tahoma',32),fg='#E9687B').grid(row=0,column=0,columnspan=2,sticky='N',pady=40)
    for i,rose in enumerate(rosemenu) :
        Label(orchidframe,bg='#FDDEDA',image=orchidimage[i],compound='right').grid(row=i,column=0,sticky=SE,pady=50,padx=50)
        Checkbutton(orchidframe,bg='#FDDEDA',font=('tahoma',16,'bold'),text=f'                   {orchidmenu[i]} Price : {orchidprice[i]}',variable=orchidspy[i]).grid(row=i,column=1,sticky=W)

def checkoutclick():
    orchidframe.grid_forget()
    lilyframe.grid_forget()
    roseframe.grid_forget()
    global sumrose,sumlily,sumcorchid
    sumrose,sumlily,sumorchid = 0,0,0
    checkoutframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    checkoutframe.grid_columnconfigure((0),weight=1)
    checkoutframe.grid(row=0,column=1,sticky='news')
    for i,cake in enumerate(roseprice) :
        sumrose += rosespy[i].get() * roseprice[i]
        sumlily += lilyspy[i].get() * lilyprice[i]
        sumorchid += orchidspy[i].get() * orchidprice[i]
    total = sumrose + sumlily + sumorchid
    net = (total*7)/100 + total
    Label(checkoutframe,text='Flower 4U Shop : Receipt',font=('comic sans ms',30,'bold'),bg='#FDDEDA',fg='red').grid(row=0,columnspan=2)
    Label(checkoutframe,text=f'Total Rose Flower = {sumrose:,.2f}',bg='#FDDEDA',font=('tahoma',16),fg='#A65872').grid(row=1,sticky='news',columnspan=2)
    Label(checkoutframe,text=f'Total Lily Flower = {sumlily:,.2f}',bg='#FDDEDA',font=('tahoma',16),fg='#A65872').grid(row=2,sticky='news',columnspan=2)
    Label(checkoutframe,text=f'Total Orchid Flower = {sumorchid:,.2f}',bg='#FDDEDA',font=('tahoma',16),fg='#A65872').grid(row=3,sticky='news',columnspan=2)
    Label(checkoutframe,text=f'Net Total (include Vat ) = {net:,.2f}',font=('comic sans ms',25,'bold'),bg='#E9687B',fg='#B53359').grid(row=5,sticky='news',columnspan=2)

    
master = createwindow()
flower1 = PhotoImage(file='Midturm/imagem4/lily.png').subsample(2,2)
flower2 = PhotoImage(file='Midturm/imagem4/lily1.png').subsample(10,10)
flower3 = PhotoImage(file='Midturm/imagem4/orchid.png').subsample(2,2)
flower4 = PhotoImage(file='Midturm/imagem4/orchid1.png').subsample(5,5)
flower5 = PhotoImage(file='Midturm/imagem4/rose.png').subsample(2,2)
flower6 = PhotoImage(file='Midturm/imagem4/rose1.png').subsample(2,2)
left = Frame(master,bg='#AB886D')
center = Frame(master,bg='#FDDEDA')
roseframe  = Frame(master,bg='#FDDEDA')
lilyframe  = Frame(master,bg='#FDDEDA')
orchidframe  = Frame(master,bg='#FDDEDA')
checkoutframe  = Frame(master,bg='#FDDEDA')
right = Frame(master,bg='white')
rosemenu = ['Rose1','Rose2']
lilymenu = ['Lily1','Lily2']
orchidmenu = ['Orchid1','Orchid2']
roseprice = [550,650]
lilyprice = [600,700]
orchidprice = [400,500]
rosespy = [IntVar() for x in roseprice]
lilyspy = [IntVar() for x in lilyprice]
orchidspy = [IntVar() for x in orchidprice]
layout(master)
master.mainloop()