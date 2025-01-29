from tkinter import *
from tkinter import ttk  # ใช้ ttk สำหรับ Progress Bar

def createwindow():  
    master = Tk()
    master.geometry('1200x900')  
    master.grid_rowconfigure((0, 2), weight=1)
    master.grid_rowconfigure(1, weight=4)
    master.grid_columnconfigure(0, weight=2)
    master.grid_columnconfigure(1, weight=1)
    master.option_add('*font', 'Garamond 20')
    return master

def layout(master):  
    top = Frame(master, bg='#D9EAFD')
    top.grid(row=0, columnspan=2, sticky='news')

    left = Frame(master, bg='#FFA09B')  
    left.grid(row=1, column=0, sticky='news')
    left.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  # เพิ่ม row รองรับ Progress Bar
    left.grid_columnconfigure((0, 1), weight=1)

    right = Frame(master, bg='#EFB036')  
    right.grid(row=1, column=1, sticky='news')

    bottom = Frame(master, bg='#26355D')  
    bottom.grid(row=2, columnspan=2, sticky='news')
    bottom.grid_rowconfigure(0, weight=1)
    bottom.grid_columnconfigure((0, 1, 2, 3), weight=1)

    return top, left, right, bottom

def widgets(top, left, right, bottom):  
    # TOP
    heading = Label(top, text="Dashboard DIY By Natchanon Saileamonpiwat", fg='Black', font=('comic sans ms', 25, 'bold'), bg="#D9EAFD")
    heading.pack(pady=15)

    # LEFT
    widgetsLeftIMG1 = Label(left, image=Profile, bg='white')
    widgetsLeftIMG1.grid(row=0, column=0, rowspan=2)  # ให้ภาพใช้พื้นที่ 2 แถว

    textleft = Label(left, text="Natchanon Saileamonpiwat", fg='Black', font=('comic sans ms', 18, 'bold'), bg="#D9EAFD")
    textleft.grid(row=0, column=1, padx=10, sticky="w")

    jobtitle = Label(left, text="Instructor", fg='Black', font=('comic sans ms', 15), bg="#D9EAFD")
    jobtitle.grid(row=1, column=1, padx=10, sticky="w")

    # Progress Bar Section
    Label(left, text="Age", bg="#FFA09B", font=('comic sans ms', 14)).grid(row=2, column=0, sticky="w", padx=20)
    age_bar = ttk.Progressbar(left, length=200, value=27, maximum=100)
    age_bar.grid(row=2, column=1, sticky="w", padx=10)

    Label(left, text="Weight", bg="#FFA09B", font=('comic sans ms', 14)).grid(row=3, column=0, sticky="w", padx=20)
    weight_bar = ttk.Progressbar(left, length=200, value=55, maximum=100)
    weight_bar.grid(row=3, column=1, sticky="w", padx=10)

    Label(left, text="Height", bg="#FFA09B", font=('comic sans ms', 14)).grid(row=4, column=0, sticky="w", padx=20)
    height_bar = ttk.Progressbar(left, length=200, value=165, maximum=200)
    height_bar.grid(row=4, column=1, sticky="w", padx=10)

    Label(left, text="Skill", bg="#FFA09B", font=('comic sans ms', 14)).grid(row=5, column=0, sticky="w", padx=20)
    skill_bar = ttk.Progressbar(left, length=200, value=5, maximum=10)
    skill_bar.grid(row=5, column=1, sticky="w", padx=10)

    # RIGHT
    widgetsRightIMG1 = Label(right, image=skill, bg='white')
    widgetsRightIMG1.grid(row=0, column=0)

    # Bottom Buttons
    btn1 = Button(bottom, text="Click Me 1", width=15)
    btn1.grid(row=0, column=0)

    btn2 = Button(bottom, text="Click Me 2", width=15)
    btn2.grid(row=0, column=1)

    btn3 = Button(bottom, text="Click Me 3", width=15)
    btn3.grid(row=0, column=2)

    btn4 = Button(bottom, text="Exit Program", width=15, command=master.quit)
    btn4.grid(row=0, column=3)

master = createwindow()
Profile = PhotoImage(file='week3 CS311/image/female.png').subsample(2, 2)
skill = PhotoImage(file='week3 CS311/image/skill.png')
top, left, right, bottom = layout(master)
widgets(top, left, right, bottom)
master.mainloop()
