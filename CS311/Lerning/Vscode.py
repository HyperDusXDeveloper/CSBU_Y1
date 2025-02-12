from tkinter import *

def createwindow():
    root = Tk()
    root.title("Am trying")
    root.wm_geometry("800x800")
    root.option_add('font*','Garamond , 16')
    root.grid_rowconfigure((2),weight=1)
    root.grid_rowconfigure(0,weight=2)
    root.grid_rowconfigure(1,weight=6)
    root.grid_columnconfigure((0,1),weight=1)
    return(root)

def layout(master):
    top = Frame(master,bg="#020409")
    top.grid(row=0 ,columnspan=3 , sticky='news',ipady=5)

    right = Frame(master,bg="#0E1117")
    right.grid(row=1 , column=1 ,columnspan=2 ,sticky='news')

    left = Frame(master,bg="white")
    left.grid(row=1,column=0 ,sticky='news')

    bottom = Frame(master,bg="#020409")
    bottom.grid(row=2 ,columnspan=2 ,sticky='news')
    return(top,right)

master = createwindow()
top,right = layout(master)
master.mainloop()