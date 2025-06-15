from tkinter import *
# import tkinter
# import tkinter as tk 

def mainwindow() :
    master = Tk()
    master.wm_geometry("1000x800")
    master.wm_title("Week2 : Introduction to GUI y Natchanon Saileamonpiwat")
    master.configure(bg="#006BFF") #config window backgroud color
    master.option_add('*font','Poppins 16') #config font 
    #config row and column for place window widget 
    master.grid_rowconfigure((0,3) , weight=1)
    master.grid_rowconfigure((1,2)  , weight=1)
    master.grid_columnconfigure((0,1),weight=1)
    return(master)   #return  master window
def widget(master) : 
    # Registration Form
    heading = Label(master,text=" Registration Form ",font=('Comic Sans MS',22,'bold'),bg="#006BFF",fg='#FBFBFB')
    heading.grid(row=0,columnspan=2)

    # Information
    namelabel = Label(master,text="Name : ",bg="#006BFF")
    namelabel.grid(row=1,column=0,sticky=E,pady=30)
    namebox = Entry(master,width=20)
    namebox.grid(row=1,column=1,sticky=W,ipady=5,pady=30)

    idlabel = Label(master,text="Student ID : ",bg="#006BFF")
    idlabel.grid(row=1,column=0,sticky=E,pady=100)
    idbox = Entry(master,width=20)
    idbox.grid(row=1,column=1,sticky=W,ipady=20,pady=100)

    # dpmlabel = Label(master,text="Department : ",bg="#006BFF")
    # dpmlabel.grid(row=1,column=0,sticky=E)
    # dpmbox = Entry(master,width=20)
    # dpmbox.grid(row=1 , column=1,sticky=W,ipady=5)

    # sqlabel = Label(master,text="Security Question : ",bg="#006BFF")
    # sqlabel.grid(row=1,column=0,sticky=E)
    # sqbox = Entry(master,width=20)
    # sqbox.grid(row=1 , column=1,sticky=W,ipady=5)

    # Button
    btn1 = Button(master,text="Cancel",width=10)
    btn1.grid(row=2 , column=0,ipady=15,sticky=NE, padx=5)
    
    btn2 = Button(master,text="Login",width=10)
    btn2.grid(row=2 , column=1,ipady=15,sticky=NW ,padx=5)

    # Created
    lower = Label(master,text="Created By Natchanon Saileamonpiwat ,ID = 1670700044 ",font=('Comic Sans MS',12,'bold'),bg="#006BFF",fg='#FBFBFB')
    lower.grid(row=3,columnspan=2,ipady=10)
master = mainwindow()
widget(master)
master.mainloop()