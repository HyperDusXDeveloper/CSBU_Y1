from tkinter import *
from tkinter import messagebox
def createwindow() :
    master = Tk()
    master.wm_geometry('1000x800+300+100')
    master.title('Art toy shop created by Natchanon Srileamonpiwat')
    master.grid_columnconfigure((0,1),weight=1)
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=5)
    master.option_add('*font','Garamond 20')
    return(master)
 
def layout(master) :
    top = Frame(master,bg="#FFFBCA")
    top.grid(row=0,columnspan=2,sticky='news')
    left = Frame(master,bg="white")
    left.grid_rowconfigure((0,1,2),weight=1)
    left.grid_columnconfigure(0,weight=1)
    left.grid(row=1,column=0,sticky='news')
    right = Frame(master,bg="#FEF9F2")
    right.rowconfigure((0,1,2),weight=1)
    right.grid_columnconfigure(0,weight=1)
    right.grid(row=1,column=1,sticky='news')
    bottom = Frame(master,bg="#C5BAFF")
    bottom.columnconfigure((0,1),weight=1)
    bottom.rowconfigure(0,weight=1)
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(top,left,right,bottom)
 
def widgets(top,left,right,bottom) :
    heading = Label(top,text="Art Toy by Popmart Official Store",fg='#2A004E',font=('comic sans ms',24,'bold'),bg="#FFFBCA")
    heading.pack(pady=15)
    figure1 = Label(left,image=toy1,bg="white")
    figure1.grid(row=0)
    figure2 = Label(left,image=toy2,bg="white")
    figure2.grid(row=1)
    figure3 = Label(left,image=toy3,bg="white")
    figure3.grid(row=2)
    order1 = Button(right,text='Select Figure1',image=icon,compound=LEFT,command=order1click)
    order1.grid(row=0,ipadx=15)
    order2 = Button(right,text='Select Figure2',image=icon,compound=LEFT,command=order2click)
    order2.grid(row=1,ipadx=15)
    order3 = Button(right,text='Select Figure3',image=icon,compound=LEFT,command=order3click)
    order3.grid(row=2,ipadx=15)
    btn1 = Button(bottom,text="Order Now",width=15)
    btn1.grid(row=0,column=0,sticky=E,padx=10,ipadx=20,ipady=10,pady=15)
    btn2 = Button(bottom,text="Exit Program",width=15,command=exit)
    btn2.grid(row=0,column=1,sticky=W,padx=10,ipadx=20,ipady=10)

def order1click() :
    messagebox.showinfo("Admin : ", "You order skullpanda ")
def order2click() :
    messagebox.showinfo("Admin : ", "You order dimoo ")
def order3click() :
    messagebox.showinfo("Admin : ", "You order crybaby ")


#main
master = createwindow()
toy1 = PhotoImage(file="image/skullpanda.png").subsample(3,3)
toy2 = PhotoImage(file='image/dimoo.png').subsample(3,3)
toy3 = PhotoImage(file='image/crybaby.png').subsample(2,2)
icon = PhotoImage(file='image/icon1.png')
top,left,right,bottom = layout(master)
widgets(top,left,right,bottom)
master.mainloop()