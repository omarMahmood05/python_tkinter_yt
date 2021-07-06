from tkinter import *

# This has to be passed all the time. This is the main box/widget in which all other widgets are posted
root = Tk()
# Now to add text we have to create a label widget
myLabel = Label(root, text="Hello World")

myLabel.pack()

# For a program to be running we need to add a loop.

root.mainloop()
