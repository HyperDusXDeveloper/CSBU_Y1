from tkinter import *
from tkinter import messagebox

def createwindow() :
    master = Tk()
    master.wm_geometry('1000x700+300+50')
    master.title("Week4 : Dream Bekery Shop by Natchanon Saileamonpiwat")
    master.option_add('*font',"Garamond 20")
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=5)
    master.grid_columnconfigure((0,1),weight=1)
    return(master)

def framelayout(master) :
    top = Frame(master,bg='#E5989B')
    top.grid(row=0,columnspan=2,sticky='news')
    left = Frame(master,bg='#FCE7C8')
    left.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    left.grid_columnconfigure((0,1),weight=1)
    left.grid(row=1,column=0,sticky='news')
    right = Frame(master,bg='#FFCDB2')
    right.grid(row=1,column=1,sticky='news')
    bottom = Frame(master,bg='#E5989B')
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(top,left,right,bottom)

def widgets(top,left,right,bottom) :
    heading = Label(top,text="Dream Bekery Shop by Natchanon Saileamonpiwat",fg='blue',font=('comic sans ms',32,'bold'),bg='#E5989B')
    heading.pack(pady=15)
    product1 = Label(left,bg='#FCE7C8',image=cake1)
    product1.grid(row=0,rowspan=2,column=0,sticky=E)
    detail1 = Label(left,text='Chocolate Cake\nPrice 160 Baht',bg='#FCE7C8')
    detail1.grid(row=0,column=1,sticky=S)
    amount1 = Checkbutton(left,text='Price : 160 B',bg='#FCE7C8',fg='#3674B5',variable=spy1,command=userclick)
    amount1.grid(row=1,column=1,sticky=N)
    product2 = Label(left,bg='#FCE7C8',image=cake2)
    product2.grid(row=2,rowspan=2,column=0,sticky=E)
    detail2 = Label(left,text='Strawberry Cake\nPrice 140 Baht',bg='#FCE7C8')
    detail2.grid(row=2,column=1,sticky=S)
    amount2 = Checkbutton(left,text="Price : 140 B",bg='#FCE7C8',fg='#3674B5',variable=spy2,command=userclick)
    amount2.grid(row=3,column=1,sticky=N)
    product3 = Label(left,bg='#FCE7C8',image=cake3)
    product3.grid(row=4,rowspan=2,column=0,sticky=E)
    detail3 = Label(left,text='Pony Donut\nPrice 75 Baht',bg='#FCE7C8')
    detail3.grid(row=4,column=1,sticky=S)
    amount3 = Checkbutton(left,text="Price : 75 B",bg='#FCE7C8',fg='#3674B5',variable=spy3,command=userclick)
    amount3.grid(row=5,column=1,sticky=N)
    summary = Label(right,text="Thank you for your shopping\nTotal Price is",font=('Garamond',32,'bold'),bg='#FFCDB2')
    summary.pack(pady=50,anchor=N)
    total = Label(right,text="Total = 0.00 Baht",font=('Garamond',32,'bold'),fg='blue',bg='#FFCDB2')
    total.pack(pady=50,anchor=N)
    btn1 = Button(bottom,text='Exit Program',command=quit)
    btn1.pack(side='right',padx=30,pady=10,ipadx=20,ipady=15)
    return(total)

def userclick() :
    net = spy1.get()*160 + spy2.get()*140 + spy3.get()*75
    total['text'] = f"Total = {net:0.2f} Bath"
#main
master = createwindow()
cake1 = PhotoImage(file="image/cake1.png")
cake2 = PhotoImage(file='image/cake2.png')
cake3 = PhotoImage(file="image/cake3.png")
spy1,spy2,spy3  = IntVar(),IntVar(),IntVar()
net = 0
top,left,right,bottom = framelayout(master)
total = widgets(top,left,right,bottom)
master.mainloop()