"""
Listbox = A listing of selectable text items within its own computer
"""
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered : ")

    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg = "yellow",
                  fg = "black",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Burger")
listbox.insert(2, "Pizza")
listbox.insert(3, "Pasta")
listbox.insert(4, "Noodles")
listbox.insert(5, "Hotdog")
listbox.insert(6, "Momos")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()
window.mainloop()