"""
Text widget = Functions like a text area, you can enter multiple line of texts.
"""
from tkinter import *
def submit():
    input = text.get(1.0, END)
    print(input)
window = Tk()
text = Text(window,
            bg="Light yellow",
            font=("Ink free", 18),
            height=10,
            width=20,
            padx=10,
            pady=10,
            fg = "Purple")
text.pack()
button = Button(window, text="submit", command=submit)
button.pack()
window.mainloop()
