from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("Message Boxes")
root.iconbitmap("images/6/catICO.ico")

def openNewWin():
    top = Toplevel()
    top.title("This is the second window")
    text = Label(top, text="This is a random test text")
    text.pack()
    buttonClose = Button(top, text="Close window", command= lambda :top.destroy()).pack()


openNewWindow = Button(root, text="Open New Window", command=openNewWin).pack()
root.mainloop()