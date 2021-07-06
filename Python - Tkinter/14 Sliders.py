from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("File Dialogs")
root.iconbitmap("images/6/catICO.ico")
root.geometry("400x400")

verticalSliders = Scale(root, from_=200, to=800)
verticalSliders.pack()

horizontalSliders = Scale(root, from_=200, to=800, orient=HORIZONTAL)
horizontalSliders.pack()

def windowResize():
    root.geometry(str(horizontalSliders.get()) + ("x") + str(verticalSliders.get()))

numberButton = Button(root, text="Click me To refresh", command=windowResize).pack()




root.mainloop()