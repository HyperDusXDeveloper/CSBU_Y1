import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def connection() :
    global conn,cursor
    conn = sqlite3.connect("dbset7/finalset7.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1100
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#EEECE8')
    root.title("finalExam")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,3),weight=1)
    root.rowconfigure((1,2),weight=2)
    root.columnconfigure((0,3),weight=1)
    root.columnconfigure((1,2),weight=2)
    return root

def loginlayout() :
    ############################################### Window Update Login ################################################
    global userentry,pwdentry

    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0),weight=1)
    loginframe.grid(row=0,column=0,columnspan=2,rowspan=4,sticky='news')


    Label(loginframe,text="Username : ",bg='#D5D5D5',fg='#e4fbff',padx=20).grid(row=0,column=0,sticky='S')
    userentry = Entry(loginframe,bg='#e4fbff',width=20)
    userentry.grid(row=1,column=0,sticky='N',padx=20)

    Label(loginframe,text="Password  : ",bg='#D5D5D5',fg='#e4fbff',padx=20).grid(row=2,column=0,sticky='S')
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,show='*')
    pwdentry.grid(row=3,column=0,sticky='N',padx=20)

    
    #Label(loginframe,text="Student ID  : ",bg='#D5D5D5',fg='#e4fbff',padx=20).grid(row=3,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userentry.get(),pwdentry.get())).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=40)

    # Label(loginframe,image=img1,padx=20).grid(row=1,column=3,rowspan=2,sticky='e')
