"""
buttons = you click it, then it does stuff.
"""
from tkinter import *
count = 0

def click():
    global count
    count += 1
    print(count)
    # print("You clicked the button!")
window = Tk()
photo = PhotoImage(file = "Like.png")
button = Button(window,
                text = "Click Me!",
                command = click,
                font = ("Comic Sans", 30),
                fg = "sky blue",
                 bg = "black",
                activeforeground = "sky blue",
                activebackground = "black",
                state = ACTIVE,
                image = photo,
                compound = "top")
button.pack()
window.mainloop()