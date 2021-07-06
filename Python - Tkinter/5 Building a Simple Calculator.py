from tkinter import *

root = Tk()
root.title("Python Calc - Omar Mahmood")
# User Input Get Start
userInput = Entry(root, width=32)
# User Input Get End
# Functions Start
def button_click(num):
    current = userInput.get()
    userInput.delete(0, END)
    userInput.insert(0, str(current) + str(num))

def addition():
    global num1
    global maths
    maths = "add"
    num1 = userInput.get()
    userInput.delete(0, END)

def multiplication():
    global num1
    global maths
    maths = "mull"
    num1 = userInput.get()
    userInput.delete(0, END)

def division():
    global num1
    global maths
    maths = "divis"
    num1 = userInput.get()
    userInput.delete(0, END)

def subtraction():
    global num1
    global maths
    maths = "subt"
    num1 = userInput.get()
    userInput.delete(0, END)

def equalsTo():
    num2 = userInput.get()
    userInput.delete(0, END)
    if maths == "add":
        userInput.insert(0, int(num1) + int(num2))
    elif maths == "mull":
        userInput.insert(0, int(num1) * int(num2))
    elif maths == "divis":
        userInput.insert(0, int(num1) / int(num2))
    elif maths == "subt":
        userInput.insert(0, int(num1) - int(num2))
    else:
        userInput.insert(0, "WRONG OPERATOR")
def clearCalc():
    userInput.delete(0, END)
# Functions End
# Button Creation Start
button1=Button(root, text="1", width= 8, height= 3, command=lambda :button_click(1))
button2=Button(root, text="2", width= 8, height= 3, command=lambda :button_click(2))
button3=Button(root, text="3", width= 8, height= 3, command=lambda :button_click(3))
button4=Button(root, text="4", width= 8, height= 3, command=lambda :button_click(4))
button5=Button(root, text="5", width= 8, height= 3, command=lambda :button_click(5))
button6=Button(root, text="6", width= 8, height= 3, command=lambda :button_click(6))
button7=Button(root, text="7", width= 8, height= 3, command=lambda :button_click(7))
button8=Button(root, text="8", width= 8, height= 3, command=lambda :button_click(8))
button9=Button(root, text="9", width= 8, height= 3, command=lambda :button_click(9))
button0=Button(root, text="0", width= 8, height= 3, command=lambda :button_click(0))

buttonAdd=Button(root, text="+", width= 8, height= 3, command=addition)
buttonClear=Button(root, text="Clear", width= 18, height= 3, command=clearCalc)
buttonEqual=Button(root, text="=", width= 18, height= 3, command= equalsTo)

buttonMul=Button(root, text="*", width=8, height=3,command=multiplication )
buttonDiv=Button(root, text="/", width=8, height=3, command=division)
buttonSub=Button(root, text="-", width=8, height=3, command= subtraction)
# Button Creation End

# Placement Start
userInput.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1,columnspan=2)

buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1,columnspan=2)

buttonMul.grid(row=6, column=0)
buttonDiv.grid(row=6, column=1)
buttonSub.grid(row=6, column=2)
# Placement End


root.mainloop()