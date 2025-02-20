from tkinter import *

def mainwindow() :
    root = Tk()
    root.title("Homework of Week5 :Home Fashion by Natchanon Saileamonpiwat")
    root.geometry("1000x800")
    root.rowconfigure((0,2),weight=1)
    root.grid_rowconfigure(1 ,weight=4)
    root.grid_columnconfigure((0,1),weight=1)
    root.option_add('*font', "Arial 12 bold")

    return(root)

def layout(master) :

    #TOP FRAME
    top = Frame(master,bg="#6E7998")
    top.grid_rowconfigure(0,weight=1)
    top.grid_columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky='news')

    #LEFT FRAME
    left = Frame(master,bg="#CED7DC")
    left.grid_rowconfigure((0,1,2,3),weight=1)
    left.grid_columnconfigure((0,1,2,3,4),weight=1)
    left.grid(row=1,column=0,sticky='news')

    #RIGHT FRAME
    right = Frame(master,bg="#FAF2D5")
    right.grid_rowconfigure((0,1,2,3),weight=1)
    right.grid_columnconfigure((0,1,2,3,4),weight=1)
    right.grid(row=1,column=1,sticky='news')

    #BOTTOM FRAME
    bottom = Frame(master,bg="#6E7998")
    bottom.grid_columnconfigure((0,1),weight=1)
    bottom.grid_rowconfigure(0,weight=1)
    bottom.grid(row=2,columnspan=2,sticky='news')

    return(top,bottom,left,right)

def topside(top) :
    title = Label(top,text="Dream Fashion by Natchanon Saileamonpiwat ",font=("Arial",22),bg="#6E7998",fg='white')
    title.grid(row=0)




#Function
master = mainwindow()
top,bottom,left,right = layout(master)
topside(top)

#Main
master.mainloop()