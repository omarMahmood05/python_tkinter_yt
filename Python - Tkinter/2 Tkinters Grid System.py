from tkinter import *

root = Tk()

myText1 = Label(root, text="Hey There!")
myText2 = Label(root, text="My Name is Omar Mahmood")
myText3 = Label(root, text="                ")

myText1.grid(row=0, column=0)
myText3.grid(row=0, column=2)
myText2.grid(row=1, column=3)


root.mainloop()