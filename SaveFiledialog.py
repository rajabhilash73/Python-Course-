"""
Save File Dialog
"""
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Abhilash\\OneDrive\\Desktop\\PYTHON",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", "*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    #filetext = input("Enter some text if you want :") #use this if you want to print through console
    file.write(filetext)
    file.close()


window = Tk()
button = Button(text="Save", command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()