from tkinter import *
from tkinter import messagebox
import sqlite3

def connection() :
    print("Connection")
    conn = sqlite3.connect("db/db_week10.db")
    cursor = conn.cursor()
    return(conn,cursor)

def mainwindow() :  
    master = Tk()
    w = 1000
    h = 800
    x = master.winfo_screenwidth()/2 - w/2
    y = master.winfo_screenheight()/2 - h/2
    master.geometry("%dx%d+%d+%d"%(w,h,x,y))
    master.config(bg='#EDDFE0')
    master.title("Login Application : ")
    master.option_add('*font',"tahoma 22")
    master.grid_rowconfigure((0,1,2),weight=1)
    master.grid_columnconfigure((0,1,2),weight=1)
    # master.grid_columnconfigure((1),weight=4)
    return(master)
def layout() :
    loginpage.grid(rowspan=3,columnspan=3,column=0,row=0,sticky='news')
    loginpage.rowconfigure((0,1,2),weight=1)
    loginpage.columnconfigure((0,1,2),weight=1)

    infor.grid(row=0,rowspan=3,column=0,columnspan=3,sticky='news')
    infor.grid_rowconfigure(0,weight=1)
    infor.grid_columnconfigure(0,weight=1)


def loginwindow() :
    global userentry,pwdentry
    centerc.grid(row=1,column=1,sticky='news')
    centerc.rowconfigure(0,weight=2)
    centerc.columnconfigure(0,weight=1)
    centerc.columnconfigure(1,weight=2)

    Label(centerc,image=user,bg='#F3C2CB').grid(row=0,column=0,sticky="EN",pady=90,padx=20) #,sticky='news'
    
    Label(centerc,text="Username",bg='#F3C2CB').grid(row=0,column=1,sticky="WN",pady=80)

    userentry = Entry(centerc,textvariable=userinfo)
    userentry.grid(row=0,column=1,sticky="WN",pady=120)

    Label(centerc,text="Password",bg='#F3C2CB').grid(row=0,column=1,sticky="WN",pady=160)

    pwdentry = Entry(centerc,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=0,column=1,sticky="WN",pady=200)

    Button(centerc,text="Login",width=5,command=loginclick).grid(row=0,column=1,sticky="SW",pady=170,padx=70)
   
def loginclick() :
    print("Login Click")
    if userinfo.get() == "" :
        messagebox.showwarning("Unauthorized","Please enter username")
        userentry.focus_force()
    elif pwdinfo.get() == "" :
        messagebox.showwarning("Unauthorized","Please enter password")
        pwdentry.focus_force()
    else :
        sql = "select * from students where username=?"             
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            sql = "select * from students where username=? and password=?"
            cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Unauthorized","Login Successful")
                welcomepage((int(result[0])),result[1],result[2],(int(result[3])),(int(result[4])))
                # welcomepage(result[0],result[1],result[2],result[3],result[4]) std_id,first_name,last_name,midterm,final
            else :
                messagebox.showwarning("Unauthorized","Invalid Password")
                pwdentry.selection_range(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Unauthorized","Username or Password invalid.")
            userentry.selection_range(0,END)
            userentry.focus_force()

def welcomepage(id,name,name2,midterm,final) :
    # print(id,name,name2,midterm,final)
    score = midterm + final
    # print(f"Score = {score}")
    centerc.grid_forget()
    loginpage.grid_forget()

    welcome.grid(rowspan=3,columnspan=3,column=0,row=0,sticky='news')
    welcome.grid_rowconfigure((0,2),weight=1)
    welcome.grid_rowconfigure((1),weight=2)
    welcome.grid_columnconfigure((0,2),weight=1)
    welcome.grid_columnconfigure(1,weight=2)

    Label(welcome,image=user,bg='#B8D7E4').grid(row=0,column=0,columnspan=3,sticky="N",pady=20)
    Label(welcome,text=f"Student ID                          {id}",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=200)
    Label(welcome,text=f"Name                                 {name} {name2}",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=250)
    Label(welcome,text=f"Score                                 {score}",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=300)
    if score >= 80 :
        Label(welcome,text=f"Grade                                 A",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=350)
    elif score >= 70 :
        Label(welcome,text=f"Grade                                 B",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=350)
    elif score >= 60 :
        Label(welcome,text=f"Grade                                 C",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=350)
    elif score >= 50 :
        Label(welcome,text=f"Grade                                 D",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=350)
    elif score < 50 :
        Label(welcome,text=f"Grade                                 F",bg='#B8D7E4').grid(row=0 ,rowspan=2,column=0,columnspan=3,sticky=NW,padx=120,pady=350)
    Button(welcome,text="Log Out ",width=10,command=backtologin).grid(row=1,column=1,sticky=S,pady=30)
    
    # Button(welcome,text="log Out",command=backtologin,bg='#E4E0E1',width=20).grid(row=2,column=1,ipady=10)
    # nametest = cursor.fetchall()
    # nametest = nametest[1]
    # print(f"Test print {name}")
    # sql = "select * from students where std_id=? and first_name=? and last_name and midterm and final"
    # cursor.execute(sql,[std_id.get(),password.get(),name.get()])

def backtologin() :
    infor.grid_forget()
    welcome.grid_forget()
    loginpage.grid(rowspan=3,columnspan=3,column=0,row=0,sticky='news')
    centerc.grid(row=1,column=1,sticky='news')
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    userentry.focus_force()

#main
#call connection function
conn,cursor = connection()
master = mainwindow()
user = PhotoImage(file="images/User.png").subsample(3,3)
infor = Frame(master,bg='#B8D7E4')
welcome = Frame(master,bg='#B8D7E4')
loginpage = Frame(master,bg='#F3C2CB')
centerc = Frame(master,bg='#F3C2CB')
userinfo = StringVar()
pwdinfo = StringVar()
layout()
loginwindow()
master.mainloop()
cursor.close()
conn.close()
# End of w9_act1.py