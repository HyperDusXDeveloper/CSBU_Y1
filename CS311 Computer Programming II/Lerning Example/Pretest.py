from tkinter import * 
from tkinter import ttk


def createwindow():
    master = Tk()
    master.geometry('1000x700')
    master.option_add("*font", "tahoma 14")
    master.title("Homework Week6 : Sweet Home Cafe'Application by Natchanon Saileamonpiwat")
    master.configure(bg='light pink')
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=3)
    master.grid_columnconfigure((0,2),weight=1)
    master.grid_columnconfigure(1,weight=3)
    return (master)

def layout(mater) :

    #TOP
    tl.grid_rowconfigure((0),weight=1)
    tl.grid_columnconfigure((0,1),weight=1)
    tl.grid(row=0,column=0 ,sticky='news')

    tc.grid_rowconfigure((0,1),weight=1)
    tc.grid_columnconfigure((0,1),weight=1)
    tc.grid(row=0,column=1 ,sticky='news')

    tr.grid_rowconfigure((0),weight=1)
    tr.grid_columnconfigure(0,weight=1)
    tr.grid(row=0,column=2 ,sticky='news')

    #Center
    cl.grid_rowconfigure((0),weight=1)
    cl.grid_columnconfigure(0,weight=1)
    cl.grid(row=1,column=0 ,sticky='news')

    cc.grid_rowconfigure((0),weight=1)
    cc.grid_columnconfigure((0,1),weight=1)
    cc.grid(row=1,column=1 ,sticky='news')

    cr.grid_rowconfigure((0),weight=1)
    cr.grid_columnconfigure(0,weight=1)
    cr.grid(row=1,column=2 ,sticky='news')


    #Bottom
    bl.grid_rowconfigure((0),weight=1)
    bl.grid_columnconfigure(0,weight=1)
    bl.grid(row=2,column=0 ,sticky='news')

    bc.grid_rowconfigure((0),weight=1)
    bc.grid_columnconfigure(0,weight=1)
    bc.grid(row=2,column=1 ,sticky='news')

    br.grid_rowconfigure((0),weight=1)
    br.grid_columnconfigure(0,weight=1)
    br.grid(row=2,column=2 ,sticky='news')

def widget(tl,cl,bl,tc,cc,tr,br):

    Button(tl,text='Drink Menu',font=('tahomas',15),image=img3,compound=TOP).grid(row=0 , column=0,sticky='news')
    Button(tl,text='Cake Menu',font=('tahoma',15),image=img4,compound=TOP).grid(row=0 , column=1,sticky='news')

    Label(cl,text="Dream\nCake",font=('tahoma',40),bg='#6ED6A9').grid(row=0 , column=0,sticky='news')

    Label(bl,text="Shop",font=('tahoma',40),bg='#6ED6A9',image=img2,compound=LEFT).grid(row=0 , column=0,sticky='news')

    Label(tc,image=img5,bg='#FFBABA').grid(rowspan=2 , columnspan=2,sticky='news')

    Label(cc,image=img6,bg='#FFF7B7').grid(row=0 , column=0,sticky='news',pady=120,padx=80)
    Label(cc,image=img7,bg='#FFF7B7').grid(row=0 , column=1,sticky='news',pady=120,padx=80)

    Button(tr,text='CheckOut',font=('tahomas',25),image=img8,compound='right').grid(row=0 , column=0,sticky='news')
    Button(br,text='EXIT',font=('tahomas',25),image=img9,compound='right').grid(row=0 , column=0,sticky='news')
master = createwindow()
#TOP
tl = Frame(master,bg='#FFBABA')
tc = Frame(master,bg='#FFBABA')
tr = Frame(master,bg='#FFBABA')

#CENTER
cl = Frame(master,bg='#6ED6A9')
cc = Frame(master,bg='#FFF7B7')
cr = Frame(master,bg='#6ED6A9')

#BOTTOM
bl = Frame(master,bg='#6ED6A9')
bc = Frame(master,bg='#FFBABA')
br = Frame(master,bg='#FFBABA')

img1 = PhotoImage(file='Lerning/image/cake-button.png')
img2 = PhotoImage(file='Lerning/image/myshop.png').subsample(5,5)
img3 = PhotoImage(file='Lerning/image/drink-button.png')
img4 = PhotoImage(file='Lerning/image/cake33.png').subsample(2,2)
img5 = PhotoImage(file='Lerning/image/cancel.png').subsample(2,2)
img6 = PhotoImage(file='Lerning/image/cake1.png')
img7 = PhotoImage(file='Lerning/image/drink1.png')
img8 = PhotoImage(file='Lerning/image/checkout.png')
img9 = PhotoImage(file='Lerning/image/exit.png')

layout(master)
widget(tl,cl,bl,tc,cc,tr,br)
master.mainloop()