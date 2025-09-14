from tkinter import *
def Openfile():
    print("The file has been opened !")

def Savefile():
    print("The file has been saved !")

def cut():
    print("You cut some text!")

def copy():
    print("You copy some text !")

def paste():
    print("You paste some text!")
window = Tk()
openImage = PhotoImage(file="folder.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=Openfile, image=openImage, compound="left")
fileMenu.add_command(label="Save", command=Savefile, image=saveImage, compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound="left")

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)


window.mainloop()