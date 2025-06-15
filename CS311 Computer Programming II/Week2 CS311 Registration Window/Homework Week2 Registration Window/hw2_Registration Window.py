from tkinter import *

def mainwindow() :
    master = Tk()
    master.wm_geometry("1000x800")
    master.wm_title("Week2 : Introduction to GUI by Natchanon Saileamonpiwat")
    master.configure(bg="#006BFF") 
    master.option_add('*font','Poppins 16')
    master.grid_rowconfigure((0,6) , weight=4)
    master.grid_rowconfigure((1,4)  , weight=1)
    master.grid_rowconfigure((2,3)  , weight=1)
    master.grid_columnconfigure((0,1),weight=1)
    return(master) 

def widget(master) : 
    # Registration Form
    heading = Label(master,text=" Registration Form ",font=('Comic Sans MS',22,'bold'),bg="#006BFF",fg='#FBFBFB')
    heading.grid(row=0,columnspan=2)

    # Information
    namelabel = Label(master,text="Name : ",bg="#006BFF")
    namelabel.grid(row=1,column=0,sticky=E)
    namebox = Entry(master,width=20)
    namebox.grid(row=1,column=1,sticky=W,ipady=5)

    idlabel = Label(master,text="Student ID : ",bg="#006BFF")
    idlabel.grid(row=2,column=0,sticky=E)
    idbox = Entry(master,width=20)
    idbox.grid(row=2,column=1,sticky=W,ipady=5)

    dpmlabel = Label(master,text="Department : ",bg="#006BFF")
    dpmlabel.grid(row=3,column=0,sticky=E)
    dpmbox = Entry(master,width=20)
    dpmbox.grid(row=3 , column=1,sticky=W,ipady=5)

    sqlabel = Label(master,text="Security Question : ",bg="#006BFF")
    sqlabel.grid(row=4,column=0,sticky=E)
    sqbox = Entry(master,width=20)
    sqbox.grid(row=4 , column=1,sticky=W,ipady=5)

    # Button
    btn1 = Button(master,text="CANCEL",width=10)
    btn1.grid(row=5 , column=0,ipady=20,sticky=NE, padx=10)
    
    btn2 = Button(master,text="REGISTER",width=10)
    btn2.grid(row=5 , column=1,ipady=20,sticky=NW ,padx=10)

    # Created
    lower = Label(master,text="Created By Natchanon Saileamonpiwat ,ID = 1670700044 ",font=('Comic Sans MS',12,'bold'),bg="#006BFF",fg='#EFB036')
    lower.grid(row=6,columnspan=2,ipady=10)
    
master = mainwindow()
widget(master)
master.mainloop()