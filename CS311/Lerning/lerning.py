from tkinter import *

def createwindow () :
    root = Tk()
    root.title("GUI5 : Create Widget Example")
    root.wm_geometry("700x900")
    root.option_add('*font','Arial 16 ')
    root.grid_columnconfigure((0,1),weight=1)
    root.grid_rowconfigure((0,2),weight=1)
    root.grid_rowconfigure(1 , weight=4)

    return(root)

def layout(master):
    top = Frame(master,bg="#020409")
    top.grid_columnconfigure(0,weight=1)
    top.grid_rowconfigure(0,weight=1)
    top.grid(row=0,columnspan=2 ,sticky='news')

    left = Frame(master,bg="#F9F9F9")
    left.grid_columnconfigure((0),weight=1)
    left.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    left.grid(row=1,column=0,sticky='news')

    right = Frame(master,bg="white")
    right.grid_columnconfigure((0),weight=1)
    right.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    right.grid(row=1,column=1,sticky='news')

    bottom = Frame(master,bg="#020409")
    bottom.grid_rowconfigure(0,weight=1)
    bottom.grid_columnconfigure(0,weight=1)
    bottom.grid(row=2,columnspan=2,sticky='news')

    return(top,left,right,bottom)

def topside(top):
    title = Label(top,text="Design By Natchanon Saileamonpiwat",font=("Arial,22"),bg="black",fg="white")
    title.grid(row=0)

def leftlayout(left):
    for i,data in enumerate(imglist):
        Label(left,image=imglist[i],bg="#F9F9F9").grid(row=i)
# def rightlayout(right):

def bottomsite(bottom):
    bottomtitle = Label(bottom,text="TEST",bg="Black",fg="white").grid(row=0)
master = createwindow()
top,left,right,bottom = layout(master)

img1 = PhotoImage(file="Lerning/image/shirt1.png")
img2 = PhotoImage(file="Lerning/image/shirt2.png")
img3 = PhotoImage(file="Lerning/image/shirt3.png")
img4 = PhotoImage(file="Lerning/image/shirt4.png")
img5 = PhotoImage(file="Lerning/image/shirt5.png")
img6 = PhotoImage(file="Lerning/image/shirt6.png")
imglist = [img1,img2,img3,img4,img5,img6]
topside(top)
leftlayout(left)
bottomsite(bottom)
master.mainloop()