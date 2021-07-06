from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("This is a cute Kitty")
root.iconbitmap("images\\6\\catICO.ico")

myImg = ImageTk.PhotoImage(Image.open("images/6/catImg.jpg"))
myLabel = Label(image=myImg)
myLabel.pack()

quitButton = Button(root,text= "Loose Kitty T_T", command=root.quit)
quitButton.pack()
root.mainloop()

