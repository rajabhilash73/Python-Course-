"""
file dialog
"""
from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Abhilash\\OneDrive\\Desktop\\PYTHON",
                                          title="Open file ok",
                                          filetypes=(("text.files", "*.text"),
                                                     ("all files", "*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()
window= Tk()
button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()