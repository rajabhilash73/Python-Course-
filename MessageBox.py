"""
message box
"""
from tkinter import *
from tkinter import messagebox   # this module import message box library

def click():
    # messagebox.showinfo(title="This is an info message box !", message="You are a wonderful person")
    # messagebox.showwarning(title="WARNING", message="You have a virus in your computer!")
    # messagebox.showerror(title="ERROR", message="An error occurred")
    # if messagebox.askokcancel(title="Ask Ok Cancel", message="Do you want to do this ?"):
    #     print("You did this")
    # else:
    #     print("You cancel this")
    # if messagebox.askretrycancel(title="Ask Ok Cancel", message="Do you want to retry this ?")  :
    #     print("You retried this.")
    # else:
    #     print("You cancelled this.")
    #
    # if messagebox.askyesno(title="Ask Yes No", message="Do you like python ?"):
    #     print("Yes i like this very much ! :)")
    # else:
    #     print("Why do you don't like python ?")

      # answer = messagebox.askquestion(title="Ask Question", message="Do you like python  ?")
      # if(answer == "Yes"):
      #  print("I like python very much ! :)")
      # else:
      #   print("Why you don't like python? :(")

    answer = messagebox.askyesnocancel(title="Yes No Cancel", message="Do you like coding? ", icon="error")
    if (answer == True):
        print("You like to code ! :)")
    elif (answer == False):
        print("Then why you are doing python course ? :(")
    else:
        print("You have dodged the question")


window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()
