import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def connection() :
    global conn,cursor
    conn = sqlite3.connect("database/tew.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1200
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#E98F9B')
    root.title("Week14 Insert/Update/Delete Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,3),weight=1)
    root.rowconfigure((1),weight=4)
    root.columnconfigure((0,3),weight=1)
    root.columnconfigure((1),weight=4)
    return root

def loginlayout() :
    ############################################### Window Update Login ################################################
    global userentry,pwdentry,cfpassword
    loginframe.rowconfigure((0,1,2,3,4),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

    Label(loginframe,text="Account Login",font="Garamond 26 bold",compound=LEFT,image=img1,bg='#FFD8D3',fg='#FFFFFF').grid(row=0,columnspan=2)
    Label(loginframe,text="Username : ",bg='#FFD8D3',fg='#FFFFFF',padx=20).grid(row=1,column=0,sticky='e')

    userentry = Entry(loginframe,bg='#FFFFFF',width=20)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#FFFFFF',width=20,show='*')
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    cfpassword = Entry(loginframe,bg='#FFFFFF',width=20,show='*')
    cfpassword.grid(row=3,column=1,sticky='w',padx=20)

    Label(loginframe,text="Password  : ",bg='#FFD8D3',fg='#FFFFFF',padx=20).grid(row=2,column=0,sticky='e')
    Label(loginframe,text="Confirm Password  : ",bg='#FFD8D3',fg='#FFFFFF',padx=20).grid(row=3,column=0,sticky='e')


    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userentry.get(),pwdentry.get(),cfpassword.get()),bg='#ffffff',fg='#000000').grid(row=4,column=1,pady=20,ipady=15,sticky='e',padx=40)
    Button(loginframe,text="Exit",width=10,command=root.quit,bg='#ffffff',fg='#000000').grid(row=4,column=0,pady=10,ipady=15,sticky='w',padx=45)

def loginclick(user,pwd,cfpassword) :
    global result
    if user == "" or pwd == "" or cfpassword == "" : 
        messagebox.showwarning("Admin : ","Please enter a username or password or Confirm Password")
        userentry.focus_force()
    else :
        sql = "select * from student where username=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            sql = "select * from student where username=? and password=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if pwd == cfpassword :
                messagebox.showinfo("Admin : ","Login Successfully.")
                welcomepage(result)
            else :
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpassword.focus_force()
                # user.selection_range(0,END)
                # pwd.selection_range(0,END)
                # cfpassword.selection_range(0,END)
                # cfpassword.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            userentry.selection_range(0,END)
            userentry.focus_force()

def welcomepage(result) :
    global top,left,right,bottom,center
    loginframe.grid_forget()
    pwdframe.grid_forget()
    updateframe.grid_forget()
    welcomeframe['bg'] = "#FFD8D3"

    #ROW
    welcomeframe.grid_rowconfigure((0),weight=1)
    welcomeframe.grid_rowconfigure((1),weight=3)
    welcomeframe.grid_rowconfigure((2),weight=1)

    #COLUMN
    welcomeframe.grid_columnconfigure((0),weight=1)
    welcomeframe.grid_columnconfigure((1),weight=3)
    welcomeframe.grid_columnconfigure((2),weight=1)

    #Frame
    welcomeframe.grid(row=0,column=0,columnspan=6,rowspan=6,sticky='news')

    #TOP FRAME
    top = Frame(welcomeframe,bg='#FFD8D3')
    # top.grid_rowconfigure((0,1),weight=0)
    top.grid_columnconfigure((0,1),weight=1)
    top.grid(row=0,columnspan=3,sticky='news')

    #LEFT
    left = Frame(welcomeframe,bg='#E98F9B')
    left.grid_rowconfigure((0,1),weight=1)
    left.grid_columnconfigure(0,weight=1)
    left.grid(row=1,column=0,sticky='news')
    
    #CENTER
    center = Frame(welcomeframe,bg='#FDDEDA')
    center.grid_rowconfigure((0,1),weight=1)
    center.grid_columnconfigure((0,1),weight=1)
    center.grid(row=1,column=1,sticky='news')

    #Right
    right = Frame(welcomeframe,bg='#E98F9B')
    right.grid_rowconfigure((0,1),weight=1)
    right.grid_columnconfigure((0),weight=1)
    right.grid(row=1,column=2,sticky='news')

    #BOTTOM
    bottom = Frame(welcomeframe,bg='#FD6994')
    bottom.grid_rowconfigure((0),weight=1)
    bottom.grid_columnconfigure((0,1),weight=1)
    bottom.grid(row=2,column=0,columnspan=3,sticky='news')

    #create widgets
    Label(top,image=img3,bg='#FFD8D3',text="Student ID : "+str(result[0])+"\n"+"Name : "+result[1]+" "+result[2],compound=LEFT).grid(row=0,column=0,columnspan=2,rowspan=2)
    Button(left,text="Add Flower",width=10,command=addclick,bg='#ffffff',fg='#000000').grid(row=0,column=0,ipady=10,ipadx=20,sticky=S,pady=20)
    Button(left,text="Update Flower",width=10,command=updateclick,bg='#ffffff',fg='#000000').grid(row=1,column=0,ipady=10,ipadx=20,sticky=N,pady=20)
    Button(right,text="Delete Flower",width=10,bg='#ffffff',fg='#000000',command=deleteclick).grid(row=1,column=0,ipady=10,ipadx=20,sticky=N,pady=20)
    Button(bottom,text="Logout",width=10,bg='#ffffff',fg='#000000',command=logoutclick).grid(row=0,column=0,ipady=10,ipadx=10,sticky=E,padx=20)
    Button(bottom,text="Exit",width=10,command=exit,bg='#ffffff',fg='#000000').grid(row=0,column=1,ipady=10,ipadx=10,sticky=W,padx=20)
    Label(center,image=img2,bg='#FDDEDA').grid(row=0,column=0,columnspan=2,rowspan=2)

    # Button(left,text="Add Course",width=10,command=addclick).grid(row=1,ipady=10)
    # Button(left,text="Update Course",width=10,command=updateclick).grid(row=2,ipady=10)
    # Button(left,text="Delete Course",width=10,command=deleteclick).grid(row=3,ipady=10)
    # Button(left,text="Logout",width=10,command=logoutclick).grid(row=4,ipady=10)
    # Label(right,image=img4,bg='#BDDDE4').grid(row=0)

def addclick() :
    print("Add Click")
    global addframe
    global flowerid,flowername,flowerprice,flowervalue

    center.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()

    addframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    addframe.grid_columnconfigure((0,1),weight=1)
    addframe.grid(row=1,column=1,sticky='news')

    Label(addframe,text="Add Flower",font="Garamond 26 bold",compound=LEFT,bg='#FDDEDA',image=img1).grid(row=0,columnspan=2)
    Label(addframe,text="Flower ID : ",bg='#FDDEDA').grid(row=1,column=0,sticky='e')
    flowerid = Entry(addframe,bg="#FFFFFF")
    flowerid.grid(row=1,column=1,sticky='w',padx=20)
    Label(addframe,text="Flower Name : ",bg='#FDDEDA').grid(row=2,column=0,sticky='e')
    flowername = Entry(addframe,bg="#FFFFFF")
    flowername.grid(row=2,column=1,sticky='w',padx=20)
    Label(addframe,text="Flower Price :",bg='#FDDEDA').grid(row=3,column=0,sticky='e')
    flowerprice = Entry(addframe,bg="#FFFFFF")
    flowerprice.grid(row=3,column=1,sticky='w',padx=20)
    Label(addframe,text="Price Value:",bg='#FDDEDA').grid(row=4,column=0,sticky='e')
    flowervalue = Entry(addframe,bg="#FFFFFF")
    flowervalue.grid(row=4,column=1,sticky='w',padx=20)
    Button(addframe,text="Add",width=10,command=addflower,bg='#ffffff',fg='#000000').grid(row=5,columnspan=2,ipady=10)
    
#  ###############################################เปลี่ยนข้อมูลตัวแปร################################################
# flowerid.get() == "" or flowername.get() == "" or flowerprice.get() == "" or flowervalue.get() == "" 
# codebox.get() == "" or namebox.get() == "" or daybox.get() == "" or roombox.get() == "" : 
def addflower() :
    print("Add Flower")
    if flowerid.get() == "" or flowername.get() == "" or flowerprice.get() == "" or flowervalue.get() == "" : 
        messagebox.showwarning("Admin: ","Please fullfill all of flower data")
        flowerid.focus_force()
    else : 
        #define sql select command of course code or course name for duplicating
        sql = "select * from flower where flowerid=? or flowername=?" #เช็คค่าที่ดึงมาว่าซ้ำไหม
        #execute step
        cursor.execute(sql,[flowerid.get(),flowername.get()]) #หาค่าใน Database 
        #fetch result
        result = cursor.fetchone()
        if result :
            messagebox.showwarning("Admin: ","flowerid or flowername already exist.") #ถ้าเจอซ้ำให้ขึ้นเตือน
            flowerid.select_range(0,END)
            flowerid.focus_force()
        else :
            #define insert command for insert a new record into the table
            sql = "insert into flower values (NULL,?,?,?,?)" #บันทึกข้อมูลลง Database  
            #execute step
            cursor.execute(sql,[flowerid.get(),flowername.get(),flowerprice.get(),flowervalue.get()])
            #commit step
            conn.commit()
            messagebox.showinfo("Admin:","Add flower successfully")
            clearclick()

def searchclick() :
    print("Search Click")
    sql = "select * from flower where flowerid=? collate nocase" #ค้นหาข้อมูลใน Database เปลี่ยนตัวแปรทั้งหมด
    #execute step
    cursor.execute(sql,[searchbox.get()]) 
    #fetch result
    result = cursor.fetchone()
    if result :
        flowerid.config(state='normal') #อ่านเท่านั้น insert ข้อมูลก่อน
        flowerid.delete(0,END)
        flowerid.insert(0,result[1])
        flowerid.config(state='readonly') #เพิ่มข้อมูลแล้วห้ามแก้ไขต่อ
        flowername.delete(0,END)
        flowername.insert(0,result[2])
        flowerprice.delete(0,END)
        flowerprice.insert(0,result[3])
        flowervalue.delete(0,END)
        flowervalue.insert(0,result[4])
    else :
        messagebox.showwarning("Admin: ","Flower ID not found\n Try again.")
        searchbox.select_range(0,END)
        searchbox.focus_force()
        flowerid.config(state='normal')
        flowername.delete(0,END)
        flowerprice.delete(0,END)
        flowervalue.delete(0,END)
        flowerid.delete(0,END)
 
def updateclick() :
    print("Update Click")
    global searchbox,flowerid,flowername,flowerprice,flowervalue
    center.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()
    updateframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    updateframe.grid_columnconfigure((0,1),weight=1)
    updateframe.grid(row=1,column=1,sticky='news')
    Label(updateframe,text="Update Flower",font="Garamond 26 bold",image=img1,compound=LEFT,bg='#FDDEDA').grid(row=0,columnspan=2)
    Label(updateframe,text="Serch Flower : ",bg='#FDDEDA').grid(row=1,column=0,sticky='e')
    searchbox = Entry(updateframe,bg="#FFFFFF")
    searchbox.grid(row=1,column=1,sticky='w',padx=20)
    Button(updateframe,text="Search",command=searchclick,bg='#E98F9B',fg='#ffffff').grid(row=1,column=1,ipady=5,ipadx=10)
    Label(updateframe,text="Flower Name : ",bg='#FDDEDA').grid(row=2,column=0,sticky='e')
    flowername = Entry(updateframe,bg="#FFFFFF")
    flowername.grid(row=2,column=1,sticky='w',padx=20)
    Label(updateframe,text="Price Flower : ",bg='#FDDEDA').grid(row=3,column=0,sticky='e')
    flowerprice = Entry(updateframe,bg="#FFFFFF")
    flowerprice.grid(row=3,column=1,sticky='w',padx=20)
    Label(updateframe,text="Value Flower : ",bg='#FDDEDA').grid(row=4,column=0,sticky='e')
    flowervalue = Entry(updateframe,bg="#FFFFFF")
    flowervalue.grid(row=4,column=1,sticky='w',padx=20)
    Button(updateframe,text="Update Flower",width=10,command=updateflower,bg='#ffffff',fg='#000000').grid(row=5,columnspan=2,ipady=5,ipadx=15)

def updateflower() :
    print("Update Flower")
    global  searchbox,flowerid,flowername,flowerprice,flowervalue
    if flowerid.get() == "" or flowername.get() == "" or flowerprice.get() == "" or flowervalue.get() == "" :
        # codebox.get() == "" or namebox.get() == "" or daybox.get() == "" or roombox.get() == "" : 
        messagebox.showwarning("Admin: ","Please fullfill all of Flower data")
        flowerid.focus_force()
    else :
        #define sql select command to checking course code exist or not
        sql = "select * from flower where flowerid=?"
        #execute step
        cursor.execute(sql,[flowerid.get()])
        #fetch result
        result = cursor.fetchone()
        if result :
            #define sql select command of course name for duplicating
            sql = "select * from flower where flowername=?"
            #execute step
            cursor.execute(sql,[flowername.get()])
            #fetch result
            result = cursor.fetchone()
            if result :
                messagebox.showwarning("Admin : ","Duplicated Flower name")
                #define sql for updating only day and room fields
                sql = """ 
                        update flower
                        set flowerprice=? , flowervalue=?
                        where flowerid=?

                """
                #execute step
                cursor.execute(sql,[flowerprice.get(),flowervalue.get(),flowerid.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update Flower successfully")
                clearclick()

            else :
                #define sql update command for updating course name, day and room
                sql = """
                        update flower
                        set flowername=?, flowerprice=?, flowervalue=?
                        where flowerid=?
                """
                #execute step
                cursor.execute(sql,[flowername.get(),flowerprice.get(),flowervalue.get(),flowerid.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update Flower successfully")
                clearclick()
        else :
            messagebox.showwarning("Admin: ","Flower ID not found\n Try again.")
            flowerid.select_range(0,END)
            flowerid.focus_force()


def deleteclick() :
    print("Delete Click")
    global searchbox,flowerid,flowername,flowerprice,flowervalue
    updateframe.grid_forget()
    addframe.grid_forget()
    center.grid_forget()
    deleteframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    deleteframe.grid_columnconfigure((0,1),weight=1)
    deleteframe.grid(row=1,column=1,sticky='news')
    Label(deleteframe,text="Delete Flower",font="Garamond 26 bold",compound=LEFT,bg='#FDDEDA',image=img1).grid(row=0,columnspan=2)
    Label(deleteframe,text="Serch Flower : ",bg='#FDDEDA').grid(row=1,column=0,sticky='e')
    searchbox = Entry(deleteframe,bg="#ffffff")
    searchbox.grid(row=1,column=1,sticky='w',padx=20)
    Button(deleteframe,text="Search",command=searchclick,bg='#E98F9B',fg='#ffffff').grid(row=1,column=1,ipady=5,ipadx=10)
    Label(deleteframe,text="Flower Name : ",bg='#FDDEDA').grid(row=2,column=0,sticky='e')
    flowername = Entry(deleteframe,bg="#FFFFFF")
    flowername.grid(row=2,column=1,sticky='w',padx=20)
    Label(deleteframe,text="Price Flower : ",bg='#FDDEDA').grid(row=3,column=0,sticky='e')
    flowerprice = Entry(deleteframe,bg="#FFFFFF")
    flowerprice.grid(row=3,column=1,sticky='w',padx=20)
    Label(deleteframe,text="Value Flower : ",bg='#FDDEDA').grid(row=4,column=0,sticky='e')
    flowervalue = Entry(deleteframe,bg="#FFFFFF")
    flowervalue.grid(row=4,column=1,sticky='w',padx=20)
    Button(deleteframe,text="Delete Flower",width=10,command=deleteflower,bg='#ffffff',fg='#000000').grid(row=5,columnspan=2,ipady=10)

def deleteflower() :
    if flowerid.get() == "":
        messagebox.showwarning("Admin: ","Please fullfill all of flower data")
        flowerid.focus_force()
    else :
        cf = messagebox.askquestion("Admin : ","Confirm to delete (Yes/No)")
        if cf == 'yes' :
            #define sql command or sql statement for deletion
            sql = "delete from flower where flowerid=?"
            #execute sql using cursor
            cursor.execute(sql,[flowerid.get()])
            #confirm/save data updated using commit() method
            conn.commit()
            messagebox.showinfo("Admin : ","Delete Successfully")
            clearclick()

def clearclick() :
    flowerid.config(state='normal')
    flowerid.delete(0,END)
    flowername.delete(0,END)
    flowerprice.delete(0,END)
    flowervalue.delete(0,END)
       
def logoutclick() :
    updateframe.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()
    center.grid_forget()
    top.grid_forget()
    bottom.grid_forget()
    left.grid_forget()
    welcomeframe.grid_forget()
    pwdframe.grid_forget()
    loginlayout() 

connection()
root = mainwindow()
loginframe = Frame(root,bg='#FFD8D3')
welcomeframe = Frame(root,bg='#FFD8D3')
updateframe = Frame(root,bg="#FDDEDA")
pwdframe = Frame(root,bg='#FDDEDA')
addframe = Frame(welcomeframe,bg='#FDDEDA')
updateframe = Frame(welcomeframe,bg='#FDDEDA')
deleteframe = Frame(welcomeframe,bg='#FDDEDA')
searchframe = Frame(welcomeframe,bg='#FDDEDA')
upatepage  = Frame(welcomeframe,bg='#FDDEDA')
selectoption = StringVar()
title = ["Course Code:","Course Name:","Day:","Room:"]
img1 = PhotoImage(file='image/rose.png').subsample(2,2)
img2 = PhotoImage(file='image/lily1.png').subsample(7,7)
img3 = PhotoImage(file="image/profile.png").subsample(4,4)
img4 = PhotoImage(file='image/search.png')
# img5 = PhotoImage(file='images/books.png').subsample(6,6)
loginlayout()
root.mainloop()
cursor.close()
conn.close()