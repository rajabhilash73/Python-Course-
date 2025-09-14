"""
Mouse events
"""
from tkinter import *
def doSomething(event):
    print("Mouse Coordinates : " + str(event.x) + "," + str(event.y))
window = Tk()

# window.bind("<Button-1>", doSomething)  # left mouse click
# window.bind("<Button-2>", doSomething)  # scroll Mouse click
# window.bind("<Button-3>", doSomething)  # Right mouse click
# window.bind("<Button-Release>", doSomething)
# window.bind("<Enter>", doSomething)  # Enter the window
# window.bind("<Leave>", doSomething)  # Leave the window
# window.bind("<Motion>", doSomething) # Where the mouse moved

window.mainloop()