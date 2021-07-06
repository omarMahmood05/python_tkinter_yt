from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Cute Kitty Slides")
root.iconbitmap("images\\6\\catICO.ico")

# Images Start
myImg1= ImageTk.PhotoImage(Image.open('images/7/cat1.jpg'))
myImg2= ImageTk.PhotoImage(Image.open('images/7/cat2.jpg'))
myImg3= ImageTk.PhotoImage(Image.open('images/7/cat3.jpg'))
myImg4= ImageTk.PhotoImage(Image.open('images/7/cat4.jpg'))
myImg5= ImageTk.PhotoImage(Image.open('images/7/cat5.jpg'))
# Images End

# Image List Start
catImageList = [myImg1, myImg2, myImg3, myImg4, myImg5]
# Image List End
# userInput = Entry(root)
# catLen = len(catImageList)
# userInput.insert(0,catLen)
# userInput.grid(row=2, column=0)
mySlide = Label(image=catImageList[0])

# Functions Start
def forward(image_number):
    global mySlide
    global forwardButton
    global backButton
    global catLen
    catLen = len(catImageList)
    mySlide.grid_forget()
    mySlide = Label(image=catImageList[int(image_number)-1])
    mySlide.grid(row=0, column=0, columnspan=3)
    forwardButton = Button(root, text=">>",width=8, command=lambda : forward(image_number+1))
    backButton = Button(root, text="<<",width=8, command=lambda : forward(image_number-1))
    forwardButton.grid(row=1, column =2)
    backButton.grid(row=1, column =0)

    if image_number >= catLen:
        forwardButton = Button(root, text="END", width=8, state=DISABLED)
        forwardButton.grid(row=1, column=2)

    if image_number == 1:
        backButton = Button(root, text="Start", width=8,  state=DISABLED)
        backButton.grid(row=1, column=0)


def back():
    return

# Functions End

# Buttons Start
backButton= Button(root, text= "Start", width=8, command=back, state=DISABLED)
exitButton= Button(root, text= "Exit Program", command=root.quit)
forwardButton= Button(root, text= ">>", width=8, command=lambda :forward(2))
# Buttons End

# Grids Start
mySlide.grid(row=0, column=0, columnspan=3)
backButton.grid(row=1, column=0)
exitButton.grid(row=1, column =1)
forwardButton.grid(row=1, column =2)
# Grids End




root.mainloop()

