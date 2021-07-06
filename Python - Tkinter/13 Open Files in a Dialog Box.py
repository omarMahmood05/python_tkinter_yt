from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("File Dialogs")
root.iconbitmap("images/6/catICO.ico")

def openImage():
    global myImage
    root.filename = filedialog.askopenfilename(initialdir="images/7", title="Choose the cutest kitty",filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))
    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    imagePrint = Label(image= myImage).pack()


button = Button(root, text="Choose Images", command=openImage).pack()

root.mainloop()