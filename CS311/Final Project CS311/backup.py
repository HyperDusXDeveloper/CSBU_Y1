import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def connection() :
    global conn,cursor
    conn = sqlite3.connect("database/Nonshop.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1400
    h = 900
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#ffffff')
    root.title("Week14 Insert/Update/Delete Application: ")
    root.option_add('*font',"Helvetica 18 bold")
    root.rowconfigure((0,1),weight=2)
    root.rowconfigure((2,3),weight=2)
    root.columnconfigure((0,1),weight=2)
    root.columnconfigure((2,3),weight=2)
    return root

def introshop():
    introframe.rowconfigure((0,1,2),weight=1)
    introframe.columnconfigure((0),weight=1)
    introframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    Label(introframe,image=nonlogo,bg='#ffffff').grid(row=0,column=0,sticky=S)
    Button(introframe,text="WELCOME",width=10,command=welcomelayout,bg='#0066FF',fg='#ffffff',font="Helvetica 25 ").grid(row=1,column=0,sticky=N)
    

def welcomelayout() :
    introframe.grid_forget()
    registerframe.grid_forget()
    global user,pwd
    loginframe.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    loginframe.columnconfigure((0),weight=1)
    loginframe.grid(row=0,column=2,columnspan=2,rowspan=4,sticky='news')

    loginframeimg.rowconfigure((0),weight=1)
    loginframeimg.columnconfigure((0),weight=1)
    loginframeimg.grid(row=0,column=0,rowspan=6,sticky=W)

    Label(loginframeimg,image=ATCimage).grid(row=0,column=0,rowspan=6,sticky=W)

    Label(loginframe,image=usericon,compound=LEFT,bg='#ffffff',fg='#0066FF',text="LOGIN PAGE",font="Helvetica 50 ").grid(row=2,column=0,sticky=SW,pady=20,padx=80)
    Label(loginframe,text="Username or Email",bg='#ffffff',fg='#000000',padx=20,font="Helvetica 30 ").grid(row=3,column=0,sticky=NW,padx=60)
    user = Entry(loginframe,bg='#ffffff',width=40)
    user.grid(row=3,column=0,sticky=SW,padx=80,pady=20)

    Label(loginframe,text="Password ",bg='#ffffff',fg='#000000',padx=20,font="Helvetica 30 ").grid(row=4,column=0,sticky=NW,padx=60)
    pwd = Entry(loginframe,bg='#ffffff',width=40,show='*')
    pwd.grid(row=4,column=0,sticky=SW,padx=80,pady=20)

    

    Button(loginframe,text="LOGIN",font="Helvetica 20 ",width=10,command=lambda:loginclick(user.get(),pwd.get()),bg='#0066FF',fg='#ffffff').grid(row=5,column=0,sticky=NW,padx=80)
    Button(loginframe,text="REGESTER",font="Helvetica 20 ",width=12,bg='#0066FF',fg='#ffffff',command=registerclick).grid(row=5,column=0,sticky=NW,padx=300)

def loginclick(user,pwd) :
    global result
    if user == "" or pwd == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        user.focus_force()
    else :
        sql = "select * from partner where username=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            sql = "select * from partner where username=? and password=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Admin : ","Login Successfully.")
                welcomepage(result)
            else :
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                pwd.selection_range(0,END)
                pwd.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            user.selection_range(0,END)
            user.focus_force()


def registerclick() :
    global fullname,username,year,gender,password,confirmpassword,point,wallet
    point = 0
    wallet = 0
    loginframe.grid_forget()
    loginframeimg.grid_forget()
    registerframe.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    registerframe.columnconfigure((0,1),weight=1)
    registerframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

    Label(registerframe,text="REGISTER",font="Helvetica 50 ",fg='#0066FF',image=usericon,compound=TOP,bg='#ffffff').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)

    Label(registerframe,text='Full name : ',bg='#ffffff',fg='#000000',font="Helvetica 20 ").grid(row=1,column=0,sticky='e',padx=10)
    fullname = Entry(registerframe,width=20,bg='#ffffff')
    fullname.grid(row=1,column=1,sticky='w',padx=10)

    Label(registerframe,text='Username : ',bg='#ffffff',fg='#000000',font="Helvetica 20 ").grid(row=2,column=0,sticky='e',padx=10)
    username = Entry(registerframe,width=20,bg='#ffffff')
    username.grid(row=2,column=1,sticky='w',padx=10)

    Label(registerframe,text="Year Birth : ",bg='#ffffff',fg='#000000',font="Helvetica 20 ").grid(row=3,column=0,sticky='e',padx=10)
    year = Entry(registerframe,width=20,bg='#ffffff')
    year.grid(row=3,column=1,sticky='w',padx=10)

    Label(registerframe,text="Gender : ",bg='#ffffff',fg='#000000',font="Helvetica 20 ").grid(row=4,column=0,sticky='e',padx=10)
    gender = Entry(registerframe,width=20,bg='#ffffff')
    gender.grid(row=4,column=1,sticky='w',padx=10)

    Label(registerframe,text="Password : ",bg='#ffffff',fg='#000000',font="Helvetica 20 ").grid(row=5,column=0,sticky='e',padx=10)
    password = Entry(registerframe,width=20,bg='#ffffff',show='*')
    password.grid(row=5,column=1,sticky='w',padx=10)

    Label(registerframe,text="Confirm Password : ",bg='#ffffff',fg='#000000',font="Helvetica 20 ").grid(row=6,column=0,sticky='e',padx=10)
    confirmpassword = Entry(registerframe,width=20,bg='#ffffff',show='*')
    confirmpassword.grid(row=6,column=1,sticky='w',padx=10)

    regisaction = Button(registerframe,text="Register Submit",command=registration,bg='#0066FF',fg='#ffffff')
    regisaction.grid(row=7,column=0,ipady=5,ipadx=5,pady=5,sticky='e')

    fullname.focus_force()
    loginbtn = Button(registerframe,text="Back to Login",command=welcomelayout,bg='#0066FF',fg='#ffffff')
    loginbtn.grid(row=7,column=1,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)

