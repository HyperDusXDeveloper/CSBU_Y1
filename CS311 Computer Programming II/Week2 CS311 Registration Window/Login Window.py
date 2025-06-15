from tkinter import *
# import tkinter
# import tkinter as tk 

def mainwindow() :
    master = Tk()
    master.wm_geometry("1000x800+300+100")
    master.wm_title("Week2 : Created By Natchanon Saileamonpiwat")
    master.configure(bg="#006BFF") #config window backgroud color
    master.option_add('*font','Poppins 16') #config font 
    #config row and column for place window widget 
    master.grid_rowconfigure((0,3) , weight=4)
    master.grid_rowconfigure((1,2)  , weight=1)
    master.grid_columnconfigure((0,1),weight=1)
    return(master)   #return  master window
def widget(master) : 
    heading = Label(master,text="Login Window",font=('Poppins',22,'bold'),bg="#006BFF",fg='#FBFBFB')
    heading.grid(row=0,columnspan=2)
    userlabel = Label(master,text="Username : ",bg="#006BFF")
    userlabel.grid(row=1,column=0,sticky=E)
    pwdlabel = Label(master,text="Password : ",bg="#006BFF")
    pwdlabel.grid(row=2,column=0,sticky=E)
    userbox = Entry(master,width=20)
    userbox.grid(row=1,column=1,sticky=W,ipady=5)
    pwdbox = Entry(master,width=20,show="*")
    pwdbox.grid(row=2 , column=1,sticky=W,ipady=5)
    btn1 = Button(master,text="Cancel",width=20)
    btn1.grid(row=3 , column=0,ipady=15,sticky=NE, padx=5)
    btn2 = Button(master,text="Login",width=20)
    btn2.grid(row=3 , column=1,ipady=15,sticky=NW ,padx=5)

master = mainwindow()
widget(master)
master.mainloop()