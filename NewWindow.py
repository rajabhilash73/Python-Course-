"""
Create a new window
"""
from tkinter import *
def create_window():
    new_window =Tk() # Toplevel() = new window 'on top' of other windows. linked to a "bottom" window.
                    #  Tk() = new independent window
    old_window.destroy() # close out of an old window.
old_window = Tk()

window = Tk()
Button(window, text="Create new window", command=create_window).pack()
window.mainloop()