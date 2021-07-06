from tkinter import *

root = Tk()

def buttonClick():
    buttonText = Label(root, text="Hey, look I clicked a button!")
    buttonText.pack()

myButton = Button(root, text="Click Me!", padx=50, pady=50, command=buttonClick, bg="Grey", fg="black")
myButton.pack()

root.mainloop()