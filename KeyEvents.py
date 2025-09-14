"""
Key events in python
"""
from tkinter import *

def doSomething(event):
    #print("You pressed a key", event.kesym)
    label.config(text=event.keysym)

window = Tk()
window.bind("<Key>", doSomething)
label = Label(window, font=("Helvetica", 50))
label.pack()

window.mainloop()