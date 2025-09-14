"""
Check buttons
"""
from tkinter import *
from tkinter import BooleanVar


def display():
    if(x.get()==1):
        print("You agree !")
    else:
        print("You don't agree :( !")
window = Tk()
x = IntVar()
python_photo = PhotoImage(file="python.png")
check_buttons = Checkbutton(window,
                            text="I agree to this statement !",
                            variable=x,
                            onvalue=1,
                            offvalue=0,
                            command=display,
                            font=("Arial", 16, "bold"),
                            fg = "Skyblue",
                            bg = "black",
                            activeforeground="Skyblue",
                            activebackground="black",
                            padx=25,
                            pady=10,
                            image=python_photo,
                            compound="left")
check_buttons.pack()
window.mainloop()