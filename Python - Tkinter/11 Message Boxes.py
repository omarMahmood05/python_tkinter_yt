from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("Message Boxes")
root.iconbitmap("images/6/catICO.ico")

# showinfo, showerror, showwarning, askquestion, askokcancel, askyesno,

def popup():
    response = messagebox.askyesno("This is the heading", "This is the body")
    if response == 1:
        myLabel = Label(root, text="You Clicked Yes!").pack()
    else:
        myLabel = Label(root, text="You Clicked No!").pack()

myButton = Button(root, text="Popup", command= lambda :popup()).pack()


root.mainloop()