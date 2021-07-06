from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("images/6/catICO.ico")

radioAns = IntVar()

global optPrint
optPrint = Label(root, text="0")

def clicked(value):
    global optPrint
    optPrint.forget()
    optPrint = Label(root, text=value)
    optPrint.pack()


Radiobutton(root, text="Option 1",variable=radioAns, value=1, command= lambda :clicked(1)).pack()
Radiobutton(root, text="Option 2",variable=radioAns, value=2, command= lambda :clicked(2)).pack()

root.mainloop()