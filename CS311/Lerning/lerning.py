from tkinter import *

def createwindow () :
    root = Tk()
    root.title("Hello World")
    root.wm_geometry("800x800")
    root.option_add('*font','Garamond , 16 ')
    root.grid_columnconfigure((0,1),weight=1)
    root.grid_rowconfigure((0,2),weight=1)
    root.grid_rowconfigure(1 , weight=4)
    return(root)

def layout(master):
    top = Frame(master,bg="#020409")
    top.grid(row=0,columnspan=2 ,sticky='news')

    left = Frame(master,bg="#0E1117")
    left.grid(row=1,column=0,sticky='news')

    right = Frame(master,bg="white")
    right.grid(row=1,column=1,sticky='news')

    bottom = Frame(master,bg="#020409")
    bottom.grid(row=2,columnspan=2,sticky='news')

    return(top,left,right,bottom)

def toplayout(top):
    titleheader = Label(top,text="Hello World",bg="black",fg="white")
    titleheader.grid(row=0)

master = createwindow()
top,left,right,bottom = layout(master)
master.mainloop()