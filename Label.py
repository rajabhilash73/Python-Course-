"""
Label = an area widgets that holds text and/or an image within a window.
"""

from tkinter import *
window = Tk()
photo = PhotoImage(file = "logo.png")
label = Label(window,
              text = "Code Like Ninja",
              font = ("Arial", 12, "bold"),
              fg = "#00FF00",
              background = "black",
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound = "bottom")
label.pack()
# label.place(x = 0, y = 0)

window.mainloop()