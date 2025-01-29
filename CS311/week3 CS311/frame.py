from tkinter import *

master = Tk()
master.wm_geometry('1200x900')
master.grid_rowconfigure((0,2),weight=1)
master.grid_rowconfigure(1,weight=4)
master.grid_columnconfigure(0,weight=2)
master.grid_columnconfigure(1,weight=1)


top = Frame(master,bg='#ECF6FC')
top.grid(row=0,columnspan=2,sticky='news')


left = Frame(master,bg='#C0E6A9') #Green
left.grid(row=1,column=0,sticky='news')

leftframe2 = Frame(master,bg='#F8F4DA') #Yellow
leftframe2.grid_columnconfigure((0,1),weight=1) 
leftframe2.grid(row=1,column=0,sticky='news',padx=15 , pady=10)

leftframe3 = Frame(master,bg='white') #ขาว
leftframe3.grid(row=1,column=0,sticky='news',padx=40 , pady=30)

right = Frame(master,bg='#DBE1F9')
right.grid(row=1,column=1,sticky='news',) 

bottom = Frame(master,bg='#91B5B5')
bottom.grid(row=2,columnspan=2,sticky='news')

master.mainloop()