from tkinter import *
from tkinter import messagebox

def createwindow() :
    master = Tk()
    master.wm_geometry('1000x700+300+50')
    master.title("Homework of Week4 : Figure Shop by Natchanon Saileamonpiwat ")
    master.option_add('*font',"Arital 20")
    master.grid_rowconfigure(0,weight=2)
    master.grid_rowconfigure(1,weight=5)
    master.grid_rowconfigure(2,weight=1)
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
    right.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    right.grid_columnconfigure((0,1,2),weight=1)
    
    bottom = Frame(master,bg='#E5989B')
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(top,left,right,bottom)

def widgets(top,left,right,bottom) :

    #Top
    exit = Button(top,image=icon2,text='EXIT PROGRAM',font=('Arial',12,'bold'),bd=3,command=quit,compound='left')
    exit.pack(side='right',padx=150,pady=5,ipadx=20,ipady=1)
    clickme = Button(top,image=icon1,text='CLICK ME',font=('Arial',12,'bold'),bd=3,compound='left',command=clickmepopup)
    clickme.pack(side='left',padx=150,pady=5,ipadx=300,ipady=1)

    #Left
    product1 = Label(left,bg='#FCE7C8',image=fig1)
    product1.grid(row=0,rowspan=2,column=0,sticky=E,padx=40)
    product2 = Label(left,bg='#FCE7C8',image=fig2)
    product2.grid(row=2,rowspan=2,column=0,sticky=E,padx=40)
    product3 = Label(left,bg='#FCE7C8',image=fig3)
    product3.grid(row=4,rowspan=2,column=0,sticky=E)

    #Right
    amount1 = Checkbutton(right,text="Skullpanda Price = 380 baths",bg='#FFCDB2',fg='black',variable=spy1,font=('Arial',12,'bold'),command=userclick)
    amount1.grid(row=0,column=1,columnspan=2,rowspan=2,padx=160)
    amount2 = Checkbutton(right,text='Dimoo Price = 450 baths',bg='#FFCDB2',fg='black',variable=spy2,font=('Arial',12,'bold'),command=userclick)
    amount2.grid(row=2,column=1,columnspan=2,rowspan=2,padx=160)
    amount3 = Checkbutton(right,text="Crybaby Price = 350 baths",bg='#FFCDB2',fg='black',variable=spy3,font=('Arial',12,'bold'),command=userclick)
    amount3.grid(row=4,column=1,columnspan=2,rowspan=2,padx=160)
    #Bottom
    total = Label(bottom,text="Total = 0.00 Baht",font=('Arial',28,'bold'),fg='#E5989B',bg='#E5989B')
    total.pack(pady=10,anchor=N)
    return(total,amount1,amount2,amount3)

def clickmepopup():
    messagebox.showinfo("Welcome to Art Toy Shop by Popmart Official Store", ' 1. Skullpanda\n 2. Dimoo\n 3. Crybaby')

def userclick() :
    total['bg'] = '#FFBDBD'
    total['fg'] = 'blue'
    net = spy1.get()*380 + spy2.get()*450 + spy3.get()*350
    total['text'] = f"Total = {net:0.2f} Bath"

#main
master = createwindow()
icon2 = PhotoImage(file="Week4_CS311/image/icon2.png")
icon1 = PhotoImage(file="Week4_CS311/image/icon1.png")
fig1 = PhotoImage(file="Week4_CS311/image/fig1.png").subsample(4,4)
fig2 = PhotoImage(file='Week4_CS311/image/fig2.png').subsample(4,4)
fig3 = PhotoImage(file="Week4_CS311/image/fig3.png").subsample(3,3)
spy1,spy2,spy3  = IntVar(),IntVar(),IntVar()
net = 0
top,left,right,bottom = framelayout(master)
total,amount1,amount2,amount3 = widgets(top,left,right,bottom)
master.mainloop()