"""
Widgets = GUI elements: Buttons, textboxes, labels, images
windows = Serves as a container to hold or contain these images.
"""
from tkinter import *
window = Tk()  #instantiate an instance of a window.
window.geometry("420x420")
window.title("Code Like Ninja First GUI Program")

icon = PhotoImage(file = "logo.png")
window.iconphoto(True, icon)
window.config(background = "Sky Blue")
window.mainloop()  # place window on computer screen, listen for events
