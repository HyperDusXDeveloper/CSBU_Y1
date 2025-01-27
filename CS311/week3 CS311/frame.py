from tkinter import *

master = Tk()
master.wm_geometry('1200x900')
master.grid_rowconfigure((0,2),weight=1)
master.grid_rowconfigure(1,weight=4)
master.grid_columnconfigure(0,weight=2)
master.grid_columnconfigure(1,weight=1)

top = Frame(master,bg='#FFDB00')
top.grid(row=0,columnspan=2,sticky='news')


left = Frame(master,bg='#06D001')
left.grid(row=1,column=0,sticky='news')

right = Frame(master,bg='#AF47D2')
right.grid(row=1,column=1,sticky='news',) #padx=10 , pady=15

bottom = Frame(master,bg='#26355D')
bottom.grid(row=2,columnspan=2,sticky='news')
master.mainloop()