def registration() : 
    print("Hello from registration")
    if fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Fullname")
        fullname.focus_force()
    elif username.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Username")
        username.focus_force()
    elif year.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Year Birthday")
        year.focus_force()
    elif gender.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Gender")
        gender.focus_force()
    elif password.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Password")
        gender.focus_force()
    elif confirmpassword.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter a Confirm Password")
        password.focus_force()
    else :
        sql = "select * from partner where username=?"
        cursor.execute(sql,[username.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("Admin:","The username is already exists")
            username.select_range(0,END)
            username.focus_force()
        else :
            if password.get() == confirmpassword.get() :
                sql = "insert into partner values (?,?,?,?,?,?,?)"
                Nyear = year.get()
                NEWyear = 2025 - int(Nyear)
                userinformation = [fullname.get(),username.get(),NEWyear,gender.get(),password.get(),point,wallet]
                cursor.execute(sql,userinformation)
                conn.commit()
                checkinfomation()
                messagebox.showinfo("Admin:","Registration Successfully")
                year.delete(0,END)
                gender.delete(0,END)
                password.delete(0,END)
                confirmpassword.delete(0,END)
                fullname.delete(0,END)
                username.delete(0,END)
            else :
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                password.selection_range(0,END)
                password.focus_force()

def checkinfomation() :
    sql = "select * from partner"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)


def welcomepage(result) :
    global top,right,keyboardbutton,mousebutton
    loginframe.grid_forget()
    loginframeimg.grid_forget()
    pwdframe.grid_forget()
    updateframe.grid_forget()
    welcomeframe['bg'] = "#ffffff"
    
    #WELCOMEFRAME ROW
    welcomeframe.grid_rowconfigure((0),weight=1)
    welcomeframe.grid_rowconfigure((1),weight=3)
    welcomeframe.grid_rowconfigure((2),weight=2)

    #WELCOMEFRAME COLUMN
    welcomeframe.grid_columnconfigure((0),weight=1)
    welcomeframe.grid_columnconfigure((1),weight=6)

    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

    #TOP FRAME
    top = Frame(welcomeframe,bg='#ffffff', bd=2, relief="groove")
    top.grid_rowconfigure((0),weight=1)
    top.grid_columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    Label(top,text="NON's ELEVENSHOP",bg='#ffffff',fg='#0066FF',font="Helvetica 60 ").grid(row=0,column=0,pady=10,sticky=W,padx=20)
    # Label(top,image=nonlogo,bg='#fffffF').grid(row=0)

    #LEFT
    lefttop = Frame(welcomeframe,bg='#ffffff', bd=2, relief="groove")
    lefttop.grid_rowconfigure((0,1,2,3),weight=1)
    lefttop.grid_columnconfigure(0,weight=1)
    lefttop.grid(row=1,column=0,sticky='news')
    Label(lefttop,text='MENU',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,column=0,pady=3,sticky=N)
    mousebutton = Button(lefttop,text="MOUSE",width=20,command=mousecrick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    mousebutton.grid(row=1,ipady=5,sticky=N)
    keyboardbutton = Button(lefttop,text="KEYBOARD",width=20,command=keyboardcrick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    keyboardbutton.grid(row=2,ipady=5,sticky=N)
    Button(lefttop,text="HEADPHONE",width=20,command=headphonecrick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ").grid(row=3,ipady=5,sticky=N)


    leftbottom = Frame(welcomeframe,bg='#ffffff', bd=2, relief="groove")
    leftbottom.grid_rowconfigure((0,1,2,3),weight=1)
    leftbottom.grid_columnconfigure(0,weight=1)
    leftbottom.grid(row=2,column=0,sticky='news')
    Label(leftbottom,text='MYINFO',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,pady=10,sticky=S)
    Button(leftbottom,text="MY WALLET",width=15,command=mywalletlayout,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ").grid(row=1,ipady=10,sticky=N)
    Button(leftbottom,text="MY POINT",width=15,command=mypointlayout,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ").grid(row=2,ipady=10,sticky=N)
    
    #RIGHT

    right = Frame(welcomeframe,bg='#ffffff')
    right.grid_rowconfigure((0),weight=1)
    right.grid_columnconfigure(0,weight=1)
    right.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(right,image=shoping,bg='#fffffF',text="SHOPING",compound='top',fg='#0066FF',font="Helvetica 60 ").grid(row=0)
    #create widgets
    # Label(top2,image=usericon,bg='#ffffff',text="partner ID : "+str(result[0])+"\n"+"Name : "+result[1]+" "+result[2],compound=LEFT).grid(row=0)


def mousecrick() :
    global mouseframe

    keyboardframe.grid_forget()
    right.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()
    headphoneframe.grid_forget()
    walletframe.grid_forget()
    pointframe.grid_forget()

    #KEY ACTVATE
    mousebutton['bg'] = "#0066FF"
    keyboardbutton['bg'] = "#D4D4D4"

    mouseframe.grid_rowconfigure((0,1,2),weight=1)
    mouseframe.grid_columnconfigure((0,1,2),weight=1)
    mouseframe.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(mouseframe,text='MOUSE',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,sticky=NW,pady=10)

# def keyboarddata(productimagename,productname,price):
#     global keyboardresult
#     sql = "select * from keyboardproduct where productimagename=? and productname=? and price=?"
#     cursor.execute(sql,[productimagename,productname,price])
#     keyboardresult = cursor.fetchall()

def keyboardcrick() :
    global keyboardframe

    right.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()
    headphoneframe.grid_forget()
    mouseframe.grid_forget()
    walletframe.grid_forget()
    pointframe.grid_forget()

    keyboardbutton['bg'] = "#0066FF"
    mousebutton['bg'] = "#D4D4D4"

    keyboardframe.grid_rowconfigure((0,1,2,3,4),weight=1)
    keyboardframe.grid_columnconfigure((0,1,2),weight=1)
    keyboardframe.grid(row=1,column=1,rowspan=2,sticky='news')
    keyboardprice = []
    cursor.execute('SELECT  productname , price FROM keyboardproduct')
    keyboardresult = cursor.fetchall()
    for i in keyboardresult :
       print(i[0] + " "+ str(i[1]))
       keyboardprice.append(i[1])
    print(int(keyboardprice[2]) + int(keyboardprice[3]))

    Label(keyboardframe,text='KEYBOARD',bg='#ffffff',fg='#000000',font="Helvetica 25 bold").grid(row=0,columnspan=3)

    Label(keyboardframe,text=keybordtext[0]+"\n\n"+str(keyboardprice[0]) + " BATH",image=keyboardimage[0],bg='#ffffff',fg='#000000',font="Helvetica 15 ",compound='top').grid(row=1,column=0,sticky=SW,pady=10,padx=30)
    Spinbox(keyboardframe,width=15,bg='#0066FF',fg='#ffffff',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=2,column=0,sticky=NW,pady=10,padx=60)
    
    Label(keyboardframe,text=keybordtext[1]+"\n\n"+str(keyboardprice[1]) + " BATH",image=keyboardimage[1],bg='#ffffff',fg='#000000',font="Helvetica 15 ",compound='top').grid(row=1,column=1,sticky=SW,pady=10)
    Spinbox(keyboardframe,width=15,bg='#0066FF',fg='#ffffff',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=2,column=1,sticky=NW,pady=10,padx=30)
    
    Label(keyboardframe,text=keybordtext[2]+"\n\n"+str(keyboardprice[2]) + " BATH",image=keyboardimage[2],bg='#ffffff',fg='#000000',font="Helvetica 15 ",compound='top').grid(row=1,column=2,sticky=SW,pady=10)
    Spinbox(keyboardframe,width=15,bg='#0066FF',fg='#ffffff',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=2,column=2,sticky=NW,pady=10,padx=30)
    
    Label(keyboardframe,text=keybordtext[3]+"\n\n"+str(keyboardprice[3]) + " BATH",image=keyboardimage[3],bg='#ffffff',fg='#000000',font="Helvetica 15 ",compound='top').grid(row=3,column=0,sticky=SW,pady=10,padx=30)
    Spinbox(keyboardframe,width=15,bg='#0066FF',fg='#ffffff',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=4,column=0,sticky=NW,pady=10,padx=60)

    Label(keyboardframe,text=keybordtext[4]+"\n\n"+str(keyboardprice[4]) + " BATH",image=keyboardimage[4],bg='#ffffff',fg='#000000',font="Helvetica 15 ",compound='top').grid(row=3,column=1,sticky=SW,pady=10)
    Spinbox(keyboardframe,width=15,bg='#0066FF',fg='#ffffff',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=4,column=1,sticky=NW,pady=10,padx=30)
    
    Label(keyboardframe,text=keybordtext[5]+"\n\n"+str(keyboardprice[5]) + " BATH",image=keyboardimage[5],bg='#ffffff',fg='#000000',font="Helvetica 15 ",compound='top').grid(row=3,column=2,sticky=SW,pady=10)
    Spinbox(keyboardframe,width=15,bg='#0066FF',fg='#ffffff',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=4,column=2,sticky=NW,pady=10,padx=30)

def headphonecrick() :
    global headphoneframe

    right.grid_forget()
    keyboardframe.grid_forget()
    mouseframe.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()
    walletframe.grid_forget()
    pointframe.grid_forget()

    headphoneframe.grid_rowconfigure((0,1,2),weight=1)
    headphoneframe.grid_columnconfigure((0,1,2),weight=1)
    headphoneframe.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(headphoneframe,text='HEADPHONE',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,sticky=NW,pady=10)

def mywalletlayout() :
    global walletframe

    keyboardframe.grid_forget()
    right.grid_forget()
    updateframe.grid_forget()
    pointframe.grid_forget()
    deleteframe.grid_forget()
    headphoneframe.grid_forget()

    walletframe.grid_rowconfigure((0,1,2),weight=1)
    walletframe.grid_columnconfigure((0,1,2),weight=1)
    walletframe.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(walletframe,text='MY WALLET',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,sticky=NW,pady=10)

def mypointlayout() :
    global pointframe

    keyboardframe.grid_forget()
    walletframe.grid_forget()
    right.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()
    headphoneframe.grid_forget()

    pointframe.grid_rowconfigure((0,1,2),weight=1)
    pointframe.grid_columnconfigure((0,1,2),weight=1)
    pointframe.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(pointframe,text='MY POINT',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,sticky=NW,pady=10)

       
def logoutclick() :
    updateframe.grid_forget()
    mouseframe.grid_forget()
    deleteframe.grid_forget()
    right.grid_forget()
    top.grid_forget()
    welcomeframe.grid_forget()
    pwdframe.grid_forget()
    welcomelayout() 

connection()
root = mainwindow()
loginframe = Frame(root,bg='#ffffff')
registerframe = Frame(root,bg='#ffffff')
loginframeimg = Frame(root,bg='#ffffff')
loginframeimg2 = Frame(root,bg='#ffffff')
introframe = Frame(root,bg='#ffffff')
welcomeframe = Frame(root,bg='#ffffff')
updateframe = Frame(root,bg="#ffffff")
pwdframe = Frame(root,bg='#ffffff')
mouseframe = Frame(welcomeframe,bg='#ffffff')
keyboardframe = Frame(welcomeframe,bg='#ffffff')
headphoneframe = Frame(welcomeframe,bg='#ffffff')
walletframe = Frame(welcomeframe,bg='#ffffff')
pointframe = Frame(welcomeframe,bg='#ffffff')
updateframe = Frame(welcomeframe,bg='#ffffff')
deleteframe = Frame(welcomeframe,bg='#ffffff')
selectoption = StringVar()
usericon = PhotoImage(file='images/Usericon.png').subsample(2,2)
ATCimage = PhotoImage(file='images/ATC3.png')
shoping = PhotoImage(file="images/shoping.png").subsample(2,2)
nonlogo = PhotoImage(file='images/nonlogo.png').subsample(8,8)
ASUSROGAZOTH = PhotoImage(file='images/ASUSROGAZOTH.png').subsample(3,3)
EGATYPECMK9 = PhotoImage(file='images/EGATYPECMK9.png').subsample(3,3)
HYPERXALLOYORIGINS = PhotoImage(file='images/HYPERXALLOYORIGINS.png').subsample(2,2)
KEYCHRONK10MAXSILENT = PhotoImage(file='images/KEYCHRONK10MAXSILENT.png').subsample(3,3)
LOGITECHGG515 = PhotoImage(file='images/LOGITECHGG515.png').subsample(3,3)
REDRAGONPOLLUXPRO = PhotoImage(file='images/REDRAGONPOLLUXPRO.png').subsample(3,3)
keyboardimage = [HYPERXALLOYORIGINS,KEYCHRONK10MAXSILENT,ASUSROGAZOTH,LOGITECHGG515,REDRAGONPOLLUXPRO,EGATYPECMK9]
keybordtext = ['\nHYPERX\nALLOYORIGINS','\nKEY CHRONK\n10 MAX SILENT','\nASUS ROG \nAZOTH','\nLOGITEC HGG515','\nREDRAGON POLLUX PRO','\nEGA TYPE\nCMK9']
introshop()
root.mainloop()
cursor.close()
conn.close()
