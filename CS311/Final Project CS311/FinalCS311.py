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
    Button(introframe,text="WELCOME",width=10,command=loginlayout,bg='#0066FF',fg='#ffffff',font="Helvetica 25 ").grid(row=1,column=0,sticky=N)
    

def loginlayout() :
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
    loginbtn = Button(registerframe,text="Back to Login",command=loginlayout,bg='#0066FF',fg='#ffffff')
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
                retrivedata()
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

def retrivedata() :
    sql = "select * from partner"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)


def welcomepage(result) :
    global top,left,right,bottom
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
    Button(lefttop,text="MOUSE",width=20,command=COMPUTEREQUIPMENT,bg='#0066FF',fg='#ffffff',font="Helvetica 20 ").grid(row=1,ipady=5,sticky=N)
    Button(lefttop,text="KEYBOARD",width=20,command=updateclick,bg='#0066FF',fg='#ffffff',font="Helvetica 20 ").grid(row=2,ipady=5,sticky=N)
    Button(lefttop,text="HEADPHONE",width=20,command=deleteclick,bg='#0066FF',fg='#ffffff',font="Helvetica 20 ").grid(row=3,ipady=5,sticky=N)


    leftbottom = Frame(welcomeframe,bg='#ffffff', bd=2, relief="groove")
    leftbottom.grid_rowconfigure((0,1,2),weight=1)
    leftbottom.grid_columnconfigure(0,weight=1)
    leftbottom.grid(row=2,column=0,sticky='news')
    Label(leftbottom,text='MYINFO',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,pady=10,sticky=S)
    Button(leftbottom,text="MY WALLET",width=15,command=logoutclick,bg='#0066FF',fg='#ffffff',font="Helvetica 25 ").grid(row=1,ipady=10,sticky=N)
    Button(leftbottom,text="MY POINT",width=15,command=logoutclick,bg='#0066FF',fg='#ffffff',font="Helvetica 25 ").grid(row=2,ipady=10,sticky=N)
    
    #RIGHT

    right = Frame(welcomeframe,bg='#ffffff')
    right.grid_rowconfigure((0),weight=1)
    right.grid_columnconfigure(0,weight=1)
    right.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(right,image=shoping,bg='#fffffF',text="SHOPING",compound='top',fg='#0066FF',font="Helvetica 60 ").grid(row=0)
    #create widgets
    # Label(top2,image=usericon,bg='#ffffff',text="partner ID : "+str(result[0])+"\n"+"Name : "+result[1]+" "+result[2],compound=LEFT).grid(row=0)


def COMPUTEREQUIPMENT() :
    global addframe
    global codebox,namebox,oderid,roombox

    right.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()
    
    addframe.grid_rowconfigure((0,1,2),weight=1)
    addframe.grid_columnconfigure((0,1,2),weight=1)
    addframe.grid(row=1,column=1,rowspan=2,sticky='news')
    Label(addframe,text='COMPUTER EQUIPMENT',bg='#ffffff',fg='#000000',font="Helvetica 40 ").grid(row=0,sticky=NW,pady=10)
    
    Label(addframe,image=case1,bg='#ffffff',text="CASE1",compound='top',fg='#0066FF',font="Helvetica 30 ").grid(row=1,column=0)
    Button(addframe,text="BUY",width=10,bg='#0066FF',fg='#ffffff',font="Helvetica 20 ").grid(row=2,column=0,ipady=10)

    Label(addframe,image=case1,bg='#ffffff',text="CASE2",compound='top',fg='#0066FF',font="Helvetica 30 ").grid(row=1,column=1)
    Button(addframe,text="BUY",width=10,bg='#0066FF',fg='#ffffff',font="Helvetica 20 ").grid(row=2,column=1,ipady=10)

    Label(addframe,image=case1,bg='#ffffff',text="CASE3",compound='top',fg='#0066FF',font="Helvetica 30 ").grid(row=1,column=2)
    Button(addframe,text="BUY",width=10,bg='#0066FF',fg='#ffffff',font="Helvetica 20 ").grid(row=2,column=2,ipady=10)

def updateclick() :
    global searchbox,codebox,namebox,oderid,roombox
    right.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()
    updateframe.grid_rowconfigure((0,1,2,3,4,5,6),weight=1)
    updateframe.grid_columnconfigure((0,1),weight=1)
    updateframe.grid(row=1,column=1,rowspan=2,sticky='news')
    
    Label(updateframe,text="Update product",font="Garamond 26 bold",compound=LEFT,bg='#ffffff').grid(row=0,columnspan=2)
    Label(updateframe,text="product Code : ",bg='#ffffff').grid(row=1,column=0,sticky='e')
    searchbox = Entry(updateframe,bg="#E6E6E6")
    searchbox.grid(row=1,column=1,sticky='w',padx=20)
    Button(updateframe,text="Search").grid(row=1,column=1,ipady=10)

    Label(updateframe,text="product Code : ",bg='#ffffff').grid(row=2,column=0,sticky='e')
    codebox = Entry(updateframe,bg="#E6E6E6")
    codebox.grid(row=2,column=1,sticky='w',padx=20)

    Label(updateframe,text="product Name : ",bg='#ffffff').grid(row=3,column=0,sticky='e')
    namebox = Entry(updateframe,bg="#E6E6E6")
    namebox.grid(row=3,column=1,sticky='w',padx=20)

    Label(updateframe,text="oder : ",bg='#ffffff').grid(row=4,column=0,sticky='e')
    oderid = Entry(updateframe,bg="#E6E6E6")
    oderid.grid(row=4,column=1,sticky='w',padx=20)
    
    Label(updateframe,text="Room : ",bg='#ffffff').grid(row=5,column=0,sticky='e')
    roombox = Entry(updateframe,bg="#E6E6E6")
    roombox.grid(row=5,column=1,sticky='w',padx=20)
    Button(updateframe,text="Update product",width=10,command=updateproduct).grid(row=6,columnspan=2,ipady=10)

