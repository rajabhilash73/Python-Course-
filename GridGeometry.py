"""
Grid geometry in python - Grid geometry manager in python organizes widgets in table like structure in a parent
"""
from tkinter import *

window = Tk()
titleLabel = Label(window, text="Enter your Information",bg="yellow", font=("Arial", 20)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First Name : ", width=20, bg="pink").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last Name : ", width=20, bg="skyblue").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="Email : ", width=20, bg="red").grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit", width=10, bg="light green").grid(row=4, column=0, columnspan=2)
window.mainloop()
