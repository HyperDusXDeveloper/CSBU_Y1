from tkinter import *

def createwindow() : #สร้างหน้าต่าง
    master = Tk()
    master.wm_geometry('1500x900')
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=3)
    master.grid_columnconfigure(0,weight=2)
    master.grid_columnconfigure(1,weight=1)
    master.option_add('*font','Garamond 20')
    return(master)

def layout(master): #
    top = Frame(master,bg='#D9EAFD')
    top.grid(row=0,columnspan=2,sticky='news')


    left = Frame(master,bg='#D1F4F4')
    left.grid(row=1,column=0,sticky='news',padx=10 , pady=15)
    # left.grid_rowconfigure((0,1),weight=1)
    # left.grid_columnconfigure((0),weight=1)
    # left.grid_columnconfigure((1),weight=3)

    right = Frame(master,bg='#EFB036')  
    right.grid(row=1,column=1,sticky='news',padx=10 , pady=15) 
    right.grid_rowconfigure((0,1),weight=1)
    right.grid_columnconfigure((0,1),weight=1)

    bottom = Frame(master,bg='#26355D')
    bottom.grid(row=2,columnspan=2,sticky='news')
    bottom.grid_rowconfigure((0),weight=1)
    bottom.grid_columnconfigure((0,1,2,3),weight=1)

    return(top,left,right,bottom)

def widgets(top,left,right,bottom) :
    #TOP
    heading = Label(top,text="Dashboard DIY By Natchanon Saileamonpiwat ",fg='Black',font=('comic sans ms',25,'bold'),bg="#D9EAFD")
    heading.pack(pady=15)

    #LEFT
    widgetsLeftIMG1 = Label(left,image=Profile,bg='#D1F4F4').place(x=0 , y=0)
    # widgetsLeftIMG1.grid(row=0,column=0,sticky='news')

    leftname = Label(left,text="Name : Natchanon Saileamonpiwat ",fg='Black',font=('comic sans ms',25,'bold'),bg="#D1F4F4").place(x=300,y=60)
    leftname = Label(left)

    leftcollegian = Label(left,text="collegian",fg='Black',font=('comic sans ms',25,'bold'),bg="#D1F4F4").place(x=300,y=120)
    # leftcollegian.grid(row=0,column=1,sticky='w',rowspan=2)

    lefttech = Label(left,text="information technorogy ",fg='Black',font=('comic sans ms',25,'bold'),bg="#D1F4F4").place(x=300,y=180)
    # lefttech.grid(row=0,column=1,sticky='w',rowspan=2)

    widgetsLeftIMG2 = Label(left,image=barcolor,bg='white').place(x=200,y=300)
    # widgetsLeftIMG2.grid(row=1,columnspan=2)

    #RIGHT
    widgetsRightIMG1 = Label(right,image=skill,bg='white')
    widgetsRightIMG1.grid(row=0,columnspan=2,rowspan=2)

    #Botton
    # bottom.option_add('*font','Garamond 20')
    btn1 = Button(bottom,text="Click Me 1",font=('comic sans ms',15,'bold'))
    btn1.grid(row=0,column=0,ipadx=50,ipady=15,padx=5,pady=5)
    
    btn2 = Button(bottom,text="Click Me 2",width=15,font=('comic sans ms',15,'bold'))
    btn2.grid(row=0,column=1,ipadx=10,ipady=15,padx=5,pady=5)

    btn3 = Button(bottom,text="Click Me 3",width=15,font=('comic sans ms',15,'bold'))
    btn3.grid(row=0,column=2,ipadx=15,ipady=15,padx=5,pady=5)
    
    btn4 = Button(bottom,text="Exit Program",width=15,font=('comic sans ms',15,'bold'),command=exit)
    btn4.grid(row=0,column=3,ipadx=15,ipady=15,padx=5,pady=5)

master = createwindow()
Profile = PhotoImage(file='week3 CS311/image/male.png').subsample(2,2)
barcolor = PhotoImage(file='week3 CS311/image/barcolor.png')
skill = PhotoImage(file='week3 CS311/image/skill.png')
top,left,right,bottom = layout(master)
widgets(top,left,right,bottom)
master.mainloop()