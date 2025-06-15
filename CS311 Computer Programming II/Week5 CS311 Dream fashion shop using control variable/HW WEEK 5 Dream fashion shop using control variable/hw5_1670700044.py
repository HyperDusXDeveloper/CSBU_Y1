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


def leftside(left) :
    shirtmenu = ["Pink T-Shirt\n225 B.","Blue T-Shirt\n210 B.","Lemoon T-Shirt\n215 B.","Orange Shirt\n1,000 B."]
    shirtspy = [IntVar() for i in shirtmenu]

    for i,shirt in enumerate(shirtmenu):
        Label(left,bg='#CED7DC',image=shirtlist[i]).grid(row=i ,column=1)
        Checkbutton(left,bg='#CED7DC',text=shirt,variable=shirtspy[i],command=userclick).grid(row=i,column=2)
    return(shirtspy)

def rightside(right) :
    shoemenu = ["Van Black Color\n2,800 B.","Van Blue Color\n2,750 B.","Van Red Color\n3,000 B."," Van Green Color\n2,900 B."]
    shoespy = [IntVar() for i in shoemenu]

    for i,shoe in enumerate(shoemenu):
        Label(right,bg='#FAF2D5',image=shoelist[i]).grid(row=i,column=1)
        Checkbutton(right,bg='#FAF2D5',text=shoe,variable=shoespy[i],command=userclick).grid(row=i,column=2)
    return(shoespy)

def bottomside(bottom) :
    showshirt = Label(bottom,bg='#6E7998')
    showshirt.grid(row=0,column=0)
    showshoe = Label(bottom,bg='#6E7998')
    showshoe.grid(row=0,column=1)

    return(showshirt,showshoe)

def userclick() :
    totalshirt = 0
    totalshoe = 0

    shirtprice = [225,210,215,1000]
    shoeprice = [2800,2750,3000,2900]

    for i,item in enumerate(shirtprice) :
        totalshirt += shirtspy[i].get()*shirtprice[i]
    
    for i,item in enumerate(shoeprice) :
        totalshoe += shoespy[i].get()*shoeprice[i]

    showshirt['text'] = f'Shirt Total Amount = {totalshirt:0.2f} Bath'
    showshirt['bg'] = "#CED6DC"
    showshirt['fg'] = "black"
    showshoe['text'] = f'Shoe Total Amount = {totalshoe:0.2f} Bath'
    showshoe['bg'] = "#CED6DC"
    showshoe['fg'] = "black"

#Function
master = mainwindow()
top,bottom,left,right = layout(master)

#import Image
shirt1 = PhotoImage(file="Week5 CS311/image/shirt1.png")
shirt2 = PhotoImage(file="Week5 CS311/image/shirt2.png")
shirt3 = PhotoImage(file="Week5 CS311/image/shirt3.png")
shirt4 = PhotoImage(file="Week5 CS311/image/shirt4.png")
shoe1 = PhotoImage(file="Week5 CS311/image/shoe1.png")
shoe2 = PhotoImage(file="Week5 CS311/image/shoe2.png")
shoe3 = PhotoImage(file="Week5 CS311/image/shoe3.png")
shoe4 = PhotoImage(file="Week5 CS311/image/shoe4.png")

#List
shirtlist = [shirt1,shirt2,shirt3,shirt4]
shoelist = [shoe1,shoe2,shoe3,shoe4]

#Function
topside(top)
shirtspy = leftside(left)
shoespy = rightside(right)
showshirt,showshoe = bottomside(bottom)

#Main
master.mainloop()