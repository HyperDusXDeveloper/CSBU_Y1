import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import IntVar
import random
def connection() :
    global conn,cursor
    conn = sqlite3.connect("database/Nonshop.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1400
    h = 1000
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#ffffff')
    root.title("Non's Web App [Shop]")
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
    Label(introframe,image=nonlogo,bg='#ffffff').grid(row=0,column=0,sticky=S,pady=30)
    Button(introframe,text="WELCOME",width=10,command=welcomelayout,bg='#0D0D0D',fg='#ffffff',font="Helvetica 25 ").grid(row=1,column=0,sticky=N)
    
def welcomelayout() :
    introframe.grid_remove()
    registerframe.grid_remove()
    settingsframe.grid_remove()
    topupframe.grid_remove()
    checkoutframe.grid_remove()
    walletframe.grid_remove()
    changeinformationframe.grid_remove()
    global user,pwd
    loginframe.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    loginframe.columnconfigure((0),weight=1)
    loginframe.grid(row=0,column=2,columnspan=2,rowspan=4,sticky='news')

    loginframeimg.rowconfigure((0),weight=1)
    loginframeimg.columnconfigure((0),weight=1)
    loginframeimg.grid(row=0,column=0,rowspan=6,sticky=W)

    Label(loginframeimg,image=welcomeshop).grid(row=0,column=0,rowspan=6,sticky=W)

    Label(loginframe,image=usericon,compound=LEFT,bg='#ffffff',fg='#0066FF',text="LOGIN PAGE",font="Helvetica 50 ").grid(row=2,column=0,sticky=SW,pady=20,padx=80)
    Label(loginframe,text="Username or Email",bg='#ffffff',fg='#000000',padx=20,font="Helvetica 30 ").grid(row=3,column=0,sticky=NW,padx=60)
    user = Entry(loginframe,bg='#ffffff',width=40)
    user.grid(row=3,column=0,sticky=SW,padx=80,pady=20)

    Label(loginframe,text="Password ",bg='#ffffff',fg='#000000',padx=20,font="Helvetica 30 ").grid(row=4,column=0,sticky=NW,padx=60)
    pwd = Entry(loginframe,bg='#ffffff',width=40,show='*')
    pwd.grid(row=4,column=0,sticky=SW,padx=80,pady=20)

    

    Button(loginframe,text="LOGIN",font="Helvetica 20 ",width=10,command=lambda:loginclick(user.get(),pwd.get()),bg='#0066FF',fg='#ffffff').grid(row=5,column=0,sticky=NW,padx=80)
    Button(loginframe,text="REGISTER",font="Helvetica 20 ",width=15,bg='#0066FF',fg='#ffffff',command=registerclick).grid(row=5,column=0,sticky=NW,padx=300)

def loginclick(user,pwd) :
    global result , username , username_str
    username = StringVar()
    topupframe.grid_remove()
    walletframe.grid_remove()
    checkoutframe.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()
    if user == "" or pwd == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        user.focus_force()
    else :
        sql = "select * from partner where username=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            username_str = user
            sql = "select * from partner where username=? and password=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if result :
                username.set(user)
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
    loginframe.grid_remove()
    topupframe.grid_remove()
    loginframeimg.grid_remove()
    walletframe.grid_remove()
    checkoutframe.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()
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
    topupframe.grid_remove()
    walletframe.grid_remove()
    changeinformationframe.grid_remove()
    print("Hello from registration")

    if fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Fullname")
        fullname.focus_force()
    elif username.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Username")
        username.focus_force()
    elif not year.get().isdigit():
        messagebox.showwarning("Admin: ", "Year must be a number")
        year.focus_force()
    elif year.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Year Birthday")
        year.focus_force()
    elif gender.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Gender")
        gender.focus_force()
    elif password.get() == "" :
        messagebox.showwarning("Admin: ","Please Enter Password")
        password.focus_force()
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
                userinformation = [fullname.get(),username.get(),year.get(),gender.get(),password.get(),point,wallet]
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
    global top,lefttop,leftbottom,right
    global keyboardbutton,mousebutton,headphonebutton,mywalletbutton,mypointbutton,checkoutbutton,point,wallet,walletbalance

    walletbalance = 0
    loginframe.grid_remove()
    loginframeimg.grid_remove()
    pwdframe.grid_remove()
    updateframe.grid_remove()
    settingsframe.grid_remove()
    topupframe.grid_remove()
    walletframe.grid_remove()
    checkoutframe.grid_remove()
    paymentconfirmframe.grid_remove()
    topupframe.grid_remove()
    walletframe.grid_remove()
    welcomeframe['bg'] = "#ffffff"
    changeinformationframe.grid_remove()

    fullname = result[0]
    
    welcomeframe.grid_rowconfigure((0),weight=1)
    welcomeframe.grid_rowconfigure((1),weight=3)
    welcomeframe.grid_rowconfigure((2),weight=2)

    welcomeframe.grid_columnconfigure((0),weight=1)
    welcomeframe.grid_columnconfigure((1),weight=6)

    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

    top = Frame(welcomeframe,bg='#ffffff', bd=2, relief="groove")
    top.grid_rowconfigure((0,1),weight=1)
    top.grid_columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    Label(top,text="NON's ELEVENSHOP",bg='#ffffff',fg='#0066FF',font="Helvetica 30 bold").grid(row=0,column=0,rowspan=2)
    Label(top,text="Welcome",bg='#ffffff',fg='#000000',font="Helvetica 20 bold").grid(row=0,column=0,sticky=SW)
    Label(top,text=fullname,bg='#ffffff',fg='#000000',font="Helvetica 20 bold").grid(row=1,column=0,sticky=NW)
    Button(top,image=settings,text="settings",bg='#ffffff',command=settingsclick).grid(row=0,column=0,rowspan=2,sticky=E,padx=60)

    lefttop = Frame(welcomeframe,bg='#ffffff', bd=2, relief="groove")
    lefttop.grid_rowconfigure((0,1,2,3,4),weight=1)
    lefttop.grid_columnconfigure(0,weight=1)
    lefttop.grid(row=1,column=0,sticky='news')

    Label(lefttop,text='MENU',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,column=0,pady=3,sticky=N)
    mousebutton = Button(lefttop,text="MOUSE",width=20,command=mouseclick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    mousebutton.grid(row=1,ipady=5,sticky=N,padx=25)
    keyboardbutton = Button(lefttop,text="KEYBOARD",width=20,command=keyboardclick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    keyboardbutton.grid(row=2,ipady=5,sticky=N,padx=25)
    headphonebutton = Button(lefttop,text="HEADPHONE",width=20,command=headphoneclick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    headphonebutton.grid(row=3,ipady=5,sticky=N,padx=25)
    checkoutbutton = Button(lefttop,text="CHECK OUT",width=20,command=checkoutclick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    checkoutbutton.grid(row=4,ipady=5,sticky=N,padx=25)


    leftbottom = Frame(welcomeframe,bg='#ffffff', bd=2, relief="groove")
    leftbottom.grid_rowconfigure((0,1,2,3),weight=1)
    leftbottom.grid_columnconfigure(0,weight=1)
    leftbottom.grid(row=2,column=0,sticky='news')
    Label(leftbottom,text='MYINFO',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,pady=10,sticky=S)
    mywalletbutton = Button(leftbottom,text="MY WALLET",width=20,command=mywalletlayout,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    mywalletbutton.grid(row=1,ipady=10,sticky=N,padx=25)
    mypointbutton = Button(leftbottom,text="MY POINT",width=20,command=mypointlayout,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    mypointbutton.grid(row=2,ipady=10,sticky=N,padx=25)

    right = Frame(welcomeframe,bg='#ffffff')
    right.grid_rowconfigure((0),weight=1)
    right.grid_columnconfigure(0,weight=1)
    right.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(right,image=shoping,bg='#fffffF',text="\nSHOPING\nYOUR DREAM",compound='top',fg='#0066FF',font="Helvetica 50 ").grid(row=0)

    cursor.execute("SELECT * FROM partner WHERE username=?", (username.get(),))
    result = cursor.fetchone()
    print(result)
    if result:
        fullname = result[0]
    else:
        fullname = "UNKnow Name"
    if result:
        point = result[5]
    else:
        point = 0

    if result :
        wallet = result[6]
    else:
        point = 0

def settingsclick():
    top.grid_remove()
    right.grid_remove()
    headphoneframe.grid_remove()
    keyboardframe.grid_remove()
    walletframe.grid_remove()
    pointframe.grid_remove()
    topupframe.grid_remove()
    lefttop.grid_remove()
    checkoutframe.grid_remove()
    leftbottom.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()

    mousebutton['bg'] = "#D4D4D4"
    keyboardbutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#D4D4D4"
    mywalletbutton['bg'] = "#D4D4D4"
    mypointbutton['bg'] = "#D4D4D4"
    checkoutbutton['bg'] = "#D4D4D4"

    settingsframe.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    settingsframe.grid_columnconfigure((0),weight=1)
    settingsframe.grid(row=0,column=0,columnspan=3,rowspan=3,sticky='news')
    Button(settingsframe,image=X,bg='#ffffff',command=randomclick).grid(row=0,column=0,sticky=E,padx=60)
    Label(settingsframe,text="SETTINGS",fg='#000000',bg='#ffffff',font="Helvetica 50 bold").grid(row=1,column=0)
    Button(settingsframe,text="CHANGE INFORMATION",bg='#0066FF',fg='#ffffff',font="Helvetica 30 bold",width=20,command=changeinformation).grid(row=2,column=0)
    Button(settingsframe,text="LOG OUT",bg='#FFB428',fg='#ffffff',font="Helvetica 30 bold",width=20,command=logoutclick).grid(row=3,column=0)
    Button(settingsframe,text="EXIT PROGRAM",bg='#FF5050',fg='#ffffff',font="Helvetica 30 bold",width=20,command=exit).grid(row=4,column=0)

def changeinformation():
    global fullname_entry, year_entry, gender_entry
 
    settingsframe.grid_remove()
    top.grid_remove()
    right.grid_remove()
    mouseframe.grid_remove()
    headphoneframe.grid_remove()
    keyboardframe.grid_remove()
    walletframe.grid_remove()
    pointframe.grid_remove()
    topupframe.grid_remove()
    lefttop.grid_remove()
    leftbottom.grid_remove()
    checkoutframe.grid_remove()
    paymentconfirmframe.grid_remove()

    changeinformationframe.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
    changeinformationframe.grid_columnconfigure((0,1), weight=1)
    changeinformationframe.grid(row=0, column=0, columnspan=3, rowspan=3, sticky='news')

    Button(changeinformationframe, image=X, bg='#ffffff', command=backtosetting).grid(row=1, column=1, sticky=NE, padx=60, pady=30)
    Label(changeinformationframe, text="\nUPDATE INFORMATION", font="Helvetica 30 bold", image=usericon, compound=TOP, bg='#ffffff').grid(row=1, columnspan=2)

    cursor.execute("SELECT fullname, year, gender FROM partner WHERE username = ?", (username_str,))
    user_data = cursor.fetchone()
    current_fullname, current_year, current_gender = user_data

    Label(changeinformationframe, text="FULL NAME :", bg='#ffffff', font="Helvetica 23 bold").grid(row=2, column=0, sticky='e')
    fullname_entry = Entry(changeinformationframe, bg="#ffffff")
    fullname_entry.insert(0, current_fullname)
    fullname_entry.grid(row=2, column=1, sticky='w', padx=20)

    Label(changeinformationframe, text="YEAR BIRTH :", bg='#ffffff', font="Helvetica 23 bold").grid(row=3, column=0, sticky='e')
    year_entry = Entry(changeinformationframe, bg="#ffffff")
    year_entry.insert(0, current_year)
    year_entry.grid(row=3, column=1, sticky='w', padx=20)

    Label(changeinformationframe, text="GENDER :", bg='#ffffff', font="Helvetica 23 bold").grid(row=4, column=0, sticky='e')
    gender_entry = Entry(changeinformationframe, bg="#ffffff")
    gender_entry.insert(0, current_gender)
    gender_entry.grid(row=4, column=1, sticky='w', padx=20)

    Button(changeinformationframe, text="SAVE CHANGES", width=20,
           command=lambda: updateinformation(fullname_entry.get(), year_entry.get(), gender_entry.get()),
           font="Helvetica 20 bold", bg='#0066FF', fg='#ffffff').grid(row=5, columnspan=2, ipady=10)
    
def backtosetting():
    changeinformationframe.grid_remove()
    topupframe.grid_remove()
    walletframe.grid_remove()
    settingsframe.grid(row=0,column=0,columnspan=3,rowspan=3,sticky='news')

def updateinformation(new_fullname, new_year, new_gender):
    if not new_fullname or not new_year.isdigit() or not new_gender:
        messagebox.showwarning("Admin:", "Please fill in the information completely and correctly.")
        return

    sql = "UPDATE partner SET fullname=?, year=?, gender=? WHERE username=?"
    cursor.execute(sql, (new_fullname, new_year, new_gender, username_str))
    conn.commit()
    messagebox.showinfo("Admin:", "Update partner successfully")

    cursor.execute("SELECT * FROM partner WHERE username=?", (username_str,))
    updated = cursor.fetchone()
    welcomepage(updated)

def clearclick() :
    username.config(state='normal')
    username.delete(0,END)
    fullname.delete(0,END)
    year.delete(0,END)
    gender.delete(0,END)

def mouseclick() :
    global mouseframe,mouseimage,mousetext,mousespy,mouseprice

    keyboardframe.grid_remove()
    right.grid_remove()
    updateframe.grid_remove()
    deleteframe.grid_remove()
    headphoneframe.grid_remove()
    walletframe.grid_remove()
    pointframe.grid_remove()
    walletframe.grid_remove()
    topupframe.grid_remove()
    checkoutframe.grid_remove()
    settingsframe.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()

    mousebutton['bg'] = "#0066FF"
    keyboardbutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#D4D4D4"
    mywalletbutton['bg'] = "#D4D4D4"
    mypointbutton['bg'] = "#D4D4D4"
    checkoutbutton['bg'] = "#D4D4D4"
    
    mouseframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    mouseframe.grid_columnconfigure((0,1,2),weight=1)
    mouseframe.grid(row=1,column=1,rowspan=2,sticky='news')

    Label(mouseframe,text='MOUSE',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=W)

    mouseimage = [ASUSP713ROGHARPEACE,HYPERXPULSEFIREHASTE2MINI,RAZERDEATHADDERV3PRO,LOGITECHGPROXSUPERLIGHT2,RAZERVIPERV2PRO,RAZERCOBRAPRO]
    mousetext = ['\nASUS P713\nROG HARPEACE','\nHYPERX PULSE\nFIREHASTE 2 MINI','\nRAZERDEATH\n ADDER V3 PRO','\nLOGITECH\nG PRO X','\nRAZER VIPER\nV2 PRO','\nRAZER\nCOBRA PRO']
    mouseprice = []
    cursor.execute('SELECT  mousename , mouseprice FROM mouseproduct')
    mouseresult = cursor.fetchall()
    for i in mouseresult:
        mouseprice.append(i[1])
    row, col = 1, 0
    for i in range(len(mousetext)):
        frame = Frame(mouseframe, bg='#ffffff')
        frame.grid(row=row, column=col, padx=30, pady=10)
        Label(frame, text=mousetext[i], image=mouseimage[i], compound='top', fg='#000000', bg='#ffffff', font="Helvetica 15 bold").pack()
        Label(frame, text=str(mouseprice[i]) + " BATH", fg='#FF5050', bg='#ffffff', font="Helvetica 25 bold").pack()
        Spinbox(frame, width=15, bg='#D4D4D4', fg='#000000', from_=0, to=10, justify='center', font="Helvetica 15", textvariable=mousespy[i]).pack()
        col += 1
        if col > 2:
            col = 0
            row += 1
            
def keyboardclick() :
    global keyboardframe,keyboardimage,keyboardtext,keyboardspy,keyboardprice

    right.grid_remove()
    updateframe.grid_remove()
    deleteframe.grid_remove()
    headphoneframe.grid_remove()
    mouseframe.grid_remove()
    walletframe.grid_remove()
    pointframe.grid_remove()
    topupframe.grid_remove()
    settingsframe.grid_remove()
    checkoutframe.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()
    
    keyboardbutton['bg'] = "#0066FF"
    mousebutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#D4D4D4"
    mywalletbutton['bg'] = "#D4D4D4"
    mypointbutton['bg'] = "#D4D4D4"
    checkoutbutton['bg'] = "#D4D4D4"

    keyboardframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    keyboardframe.grid_columnconfigure((0,1,2),weight=1)
    keyboardframe.grid(row=1,column=1,rowspan=2,sticky='news')

    Label(keyboardframe,text='KEYBOARD',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=W)

    keyboardimage = [HYPERXALLOYORIGINS,KEYCHRONK10MAXSILENT,ASUSROGAZOTH,LOGITECHGG515,REDRAGONPOLLUXPRO,EGATYPECMK9]
    keyboardtext = ['\nHYPERX\nALLOYORIGINS','\nKEYCHRON\nK10MAXSILENT','\nASUS ROG\nAZOTH','\nLOGITEC\nHG G515','\nREDRAGON\nPOLLUX PRO','\nEGA TYPE\nCMK 9']
    keyboardprice = []
    cursor.execute('SELECT  keyboardname , keyboardprice FROM keyboardproduct')
    keyboardresult = cursor.fetchall()
    for i in keyboardresult :
       keyboardprice.append(i[1])
       keyboardspy.append(IntVar(value=0))
    row, col = 1, 0
    for i in range(len(keyboardtext)):
        frame = Frame(keyboardframe, bg='#ffffff')
        frame.grid(row=row, column=col, padx=30, pady=10)
        Label(frame, text=keyboardtext[i], image=keyboardimage[i], compound='top', fg='#000000', bg='#ffffff', font="Helvetica 15 bold").pack()
        Label(frame, text=str(keyboardprice[i]) + " BATH", fg='#FF5050', bg='#ffffff', font="Helvetica 25 bold").pack()
        Spinbox(frame, width=15, bg='#D4D4D4', fg='#000000', from_=0, to=10, justify='center', font="Helvetica 15", textvariable=keyboardspy[i]).pack()
        col += 1
        if col > 2:
            col = 0
            row += 1
            
def headphoneclick() :
    global headphoneframe,headphoneimage,headphonetext,headphonespy,headphoneprice

    right.grid_remove()
    keyboardframe.grid_remove()
    mouseframe.grid_remove()
    updateframe.grid_remove()
    deleteframe.grid_remove()
    walletframe.grid_remove()
    pointframe.grid_remove()
    topupframe.grid_remove()
    settingsframe.grid_remove()
    checkoutframe.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()

    mousebutton['bg'] = "#D4D4D4"
    keyboardbutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#0066FF"
    mywalletbutton['bg'] = "#D4D4D4"
    mypointbutton['bg'] = "#D4D4D4"
    checkoutbutton['bg'] = "#D4D4D4"

    headphoneframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    headphoneframe.grid_columnconfigure((0,1,2),weight=1)
    headphoneframe.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(headphoneframe,text='HEADPHONE',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=W)

    headphoneimage = [APPLEAIRPODSPRO2ND,SONYWHULT900N,STEELSERIESARCTIS7,RAZERBARRACUDAPRO,ASUSROGDELTASWIRELESS,RAZERWIRELESSBLACKSHARKV2]
    headphonetext = ['\nAPPLEAIRPODS\nPRO 2ND','\nSONY\nWHULT 900 N','\nSTEELSERIE\nSARCTI S 7','\nRAZER BARRA\nCUDA PRO','\nASUS ROG\nDELTAS WIRELESS','\nRAZER WIRELESS\nBLACK SHARK V2']
    headphoneprice = []
    cursor.execute('SELECT  headphonename , headphoneprice FROM headphoneproduct')
    headphoneresult = cursor.fetchall()
    for i in headphoneresult :
       headphoneprice.append(i[1])
       headphonespy.append(IntVar(value=0))
    row, col = 1, 0
    for i in range(len(headphonetext)):
        frame = Frame(headphoneframe, bg='#ffffff')
        frame.grid(row=row, column=col, padx=30, pady=10)
        Label(frame, text=headphonetext[i], image=headphoneimage[i], compound='top', fg='#000000', bg='#ffffff', font="Helvetica 15 bold").pack()
        Label(frame, text=str(headphoneprice[i]) + " BATH", fg='#FF5050', bg='#ffffff', font="Helvetica 25 bold").pack()
        Spinbox(frame, width=15, bg='#D4D4D4', fg='#000000', from_=0, to=10, justify='center', font="Helvetica 15", textvariable=headphonespy[i]).pack()
        col += 1
        if col > 2:
            col = 0
            row += 1

def checkoutclick():
    right.grid_remove()
    keyboardframe.grid_remove()
    mouseframe.grid_remove()
    updateframe.grid_remove()
    deleteframe.grid_remove()
    walletframe.grid_remove()
    pointframe.grid_remove()
    topupframe.grid_remove()
    settingsframe.grid_remove()
    changeinformationframe.grid_remove()
    paymentconfirmframe.grid_remove()

    checkoutframe.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29), weight=1)
    checkoutframe.grid_columnconfigure((0,1,2,3), weight=1)
    checkoutframe.grid(row=1, column=1, rowspan=2, sticky='news')

    checkoutframe.config(bg='#ffffff')
    mousebutton['bg'] = "#D4D4D4"
    keyboardbutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#D4D4D4"
    mywalletbutton['bg'] = "#D4D4D4"
    mypointbutton['bg'] = "#D4D4D4"
    checkoutbutton['bg'] = "#0066FF"

    global wallet,pointcheckout,discountcheckout,discount,point,summarypointcheckout,totalprice,finalpricecheckout,finalprice,walletbalance,pointdiscount50,pointalreadyused

    cursor.execute("SELECT wallet FROM partner WHERE username=?", (username.get(),))
    result = cursor.fetchone()
    if result:
        wallet = result[0]
    else:
        wallet = 0

    for widget in checkoutframe.winfo_children():
        widget.destroy()

    Label(checkoutframe, text="CHECKOUT SUMMARY", font="Helvetica 30 bold", bg="#ffffff", fg="#0066FF").grid(row=0, column=0, columnspan=4, pady=5)
    pointalreadyused = Label(checkoutframe, text="POINT DISCOUNT", font="Helvetica 12 bold", bg="#ffffff", fg="#000000")
    pointalreadyused.grid(row=0, column=3,sticky=E)
    pointdiscount50 = Label(checkoutframe, text=f"{point} // 50", font="Helvetica 12 bold", bg="#ffffff", fg="#000000")
    pointdiscount50.grid(row=0, column=3,sticky=SE)

    row = 1
    totalprice = 0
    Label(checkoutframe, text="PRODUCT", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=row, column=0, sticky='w', padx=10)
    Label(checkoutframe, text="PRODUCT PRICE", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=row, column=1, sticky='w', padx=10)
    Label(checkoutframe, text="Qty", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=row, column=2)
    Label(checkoutframe, text="SUBTOTAL", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=row, column=3, sticky='e', padx=10)
    row += 1 

    for i in range(6):
        qty = mousespy[i].get()
        if qty > 0:
            name = mousetext[i].replace('\n', ' ')
            productprice = mouseprice[i]
            price = mouseprice[i]
            subtotal = qty * price
            totalprice += subtotal
            Label(checkoutframe, text=f"{name}", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=0, sticky='w', padx=10)
            Label(checkoutframe, text=f"{productprice} BAHT", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=1, sticky='w', padx=10)
            Label(checkoutframe, text=f"{qty}", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=2)
            Label(checkoutframe, text=f"{subtotal} BAHT", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=3, sticky='e', padx=10)
            row += 1

    for i in range(6):
        qty = keyboardspy[i].get()
        if qty > 0:
            name = keyboardtext[i].replace('\n', ' ')
            productprice = keyboardprice[i]
            price = keyboardprice[i]
            subtotal = qty * price
            totalprice += subtotal
            Label(checkoutframe, text=f"{name}", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=0, sticky='w', padx=10)
            Label(checkoutframe, text=f"{productprice} BAHT", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=1, sticky='w', padx=10)
            Label(checkoutframe, text=f"{qty}", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=2)
            Label(checkoutframe, text=f"{subtotal} BAHT", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=3, sticky='e', padx=10)
            row += 1

    for i in range(6):
        qty = headphonespy[i].get()
        if qty > 0:
            name = headphonetext[i].replace('\n', ' ')
            productprice = headphoneprice[i]
            price = headphoneprice[i]
            subtotal = qty * price
            totalprice += subtotal
            Label(checkoutframe, text=f"{name}", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=0, sticky='w', padx=10)
            Label(checkoutframe, text=f"{productprice } BAHT", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=1, sticky='w', padx=10)
            Label(checkoutframe, text=f"{qty}", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=2)
            Label(checkoutframe, text=f"{subtotal} BAHT", bg="#ffffff", font="Helvetica 12 bold").grid(row=row, column=3, sticky='e', padx=10)
            row += 1

    discount = point // 50
    finalprice = max(wallet - totalprice  , 0)
    walletbalance = (wallet - totalprice)

    #CHECKOUT ROW
    Label(checkoutframe, text="CHECKOUT", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=22, column=0, sticky='w', padx=10)
    Label(checkoutframe, text="MY WALLET", bg="#ffffff", font="Helvetica 15 bold",fg="#0066FF").grid(row=23, column=0, sticky='w', padx=10)
    Label(checkoutframe, text="TOTAL PRICE", bg="#ffffff", font="Helvetica 15 bold",fg="#000000").grid(row=24, column=0, sticky='w', padx=10)
    Label(checkoutframe, text="POINT", bg="#ffffff", font="Helvetica 15 bold",fg="#000000").grid(row=25, column=0, sticky='w', padx=10)
    Label(checkoutframe, text="SUMMARY PRICE", bg="#ffffff", font="Helvetica 15 bold",fg="#000000").grid(row=26, column=0, sticky='w', padx=10)

    #INFOR ROW
    Label(checkoutframe, text="INFORMATION", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=22, column=1, sticky='w', padx=10)
    Label(checkoutframe, text=f"{wallet} BAHT", bg="#ffffff", font="Helvetica 15 bold",fg="#0066FF").grid(row=23, column=1,sticky=W, padx=10)
    Button(checkoutframe, text="TOP UP MONEY", font="Helvetica 10 bold",bg='#0066FF',fg='#ffffff',command=topupwalletclick).grid(row=23, column=0, sticky=E)
    Label(checkoutframe, text=f"{totalprice} BAHT", bg="#ffffff", font="Helvetica 15 bold",fg="#FF5050").grid(row=24, column=1,sticky=W, padx=10)
    pointcheckout = Label(checkoutframe, text=f"{point} POINT", bg="#ffffff", font="Helvetica 15 bold",fg="#000000")
    pointcheckout.grid(row=25, column=1,sticky=W, padx=10)
    Button(checkoutframe, text="USE POINT", font="Helvetica 12 bold",bg='#5EFF71',fg='#000000',command=pointdiscount).grid(row=25, column=0, padx=30)
    Label(checkoutframe, text="-", bg="#ffffff", font="Helvetica 15 bold",fg="#000000").grid(row=26, column=1, padx=10)

    #DISCOUNT ROW
    Label(checkoutframe, text="DISCOINT", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=22, column=2)
    Label(checkoutframe, text="-", bg="#ffffff", font="Helvetica 15 bold",fg="#0066FF").grid(row=23, column=2, padx=10)
    Label(checkoutframe, text="-", bg="#ffffff", font="Helvetica 15 bold",fg="#FF5050").grid(row=24, column=2, padx=10)
    discountcheckout = Label(checkoutframe, text="-", bg="#ffffff", font="Helvetica 15 bold",fg="#000000")
    discountcheckout.grid(row=25, column=2, padx=10)
    Label(checkoutframe, text="-", bg="#ffffff", font="Helvetica 15 bold",fg="#000000").grid(row=26, column=2, padx=10)
    
    #SUMMARY COUNT ROW
    Label(checkoutframe, text="SUMMARY COUNT", font="Helvetica 10 bold", bg="#ffffff",fg="#656565").grid(row=22, column=3, sticky='e', padx=10)
    Label(checkoutframe, text=f"{wallet} BAHT", bg="#ffffff", font="Helvetica 15 bold",fg="#0066FF").grid(row=23, column=3,sticky=E, padx=10)
    Label(checkoutframe, text=f"{(-1 * totalprice)} BAHT", bg="#ffffff", font="Helvetica 15 bold",fg="#FF5050").grid(row=24, column=3,sticky=E, padx=10)
    summarypointcheckout = Label(checkoutframe, text=f"0 BAHT", bg="#ffffff", font="Helvetica 15 bold",fg="#0066FF")
    summarypointcheckout.grid(row=25, column=3,sticky=E, padx=10)
    finalpricecheckout = Label(checkoutframe, text=f"{(finalprice)} BAHT", bg="#ffffff", font="Helvetica 15 bold",fg="#5EFF71")
    finalpricecheckout.grid(row=26, column=3,sticky=E, padx=10)
    Button(checkoutframe,text="CHECK OUT" ,bg='#0066FF',fg='#ffffff', command=checkproduct).grid(row=27, column=3, sticky=SE, padx=10)

def checkproduct():

    if totalprice == 0:
        messagebox.showwarning("Admin:", "Please select a product")
        return
    if wallet < totalprice:
        messagebox.showwarning("Admin:", "Please top up, there is insufficient funds")
        return
    messagebox.showinfo("Admin:", "Payment Successfully")
    resetspinboxvalues()
    paymentconfirm()

def paymentconfirm():
    keyboardframe.grid_remove()
    headphoneframe.grid_remove()
    mouseframe.grid_remove()
    updateframe.grid_remove()
    deleteframe.grid_remove()
    walletframe.grid_remove()
    pointframe.grid_remove()
    topupframe.grid_remove()
    changeinformationframe.grid_remove()
    settingsframe.grid_remove()
    checkoutframe.grid_remove()
    paymentconfirmframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    paymentconfirmframe.grid_columnconfigure((0),weight=1)
    paymentconfirmframe.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(paymentconfirmframe,image=shoping,bg='#fffffF',text="PAYMENT\nSUCCESSFUL",compound='top',fg='#0066FF',font="Helvetica 40 bold").grid(row=1,column=0,sticky=S)
    Label(paymentconfirmframe,bg='#fffffF',text=f"Wallet Balance {walletbalance} BAHT",fg='#000000',font="Helvetica 40 bold").grid(row=2,column=0,sticky=S,ipadx=100)
    Label(paymentconfirmframe,bg='#fffffF',text=f"Receive {(totalprice)} Point",fg='#000000',font="Helvetica 40 bold").grid(row=3,column=0,sticky=N,ipadx=100)

    cursor.execute("SELECT point FROM partner WHERE username=?", (username.get(),))
    current_point = cursor.fetchone()[0]

    new_point = current_point + int(totalprice)
    sql = "UPDATE partner SET point=? WHERE username=?"
    cursor.execute(sql, (new_point, username.get()))
    conn.commit()
    
    sql = "UPDATE partner SET wallet=? WHERE username=?"
    cursor.execute(sql, (walletbalance, username.get()))
    conn.commit()

    cursor.execute("SELECT point FROM partner WHERE username=?", (username.get(),))
    updated_point = cursor.fetchone()[0]
    global point
    point = updated_point

def pointdiscount():
    global walletbalance
    pointcheckout['text'] = "-"
    discountcheckout['text'] = f"{(discount)} BAHT"
    summarypointcheckout['text'] = f"+ {(discount)} BAHT"
    finalpricecheckout['text'] = f"{(finalprice - (-1 * discount))} BAHT"
    pointalreadyused['text'] = f" Point Already Used"
    pointalreadyused['fg'] = "#5EFF71"
    pointalreadyused['bg'] = "#000000"
    pointdiscount50['fg'] = "#5EFF71"
    pointdiscount50['bg'] = "#000000"
    pointdiscount50['text'] = f"{(point)} // 50 = {discount} BAHT"

    walletbalance = (finalprice + discount)
    resetpoint = 0
    sql = "UPDATE partner SET point=? WHERE username=?"
    cursor.execute(sql, (resetpoint, username.get()))
    conn.commit()

def mywalletlayout() :
    global walletframe,wallet,walletcolor
    checkoutframe.grid_remove()
    right.grid_remove()
    updateframe.grid_remove()
    pointframe.grid_remove()
    deleteframe.grid_remove()
    mouseframe.grid_remove()
    keyboardframe.grid_remove()
    headphoneframe.grid_remove()
    changeinformationframe.grid_remove()
    paymentconfirmframe.grid_remove()
    topupframe.grid_remove()

    mousebutton['bg'] = "#D4D4D4"
    keyboardbutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#D4D4D4"
    mywalletbutton['bg'] = "#0066FF"
    mypointbutton['bg'] = "#D4D4D4"
    checkoutbutton['bg'] = "#D4D4D4"

    walletframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    walletframe.grid_columnconfigure((0,1,2),weight=1)
    walletframe.grid(row=1,column=1,rowspan=2,sticky='news')
    
    cursor.execute("SELECT * FROM partner WHERE username=?", (username.get(),))
    result = cursor.fetchone()
    if result:
        wallet = result[6]
    else:
        wallet = 0

    Label(walletframe,text='MY Wallet',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=NW)
    Label(walletframe,image=walletimg,text='\nMONEY IN YOU WALLET',bg='#ffffff',fg='#989898',font="Helvetica 40 bold",compound=TOP).grid(row=1,column=0,columnspan=3,rowspan=3,sticky=N)
    walletcolor = Label(walletframe,text=str(wallet)+"  "+"BATH",bg='#ffffff',fg='#000000',font="Helvetica 70 bold")
    walletcolor.grid(row=3,column=0,columnspan=4,sticky=S,pady=50,ipadx=200)
    Button(walletframe,text=" BUY PRODUCT ",bg='#0066FF',fg='#ffffff',font="Helvetica 30 bold",width=15,command=usemoneywallet).grid(row=4,column=0,sticky=NE,padx=20)
    Button(walletframe,text=" TOP UP YOU WALLET ",bg='#0066FF',fg='#ffffff',font="Helvetica 30 bold",width=20,command=topupwalletclick).grid(row=4,column=2,sticky=NW,padx=20)

def usemoneywallet():
    walletframe.grid_remove()
    topupframe.grid_remove()
    randomclick()

def topupwalletclick():
    global topup
    right.grid_remove()
    checkoutframe.grid_remove()
    updateframe.grid_remove()
    pointframe.grid_remove()
    deleteframe.grid_remove()
    mouseframe.grid_remove()
    keyboardframe.grid_remove()
    headphoneframe.grid_remove()
    paymentconfirmframe.grid_remove()
    walletframe.grid_remove()
    changeinformationframe.grid_remove()

    topupframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    topupframe.grid_columnconfigure((0,1,2),weight=1)
    topupframe.grid(row=1,column=1,rowspan=2,sticky='news')
    var = StringVar()
    Label(topupframe,text='TOP UP WALLET',bg='#ffffff',fg='#000000',font="Helvetica 40 bold").grid(row=0,column=0,pady=20,padx=20,sticky=NW)
    Label(topupframe,text='SELECT BANK\n',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=1,column=0,pady=20,padx=20,sticky=NW)
    Radiobutton(topupframe,text='  SCB BANK',bg='#ffffff',fg='#000000',font="Helvetica 15 bold",image=scb,compound='left',value="Option 1",variable=var).grid(row=1,column=0,pady=20,padx=20,sticky=W)
    Radiobutton(topupframe,text='  KRUNGSRI BANK',bg='#ffffff',fg='#000000',font="Helvetica 15 bold",image=krungsri,compound='left',value="Option 2",variable=var).grid(row=1,column=0,pady=20,padx=20,sticky=E)
    Radiobutton(topupframe,text='  KASIKORN BANK',bg='#ffffff',fg='#000000',font="Helvetica 15 bold",image=kasikorn,compound='left',value="Option 3",variable=var).grid(row=1,column=1,pady=20,padx=20,sticky=W)
    Label(topupframe,text='SPECIFY THE AMOUNT',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=2,column=0,pady=20,padx=20,sticky=NW)
    topup = Entry(topupframe,bg='#ffffff',width=50)
    topup.grid(row=2,column=0,sticky=SW,padx=20,pady=30)
    Button(topupframe,text="PAY NOW",bg='#0066FF',fg='#ffffff',font="Helvetica 20 bold",width=10,command=topupwallet).grid(row=3,column=0,sticky=NW,padx=20)

def topupwallet():
    topupmoney = topup.get()
    print(topupmoney)
    global username
    if not topupmoney.isdigit():
        messagebox.showwarning("Error isdigit Number","Please Input Number")
        return

    if result is not None:
        walletmoney = int(result[6])
        wallet = walletmoney + int(topupmoney)
        cursor.execute("SELECT wallet FROM partner WHERE username=?", (username.get(),))
        currentwallet = cursor.fetchone()[0]
        topupamount = int(topupmoney)
        newwallet = currentwallet + topupamount
        if newwallet > 1000000:
            messagebox.showwarning("Admin:", "Wallet limit exceeded (max 1,000,000 BAHT)")
            return
        sql = "UPDATE partner SET wallet=? WHERE username=?"
        cursor.execute(sql, (newwallet, username.get()))
        conn.commit()
        messagebox.showinfo("Admin:","Update wallet successfully")
        topupwalletclick()
    
def mypointlayout() :
    global pointframe,point
    checkoutframe.grid_remove()
    keyboardframe.grid_remove()
    walletframe.grid_remove()
    right.grid_remove()
    updateframe.grid_remove()
    deleteframe.grid_remove()
    headphoneframe.grid_remove()
    topupframe.grid_remove()
    paymentconfirmframe.grid_remove()

    mousebutton['bg'] = "#D4D4D4"
    keyboardbutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#D4D4D4"
    mywalletbutton['bg'] = "#D4D4D4"
    mypointbutton['bg'] = "#0066FF"
    checkoutbutton['bg'] = "#D4D4D4"

    pointframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    pointframe.grid_columnconfigure((0,1,2),weight=1)
    pointframe.grid(row=1,column=1,rowspan=2,sticky='news')

    cursor.execute("SELECT point FROM partner WHERE username=?", (username_str,))
    result = cursor.fetchone()
    if result:
        point = result[0]
    else:
        point = 0

    Label(pointframe,text='MY POINT',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=NW)
    Label(pointframe,text='\nYOU HAVE POINT',image=nonpoint,bg='#ffffff',fg='#989898',font="Helvetica 40 bold",compound=TOP).grid(row=1,column=0,columnspan=3,rowspan=3,sticky=N)
    Label(pointframe,text=str(point)+"  "+"POINT",bg='#ffffff',fg='#000000',font="Helvetica 70 bold").grid(row=3,column=0,columnspan=4,sticky=S,pady=50,ipadx=220)
    Button(pointframe,text=" USE POINT ",bg='#0066FF',fg='#ffffff',font="Helvetica 30 bold",width=20,command=usepoint).grid(row=4,column=0,columnspan=3,sticky=N,padx=50)

def usepoint() :
    checkoutframe.grid_remove()
    pointframe.grid_remove()
    topupframe.grid_remove()
    walletframe.grid_remove()
    paymentconfirmframe.grid_remove()
    randomclick()
       
def logoutclick() :
    resetspinboxvalues()
    topupframe.grid_remove()
    right.grid_remove()
    lefttop.grid_remove()
    checkoutframe.grid_remove()
    leftbottom.grid_remove()
    top.grid_remove()
    welcomeframe.grid_remove()
    pwdframe.grid_remove()
    topupframe.grid_remove()
    walletframe.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()
    welcomelayout() 

def resetspinboxvalues():
    for var in mousespy:
        var.set(0)
    for var in keyboardspy:
        var.set(0)
    for var in headphonespy:
        var.set(0)

def randomclick():
    checkoutframe.grid_remove()
    topupframe.grid_remove()
    walletframe.grid_remove()
    right.grid_remove()
    settingsframe.grid_remove()
    paymentconfirmframe.grid_remove()
    changeinformationframe.grid_remove()
    optionnumber =(1,2,3)
    top.grid(row=0,columnspan=2,sticky='news')
    leftbottom.grid(row=2,column=0,sticky='news')
    lefttop.grid(row=1,column=0,sticky='news')
    randomnumber = random.choice(optionnumber)
    print(randomnumber)
    if randomnumber == 1 :
        mouseclick()
    elif randomnumber == 2 :
        keyboardclick()
    else :
        headphoneclick()
            
connection()
root = mainwindow()
mousespy = [IntVar(value=0) for _ in range(6)]
headphonespy = [IntVar(value=0) for _ in range(6)]
keyboardspy = [IntVar(value=0) for _ in range(6)]
loginframe = Frame(root,bg='#ffffff')
registerframe = Frame(root,bg='#ffffff')
loginframeimg = Frame(root,bg='#ffffff')
loginframeimg2 = Frame(root,bg='#ffffff')
introframe = Frame(root,bg='#ffffff')
updateframe = Frame(root,bg="#ffffff")
pwdframe = Frame(root,bg='#ffffff')

welcomeframe = Frame(root,bg='#ffffff')
paymentconfirmframe = Frame(welcomeframe,bg='#ffffff')
changeinformationframe = Frame(welcomeframe,bg='#ffffff')
mouseframe = Frame(welcomeframe,bg='#ffffff')
keyboardframe = Frame(welcomeframe,bg='#ffffff')
headphoneframe = Frame(welcomeframe,bg='#ffffff')
walletframe = Frame(welcomeframe,bg='#ffffff')
topupframe = Frame(welcomeframe,bg='#ffffff')
settingsframe = Frame(welcomeframe,bg='#ffffff')
pointframe = Frame(welcomeframe,bg='#ffffff')
updateframe = Frame(welcomeframe,bg='#ffffff')
deleteframe = Frame(welcomeframe,bg='#ffffff')
checkoutframe = Frame(welcomeframe,bg='#ffffff')

selectoption = StringVar()
usericon = PhotoImage(file='images/Usericon.png').subsample(2,2)
welcomeshop = PhotoImage(file='images/welcomeshop.png')
shoping = PhotoImage(file="images/shoping.png").subsample(2,2)
nonlogo = PhotoImage(file='images/nonlogo.png').subsample(2,2)
settings = PhotoImage(file='images/settings.png').subsample(3,3)
walletimg = PhotoImage(file='images/wallet.png').subsample(2,2)
X = PhotoImage(file='images/X.png').subsample(2,2)
nonpoint = PhotoImage(file='images/nonpoint.png').subsample(3,3)
scb = PhotoImage(file='images/scb.png').subsample(2,2)
krungsri = PhotoImage(file='images/krungsri.png').subsample(2,2)
kasikorn = PhotoImage(file='images/kasikorn.png').subsample(2,2)

#KEYBOARD
ASUSROGAZOTH = PhotoImage(file='images/ASUSROGAZOTH.png').subsample(3,3)
EGATYPECMK9 = PhotoImage(file='images/EGATYPECMK9.png').subsample(3,3)
HYPERXALLOYORIGINS = PhotoImage(file='images/HYPERXALLOYORIGINS.png').subsample(2,2)
KEYCHRONK10MAXSILENT = PhotoImage(file='images/KEYCHRONK10MAXSILENT.png').subsample(3,3)
LOGITECHGG515 = PhotoImage(file='images/LOGITECHGG515.png').subsample(3,3)
REDRAGONPOLLUXPRO = PhotoImage(file='images/REDRAGONPOLLUXPRO.png').subsample(3,3)

#MOUSE
ASUSP713ROGHARPEACE = PhotoImage(file='images/ASUSP713ROGHARPEACE.png').subsample(5,5)
HYPERXPULSEFIREHASTE2MINI = PhotoImage(file='images/HYPERXPULSEFIREHASTE2MINI.png').subsample(5,5)
RAZERDEATHADDERV3PRO = PhotoImage(file='images/RAZERDEATHADDERV3PRO.png').subsample(5,5)
LOGITECHGPROXSUPERLIGHT2 = PhotoImage(file='images/LOGITECHGPROXSUPERLIGHT2.png').subsample(5,5)
RAZERVIPERV2PRO = PhotoImage(file='images/RAZERVIPERV2PRO.png').subsample(5,5)
RAZERCOBRAPRO = PhotoImage(file='images/RAZERCOBRAPRO.png').subsample(5,5)

#HEADPHONE
APPLEAIRPODSPRO2ND = PhotoImage(file='images/APPLEAIRPODSPRO2ND.png').subsample(5,5)
SONYWHULT900N = PhotoImage(file='images/SONYWHULT900N.png').subsample(5,5)
STEELSERIESARCTIS7 = PhotoImage(file='images/STEELSERIESARCTIS7.png').subsample(4,4)
RAZERBARRACUDAPRO = PhotoImage(file='images/RAZERBARRACUDAPRO.png').subsample(5,5)
ASUSROGDELTASWIRELESS = PhotoImage(file='images/ASUSROGDELTASWIRELESS.png').subsample(5,5)
RAZERWIRELESSBLACKSHARKV2 = PhotoImage(file='images/RAZERWIRELESSBLACKSHARKV2.png').subsample(5,5)

introshop()
root.mainloop()
cursor.close()
conn.close()