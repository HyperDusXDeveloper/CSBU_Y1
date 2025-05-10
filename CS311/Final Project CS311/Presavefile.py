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
    h = 1000
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
                print(year)
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
    #MAIN
    global top,lefttop,leftbottom,right

    #MAIN CHANGE
    global keyboardbutton,mousebutton,headphonebutton

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
    Label(top,text="NON's ELEVENSHOP",bg='#ffffff',fg='#0066FF',font="Helvetica 50 ").grid(row=0,column=0,pady=10,sticky=W,padx=20)
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
    headphonebutton = Button(lefttop,text="HEADPHONE",width=20,command=headphonecrick,bg='#D4D4D4',fg='#ffffff',font="Helvetica 20 ")
    headphonebutton.grid(row=3,ipady=5,sticky=N)


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
    Label(right,image=shoping,bg='#fffffF',text="\nSHOPING\nYOUR DREAM",compound='top',fg='#0066FF',font="Helvetica 50 ").grid(row=0)
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
    headphonebutton['bg'] = "#D4D4D4"

    mouseframe.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    mouseframe.grid_columnconfigure((0,1,2),weight=1)
    mouseframe.grid(row=1,column=1,rowspan=2,sticky='news')
    mouseprice = []
    cursor.execute('SELECT  mousename , mouseprice FROM mouseproduct')
    mouseresult = cursor.fetchall()
    for i in mouseresult :
       print(i[0] + " "+ str(i[1]))
       mouseprice.append(i[1])
       print(mouseprice)
    # print(int(mouseprice[2]) + int(mouseprice[3]))

    Label(mouseframe,text='MOUSE',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=W)
    # Button(mouseframe,text="CHECK OUT",bg='#0066FF',fg='#ffffff',font="Helvetica 25 bold").grid(row=7,column=1,columnspan=2,pady=40,padx=100,sticky=E)
    Button(mouseframe,text="CHECK OUT",bg='#0066FF',fg='#ffffff',font="Helvetica 20 bold",width=15).grid(row=7,column=0,columnspan=3)

    
    Label(mouseframe,text=mousetext[0],image=mouseimage[0],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=0,sticky=SE,pady=10,padx=70)
    Label(mouseframe,text=str(mouseprice[0]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=0,sticky=NE,padx=65)
    Spinbox(mouseframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=0,sticky=NE,padx=60)
    
    Label(mouseframe,text=mousetext[1],image=mouseimage[1],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=1,sticky=SE,padx=30)
    Label(mouseframe,text=str(mouseprice[1]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=1,sticky=NE,padx=30)
    Spinbox(mouseframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=1,sticky=NE,padx=30)
    
    Label(mouseframe,text=mousetext[2],image=mouseimage[2],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=2,sticky=SW,pady=10,padx=100)
    Label(mouseframe,text=str(mouseprice[2]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=2,sticky=NW,padx=90)
    Spinbox(mouseframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=2,sticky=NW,pady=10,padx=90)
    
    Label(mouseframe,text=mousetext[3],image=mouseimage[3],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=0,sticky=SE,pady=10,padx=90)
    Label(mouseframe,text=str(mouseprice[3]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=0,sticky=NE,padx=60)
    Spinbox(mouseframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15").grid(row=6,column=0,sticky=NE,pady=10,padx=50)

    Label(mouseframe,text=mousetext[4],image=mouseimage[4],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=1,sticky=SE,pady=10,padx=50)
    Label(mouseframe,text=str(mouseprice[4]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=1,sticky=NE,padx=30)
    Spinbox(mouseframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=6,column=1,sticky=NE,pady=10,padx=30)
    
    Label(mouseframe,text=mousetext[5],image=mouseimage[5],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=2,sticky=SW,pady=10,padx=115)
    Label(mouseframe,text=str(mouseprice[5]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=2,sticky=NW,padx=90)
    Spinbox(mouseframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=6,column=2,sticky=NW,pady=10,padx=90)


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
    headphonebutton['bg'] = "#D4D4D4"

    keyboardframe.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    keyboardframe.grid_columnconfigure((0,1,2),weight=1)
    keyboardframe.grid(row=1,column=1,rowspan=2,sticky='news')
    keyboardprice = []
    cursor.execute('SELECT  keyboardname , keyboardprice FROM keyboardproduct')
    keyboardresult = cursor.fetchall()
    for i in keyboardresult :
       print(i[0] + " "+ str(i[1]))
       keyboardprice.append(i[1])
    print(int(keyboardprice[2]) + int(keyboardprice[3]))

    Label(keyboardframe,text='KEYBOARD',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=W)
    # Button(keyboardframe,text="CHECK OUT",bg='#0066FF',fg='#ffffff',font="Helvetica 25 bold").grid(row=7,column=1,columnspan=2,pady=40,padx=100,sticky=E)
    Button(keyboardframe,text="CHECK OUT",bg='#0066FF',fg='#ffffff',font="Helvetica 20 bold",width=15).grid(row=7,column=0,columnspan=3)

    
    Label(keyboardframe,text=keybordtext[0],image=keyboardimage[0],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=0,sticky=SW,pady=10,padx=30)
    Label(keyboardframe,text=str(keyboardprice[0]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=0,sticky=NW,padx=65)
    Spinbox(keyboardframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=0,sticky=NW,padx=60)
    
    Label(keyboardframe,text=keybordtext[1],image=keyboardimage[1],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=1,sticky=SW)
    Label(keyboardframe,text=str(keyboardprice[1]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=1,sticky=NW,padx=20)
    Spinbox(keyboardframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=1,sticky=NW,padx=30)
    
    Label(keyboardframe,text=keybordtext[2],image=keyboardimage[2],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=2,sticky=SW,pady=10)
    Label(keyboardframe,text=str(keyboardprice[2]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=2,sticky=NW,padx=30)
    Spinbox(keyboardframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=2,sticky=NW,pady=10,padx=30)
    
    Label(keyboardframe,text=keybordtext[3],image=keyboardimage[3],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=0,sticky=SW,pady=10,padx=30)
    Label(keyboardframe,text=str(keyboardprice[3]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=0,sticky=NW,padx=50)
    Spinbox(keyboardframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15").grid(row=6,column=0,sticky=NW,pady=10,padx=30)

    Label(keyboardframe,text=keybordtext[4],image=keyboardimage[4],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=1,sticky=SW,pady=10)
    Label(keyboardframe,text=str(keyboardprice[4]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=1,sticky=NW,padx=30)
    Spinbox(keyboardframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=6,column=1,sticky=NW,pady=10,padx=30)
    
    Label(keyboardframe,text=keybordtext[5],image=keyboardimage[5],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=2,sticky=SW,pady=10)
    Label(keyboardframe,text=str(keyboardprice[5]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=2,sticky=NW,padx=30)
    Spinbox(keyboardframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=6,column=2,sticky=NW,pady=10,padx=30)

def headphonecrick() :
    global headphoneframe

    right.grid_forget()
    keyboardframe.grid_forget()
    mouseframe.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()
    walletframe.grid_forget()
    pointframe.grid_forget()

    mousebutton['bg'] = "#D4D4D4"
    keyboardbutton['bg'] = "#D4D4D4"
    headphonebutton['bg'] = "#0066FF"

    headphoneframe.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    headphoneframe.grid_columnconfigure((0,1,2),weight=1)
    headphoneframe.grid(row=1,column=1,rowspan=2,sticky='news')
    headphoneprice = []
    cursor.execute('SELECT  headphonename , headphoneprice FROM headphoneproduct')
    headphoneresult = cursor.fetchall()
    for i in headphoneresult :
       print(i[0] + " "+ str(i[1]))
       headphoneprice.append(i[1])
    print(int(headphoneprice[2]) + int(headphoneprice[3]))

    Label(headphoneframe,text='HEADPHONE',bg='#ffffff',fg='#000000',font="Helvetica 30 bold").grid(row=0,column=0,pady=20,padx=20,sticky=W)
    Label(headphoneframe,text='GAMING',bg='#ffffff',fg='#0066FF',font="Helvetica 10 bold").grid(row=0,column=0,columnspan=2,pady=40,padx=280,sticky=NW)
    # Button(keyboardframe,text="CHECK OUT",bg='#0066FF',fg='#ffffff',font="Helvetica 25 bold").grid(row=7,column=1,columnspan=2,pady=40,padx=100,sticky=E)
    Button(headphoneframe,text="CHECK OUT",bg='#0066FF',fg='#ffffff',font="Helvetica 20 bold",width=15).grid(row=7,column=0,columnspan=3)

    
    Label(headphoneframe,text=headphonetext[0],image=headphoneimage[0],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=0,sticky=SW,padx=80)
    Label(headphoneframe,text=str(headphoneprice[0]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=0,sticky=NW,padx=65)
    Spinbox(headphoneframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=0,sticky=NW,padx=60)
    
    Label(headphoneframe,text=headphonetext[1],image=headphoneimage[1],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=1,sticky=SW,padx=60)
    Label(headphoneframe,text=str(headphoneprice[1]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=1,sticky=NW,padx=30)
    Spinbox(headphoneframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=1,sticky=NW,padx=30)
    
    Label(headphoneframe,text=headphonetext[2],image=headphoneimage[2],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=1,column=2,sticky=SW,padx=70)
    Label(headphoneframe,text=str(headphoneprice[2]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=2,column=2,sticky=NW,padx=40)
    Spinbox(headphoneframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=3,column=2,sticky=NW,pady=10,padx=50)
    
    Label(headphoneframe,text=headphonetext[3],image=headphoneimage[3],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=0,sticky=SW,padx=90)
    Label(headphoneframe,text=str(headphoneprice[3]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=0,sticky=NW,padx=65)
    Spinbox(headphoneframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15").grid(row=6,column=0,sticky=NW,pady=10,padx=60)

    Label(headphoneframe,text=headphonetext[4],image=headphoneimage[4],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=1,sticky=SW,padx=30)
    Label(headphoneframe,text=str(headphoneprice[4]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=1,sticky=NW,padx=30)
    Spinbox(headphoneframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=6,column=1,sticky=NW,pady=10,padx=35)
    
    Label(headphoneframe,text=headphonetext[5],image=headphoneimage[5],bg='#ffffff',fg='#000000',font="Helvetica 15 bold",compound='top').grid(row=4,column=2,sticky=SW,padx=30)
    Label(headphoneframe,text=str(headphoneprice[5]) + " BATH",bg='#ffffff',fg='#FF5050',font="Helvetica 25 bold").grid(row=5,column=2,sticky=NW,padx=30)
    Spinbox(headphoneframe,width=15,bg='#D4D4D4',fg='#000000',from_=0,to=10,justify='center',font="Helvetica 15 ").grid(row=6,column=2,sticky=NW,pady=10,padx=30)


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

#KEYBOARD
ASUSROGAZOTH = PhotoImage(file='images/ASUSROGAZOTH.png').subsample(3,3)
EGATYPECMK9 = PhotoImage(file='images/EGATYPECMK9.png').subsample(3,3)
HYPERXALLOYORIGINS = PhotoImage(file='images/HYPERXALLOYORIGINS.png').subsample(2,2)
KEYCHRONK10MAXSILENT = PhotoImage(file='images/KEYCHRONK10MAXSILENT.png').subsample(3,3)
LOGITECHGG515 = PhotoImage(file='images/LOGITECHGG515.png').subsample(3,3)
REDRAGONPOLLUXPRO = PhotoImage(file='images/REDRAGONPOLLUXPRO.png').subsample(3,3)
keyboardimage = [HYPERXALLOYORIGINS,KEYCHRONK10MAXSILENT,ASUSROGAZOTH,LOGITECHGG515,REDRAGONPOLLUXPRO,EGATYPECMK9]
keybordtext = ['\nHYPERX\nALLOYORIGINS','\nKEYCHRON\nK10MAXSILENT','\nASUS ROG\nAZOTH','\nLOGITEC\nHG G515','\nREDRAGON\nPOLLUX PRO','\nEGATYPECMK9']

#MOUSE
ASUSP713ROGHARPEACE = PhotoImage(file='images/ASUSP713ROGHARPEACE.png').subsample(5,5)
HYPERXPULSEFIREHASTE2MINI = PhotoImage(file='images/HYPERXPULSEFIREHASTE2MINI.png').subsample(5,5)
RAZERDEATHADDERV3PRO = PhotoImage(file='images/RAZERDEATHADDERV3PRO.png').subsample(5,5)
LOGITECHGPROXSUPERLIGHT2 = PhotoImage(file='images/LOGITECHGPROXSUPERLIGHT2.png').subsample(5,5)
RAZERVIPERV2PRO = PhotoImage(file='images/RAZERVIPERV2PRO.png').subsample(5,5)
RAZERCOBRAPRO = PhotoImage(file='images/RAZERCOBRAPRO.png').subsample(5,5)
mouseimage = [ASUSP713ROGHARPEACE,HYPERXPULSEFIREHASTE2MINI,RAZERDEATHADDERV3PRO,LOGITECHGPROXSUPERLIGHT2,RAZERVIPERV2PRO,RAZERCOBRAPRO]
mousetext = ['\nASUS P713\nROG HARPEACE','\nHYPERX PULSE\nFIREHASTE 2 MINI','\nRAZERDEATH\n ADDER V3 PRO','\nLOGITECH\nG PRO X','\nRAZER VIPER\nV2 PRO','\nRAZER\nCOBRA PRO']

#HEADPHONE
APPLEAIRPODSPRO2ND = PhotoImage(file='images/APPLEAIRPODSPRO2ND.png').subsample(5,5)
SONYWHULT900N = PhotoImage(file='images/SONYWHULT900N.png').subsample(5,5)
STEELSERIESARCTIS7 = PhotoImage(file='images/STEELSERIESARCTIS7.png').subsample(5,5)
RAZERBARRACUDAPRO = PhotoImage(file='images/RAZERBARRACUDAPRO.png').subsample(5,5)
ASUSROGDELTASWIRELESS = PhotoImage(file='images/ASUSROGDELTASWIRELESS.png').subsample(5,5)
RAZERWIRELESSBLACKSHARKV2 = PhotoImage(file='images/RAZERWIRELESSBLACKSHARKV2.png').subsample(5,5)
headphoneimage = [APPLEAIRPODSPRO2ND,SONYWHULT900N,STEELSERIESARCTIS7,RAZERBARRACUDAPRO,ASUSROGDELTASWIRELESS,RAZERWIRELESSBLACKSHARKV2]
headphonetext = ['\nAPPLEAIRPODS\nPRO 2ND','\nSONY\nWHULT 900 N','\nSTEELSERIE\nSARCTI S 7','\nRAZER BARRA\nCUDA PRO','\nASUS ROG\nDELTAS WIRELESS','\nRAZER WIRELESS\nBLACK SHARK V2']
introshop()
root.mainloop()
cursor.close()
conn.close()