def loginclick(user,pwd) :
    global result
    if user == "" or pwd == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        userentry.focus_force()
    else :
        sql = "select * from login where user=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            sql = "select * from login where user=? and pwd=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Admin : ","Login Successfully.")
                welcomepage(result)
            else :
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                pwdentry.selection_range(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            userentry.selection_range(0,END)
            userentry.focus_force()

def welcomepage(result) :
    global topbottom,topright,left
    loginframe.grid_forget()
    pwdframe.grid_forget()
    updateframe.grid_forget()
    welcomeframe['bg'] = "#FCC2FC"

    #ROW
    welcomeframe.grid_rowconfigure((0),weight=1)
    welcomeframe.grid_rowconfigure((1),weight=2)

    #COLUMN
    welcomeframe.grid_columnconfigure((0),weight=5)
    welcomeframe.grid_columnconfigure((1),weight=1)

    #Frame
    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')


    left = Frame(welcomeframe,bg='#EEECE8')
    left.grid_rowconfigure((0,1),weight=1)
    left.grid_columnconfigure(0,weight=1)
    left.grid(row=0,column=0,rowspan=3,sticky='news')

    topright = Frame(welcomeframe,bg='#55ABFD')
    topright.grid_rowconfigure((0,1,2),weight=1)
    topright.grid_columnconfigure((0),weight=1)
    topright.grid(row=0,column=1,columnspan=2,sticky='news')
    
    topbottom = Frame(welcomeframe,bg='#A4D7FE')
    topbottom.grid_rowconfigure((0,1,2),weight=1)
    topbottom.grid_columnconfigure(0,weight=1)
    topbottom.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

    #create widgets

    Label(topright,bg='#55ABFD',text="Welcome "+"\n"+str(result[0])+"\n",compound=TOP,font="Garamond 26 bold",image=img2).grid(row=0,column=0)
    Button(topbottom,text="Add Content",width=12,command=addclick).grid(row=0,column=0,ipady=10)
    Button(topbottom,text="Search",width=12,command=updateclick).grid(row=1,column=0,ipady=10)
    Button(topbottom,text="Logout",width=12,command=logoutclick).grid(row=2,column=0,ipady=10,sticky='S',pady=15)
    Label(topbottom,bg='#BDDDE4').grid(row=0,column=0)

def addclick() :
    global addframe
    global email,first,last,mobie,other

    left.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()

    addframe.grid_rowconfigure((0,1,2,3,4,5,6),weight=1)
    addframe.grid_columnconfigure((0,1),weight=1)
    addframe.grid(row=0,column=0,rowspan=3,sticky='news')

    Label(addframe,text="Add New Content ",font="Garamond 35 bold",compound=LEFT,bg='#BDDDE4',fg='red').grid(row=0,columnspan=2)

    Label(addframe,text="Email : ",bg='#BDDDE4').grid(row=1,column=0,padx=40)
    email = Entry(addframe,bg="#ffffff")
    email.grid(row=1,column=1,sticky='w')

    Label(addframe,text="firstname : ",bg='#BDDDE4').grid(row=2,column=0,padx=40)
    first = Entry(addframe,bg="#ffffff")
    first.grid(row=2,column=1,sticky='w')

    Label(addframe,text="Lastname : ",bg='#BDDDE4').grid(row=3,column=0,padx=40)
    last = Entry(addframe,bg="#fffffF")
    last.grid(row=3,column=1,sticky='w')

    Label(addframe,text="Mobie : ",bg='#BDDDE4').grid(row=4,column=0,padx=40)
    mobie = Entry(addframe,bg="#ffffff")
    mobie.grid(row=4,column=1,sticky='w')

    Label(addframe,text="Other ",bg='#BDDDE4').grid(row=5,column=0,padx=40)
    other = Entry(addframe,bg="#ffffff")
    other.grid(row=5,column=1,sticky='w')

    Button(addframe,text="Add",width=10,command=addfriend_1670700044).grid(row=6,columnspan=3,ipady=10)
    
 ###############################################เปลี่ยนข้อมูลตัวแปร################################################

def addfriend_1670700044() :
    if email.get() == "" or first.get() == "" or last.get() == "" or mobie.get() == "" or other.get() == "" : 
        messagebox.showwarning("Admin: ","Please fullfill all of friend_1670700044 data")
        email.focus_force()
    else : 
        #define sql select command of friend_1670700044 code or friend_1670700044 name for duplicating
        sql = "select * from friend_1670700044 where email=? or first=?" #เช็คค่าที่ดึงมาว่าซ้ำไหม
        #execute step
        cursor.execute(sql,[email.get(),first.get()]) #หาค่าใน Database 
        #fetch result
        result = cursor.fetchone()
        if result :
            messagebox.showwarning("Admin: ","friend_1670700044  or name already exist.") #ถ้าเจอซ้ำให้ขึ้นเตือน
            email.select_range(0,END)
            email.focus_force()
        else :
            #define insert command for insert a new record into the table
            sql = "insert into friend_1670700044 values (?,?,?,?,?)" #บันทึกข้อมูลลง Database  
            #execute step
            cursor.execute(sql,[email.get(),first.get(),last.get(),mobie.get(),other.get()])
            #commit step
            conn.commit()
            messagebox.showinfo("Admin:","Add friend_1670700044 successfully")
            clearclick()

def searchclick() :
    global email,first,last,mobie,other

    Label(updateframe,text="Email : ",bg='#BDDDE4').grid(row=2,column=0,sticky='e')
    email = Entry(updateframe,bg="#DAF5FF")
    email.grid(row=2,column=1,sticky='w',padx=20)

    Label(updateframe,text="firstname :",bg='#BDDDE4').grid(row=3,column=0,sticky='e')
    first = Entry(updateframe,bg="#DAF5FF")
    first.grid(row=3,column=1,sticky='w',padx=20)

    Label(updateframe,text="Lastname :",bg='#BDDDE4').grid(row=4,column=0,sticky='e')
    last = Entry(updateframe,bg="#DAF5FF")
    last.grid(row=4,column=1,sticky='w',padx=20)
    
    Label(updateframe,text="Mobie :",bg='#BDDDE4').grid(row=5,column=0,sticky='e')
    mobie = Entry(updateframe,bg="#DAF5FF")
    mobie.grid(row=5,column=1,sticky='w',padx=20)

    Label(updateframe,text="Other ",bg='#BDDDE4').grid(row=6,column=0,sticky='e')
    other = Entry(updateframe,bg="#DAF5FF")
    other.grid(row=6,column=1,sticky='w',padx=20)
    
    Button(updateframe,text="Update Content",width=20,command=updatefriend_1670700044).grid(row=7,columnspan=2,column=0,ipady=10)

    sql = "select * from friend_1670700044 where email=? collate nocase" #ค้นหาข้อมูลใน Database เปลี่ยนตัวแปรทั้งหมด
    #execute step
    cursor.execute(sql,[searchbox.get()]) 
    #fetch result
    result = cursor.fetchone()
    if result :
        email.config(state='normal') #อ่านเท่านั้น insert ข้อมูลก่อน
        email.delete(0,END)
        email.insert(0,result[0])
        email.config(state='readonly') #เพิ่มข้อมูลแล้วห้ามแก้ไขต่อ
        first.delete(0,END)
        first.insert(0,result[1])
        last.delete(0,END)
        last.insert(0,result[2])
        mobie.delete(0,END)
        mobie.insert(0,result[3])
        other.delete(0,END)
        other.insert(0,result[4])
    else :
        messagebox.showwarning("Admin: ","friend_1670700044 code not found\n Try again.")
        searchbox.select_range(0,END)
        searchbox.focus_force()
        email.config(state='normal')
        first.delete(0,END)
        last.delete(0,END)
        mobie.delete(0,END)
        other.delete(0,END)
        email.delete(0,END)


def updateclick() :
    global searchbox,email,first,last,other

    left.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()

    updateframe.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    updateframe.grid_columnconfigure((0,1),weight=1)
    updateframe.grid(row=0,column=0,rowspan=3,sticky='news')

    Label(updateframe,text="Search friend_1670700044",font="Garamond 26 bold",compound=LEFT,bg='#BDDDE4').grid(row=0,columnspan=2)
    Label(updateframe,text="friend_1670700044 Code : ",bg='#BDDDE4').grid(row=1,column=0,sticky='e')
    searchbox = Entry(updateframe,bg="#DAF5FF")
    searchbox.grid(row=1,column=1,sticky='w',padx=20)
    Button(updateframe,text="Search",command=searchclick).grid(row=1,column=1,ipady=10)

def updatefriend_1670700044() :
    global email,first,last,other
    if email.get() == "" or first.get() == "" or last.get() == "" or other.get() == "" :
        messagebox.showwarning("Admin: ","Please fullfill all of friend_1670700044 data")
        email.focus_force()
    else :
        #define sql select command to checking friend_1670700044 code exist or not
        sql = "select * from friend_1670700044 where email=?"
        #execute step
        cursor.execute(sql,[email.get()])
        #fetch result
        result = cursor.fetchone()
        if result :
            #define sql select command of friend_1670700044 name for duplicating
            sql = "select * from friend_1670700044 where first=?"
            #execute step
            cursor.execute(sql,[first.get()])
            #fetch result
            result = cursor.fetchone()
            if result :
                messagebox.showwarning("Admin : ","Duplicated friend_1670700044 name")
                #define sql for updating only mobie and other fields
                sql = """ 
                        update friend_1670700044
                        set mobie=? , other=?
                        where email=?

                """
                #execute step
                cursor.execute([first.get(),last.get(),mobie.get(),other.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update friend_1670700044 successfully")
                clearclick()

            else :
                #define sql update command for updating friend_1670700044 name, mobie and other
                sql = """
                        update friend_1670700044
                        set first=?, mobie=?, other=?
                        where email=?
                """
                #execute step
                cursor.execute(sql,[first.get(),last.get(),mobie.get(),other.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update friend_1670700044 successfully")
                clearclick()
        else :
            messagebox.showwarning("Admin: ","friend_1670700044 code not found\n Try again.")
            email.select_range(0,END)
            email.focus_force()


def clearclick() :
    email.config(state='normal')
    email.delete(0,END)
    first.delete(0,END)
    last.delete(0,END)
    other.delete(0,END)
       
def logoutclick() :
    cf = messagebox.askquestion("Admin : ","Confirm to Logout (Yes/No)")
    if cf == 'yes' :
        messagebox.showinfo("Admin : ","Back To Login ")
        updateframe.grid_forget()
        addframe.grid_forget()
        deleteframe.grid_forget()
        left.grid_forget()
        topbottom.grid_forget()
        topbottom.grid_forget()
        topright.grid_forget()
        welcomeframe.grid_forget()
        pwdframe.grid_forget()
        loginlayout() 

connection()
root = mainwindow()
loginframe = Frame(root,bg='#D5D5D5')
welcomeframe = Frame(root,bg='#EEECE8')
updateframe = Frame(root,bg="#EEECE8")
updateframedown = Frame(root,bg="#EEECE8")
pwdframe = Frame(root,bg='#28b5b5')
addframe = Frame(welcomeframe,bg='#EEECE8')
updateframe = Frame(welcomeframe,bg='#EEECE8')
deleteframe = Frame(welcomeframe,bg='#EEECE8')
img1 = PhotoImage(file='imageset7/phone-book.png').subsample(2,2)
img2 = PhotoImage(file='imageset7/profile.png')
# img3 = PhotoImage(file="image/login.png").subsample(6,6)
# img4 = PhotoImage(file='image/books.png')
# img5 = PhotoImage(file='image/books.png').subsample(6,6)
loginlayout()
root.mainloop()
cursor.close()
conn.close()