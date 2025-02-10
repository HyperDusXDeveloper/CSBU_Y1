from tkinter import *

def createwindow():
    window = Tk()
    window.title("Hello World")
    window.wm_geometry("1000x500")
    return(window)

window = createwindow()
window.mainloop()