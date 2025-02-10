from tkinter import *

def createwindow() :
    window = Tk()
    window.title("Atommic Save Seazone")
    window.wm_geometry("500x500")
    window.grid_columnconfigure((0,1), weight=1)
    window.grid_rowconfigure(0 ,weight=1)
    window.grid_rowconfigure(1 ,weight=5)
    window.grid_rowconfigure(2 ,weight=2)
    return(window)

def layout(window):
    top = Frame(window,bg="black")

window = createwindow()
top = layout(window)
window.mainloop()