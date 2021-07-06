from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Pizza")
root.iconbitmap("images/6/catICO.ico")

MODES = [
    ("Peperoni", "Peperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("BBQ", "BBQ"),
]

pizza = StringVar()
pizza.set("Peperoni")

for text,type in MODES:
    Radiobutton(root, text=text,variable=pizza, value=type).pack(pady=10)

myButton = Button(root, text="Click to Order Now!", command= lambda :buttonClick()).pack(padx=100, pady=10)

def buttonClick():
    global myLabel
    myLabel = Label(root, text="You've ordered a " + pizza.get() + " pizza.").pack()

root.mainloop()