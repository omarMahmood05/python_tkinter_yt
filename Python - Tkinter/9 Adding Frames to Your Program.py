from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frames")
root.iconbitmap("images/6/catICO.ico")
# we can use pack and grid together when using frames
myFrame = LabelFrame(root, padx=50, pady=50) # We can add text here
myFrame.pack(padx=100, pady=100)

myLabel = Button(myFrame, text="This is a button inside the frame")
myLabel.pack()

root.mainloop()