def updateproduct() :
    global codebox,namebox,oderid,roombox
    if codebox.get() == "" or namebox.get() == "" or oderid.get() == "" or roombox.get() == "" :
        messagebox.showwarning("Admin: ","Please fullfill all of product data")
        codebox.focus_force()
    else :
        #define sql select command to checking product code exist or not
        sql = "select * from product where product_code=?"
        #execute step
        cursor.execute(sql,[codebox.get()])
        #fetch result
        result = cursor.fetchone()
        if result :
            #define sql select command of product name for duplicating
            sql = "select * from product where product_name=?"
            #execute step
            cursor.execute(sql,[namebox.get()])
            #fetch result
            result = cursor.fetchone()
            if result :
                messagebox.showwarning("Admin : ","Duplicated product name")
                #define sql for updating only oder and room fields
                sql = """ 
                        update product
                        set oder=? , room=?
                        where product_code=?

                """
                #execute step
                cursor.execute(sql,[oderid.get(),roombox.get(),codebox.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update product successfully")
                clearclick()

            else :
                #define sql update command for updating product name, oder and room
                sql = """
                        update product
                        set product_name=?, oder=?, room=?
                        where product_code=?
                """
                #execute step
                cursor.execute(sql,[namebox.get(),oderid.get(),roombox.get(),codebox.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update product successfully")
                clearclick()
        else :
            messagebox.showwarning("Admin: ","product code not found\n Try again.")
            codebox.select_range(0,END)
            codebox.focus_force()


def clearclick() :
    codebox.config(state='normal')
    codebox.delete(0,END)
    namebox.delete(0,END)
    oderid.delete(0,END)
    roombox.delete(0,END)
       
def logoutclick() :
    updateframe.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()
    right.grid_forget()
    top.grid_forget()
    welcomeframe.grid_forget()
    pwdframe.grid_forget()
    loginlayout() 

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
addframe = Frame(welcomeframe,bg='#ffffff')
updateframe = Frame(welcomeframe,bg='#ffffff')
deleteframe = Frame(welcomeframe,bg='#ffffff')
selectoption = StringVar()
usericon = PhotoImage(file='images/Usericon.png').subsample(2,2)
ATCimage = PhotoImage(file='images/ATC3.png')
shoping = PhotoImage(file="images/shoping.png").subsample(2,2)
nonlogo = PhotoImage(file='images/nonlogo.png').subsample(8,8)
case1 = PhotoImage(file='images/case1.png').subsample(4,4)
introshop()
root.mainloop()
cursor.close()
conn.close()


# def addproduct() :
#     if codebox.get() == "" or namebox.get() == "" or oderid.get() == "" or roombox.get() == "" : 
#         messagebox.showwarning("Admin: ","Please fullfill all of product data")
#         codebox.focus_force()
#     else : 
#         #define sql select command of product code or product name for duplicating
#         sql = "select * from product where product_code=? or product_name=?" #เช็คค่าที่ดึงมาว่าซ้ำไหม
#         #execute step
#         cursor.execute(sql,[codebox.get(),namebox.get()]) #หาค่าใน Database 
#         #fetch result
#         result = cursor.fetchone()
#         if result :
#             messagebox.showwarning("Admin: ","product code or name already exist.") #ถ้าเจอซ้ำให้ขึ้นเตือน
#             codebox.select_range(0,END)
#             codebox.focus_force()
#         else :
#             #define insert command for insert a new record into the table
#             sql = "insert into product values (NULL,?,?,?,?)" #บันทึกข้อมูลลง Database  
#             #execute step
#             cursor.execute(sql,[codebox.get(),namebox.get(),oderid.get(),roombox.get()])
#             #commit step
#             conn.commit()
#             messagebox.showinfo("Admin:","Add product successfully")
#             clearclick()

# def searchclick() :
#     sql = "select * from product where product_code=? collate nocase" #ค้นหาข้อมูลใน Database เปลี่ยนตัวแปรทั้งหมด
#     #execute step
#     cursor.execute(sql,[searchbox.get()]) 
#     #fetch result
#     result = cursor.fetchone()
#     if result :
#         codebox.config(state='normal') #อ่านเท่านั้น insert ข้อมูลก่อน
#         codebox.delete(0,END)
#         codebox.insert(0,result[1])
#         codebox.config(state='readonly') #เพิ่มข้อมูลแล้วห้ามแก้ไขต่อ
#         namebox.delete(0,END)
#         namebox.insert(0,result[2])
#         oderid.delete(0,END)
#         oderid.insert(0,result[3])
#         roombox.delete(0,END)
#         roombox.insert(0,result[4])
#     else :
#         messagebox.showwarning("Admin: ","product code not found\n Try again.")
#         searchbox.select_range(0,END)
#         searchbox.focus_force()
#         codebox.config(state='normal')
#         namebox.delete(0,END)
#         oderid.delete(0,END)
#         roombox.delete(0,END)
#         codebox.delete(0,END)
 