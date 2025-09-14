"""
Frame = A rectangular container who hold the widgets
"""
from tkinter import *

window = Tk()

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.place(x=0, y=0)

Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="B", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="E", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="M", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()
