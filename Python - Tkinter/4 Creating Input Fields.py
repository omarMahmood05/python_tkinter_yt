from tkinter import *

root = Tk()

def printName():
    printText = "Hey there " + userEntry.get() + " hope you're having a good day!"
    buttonText = Label(root, text=printText)
    buttonText.pack()

userEntry = Entry(root, width=50, bg="grey", fg="Black", borderwidth=5)
userEntry.pack()
userEntry.get()
userEntry.insert(0, "Enter your name to be greeted")





myButton = Button(root, text="Click Me!", padx=50, pady=50, command=printName, bg="Grey", fg="black")
myButton.pack()

root.mainloop()