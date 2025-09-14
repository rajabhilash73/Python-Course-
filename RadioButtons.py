"""
Radio Buttons = similar to checkbox, but you can only select one from a group.
"""
from tkinter import *

food = ["Burger", "Pizza", "Samosa", "Momos"]

def order():
    if(x.get()==0):
        print("You ordered burger !")
    elif(x.get()==1):
        print("You ordered pizza ! ")
    elif (x.get() == 1):
        print("You ordered pizza ! ")
    else:
        print("You ordered Momos !")

window = Tk()
burger_photo = PhotoImage(file="burger.png")
pizza_photo = PhotoImage(file="pizza.png")
samosa_photo = PhotoImage(file="samosa.png")
momos_photo = PhotoImage(file="momos.png")
food_images = [burger_photo, pizza_photo, samosa_photo, momos_photo]
x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # add text to radiobutton
                              variable=x,        # groups radiobuttons together if they share the same variables.
                              value=index,       # assigns each radiobutton a different value.
                              padx = 25,          #adds padding on x axis
                              font=("Impact", 50),
                              image=food_images[index],  # adds images to radiobuttons
                              compound= "left",        # adss image & texts left-side
                              indicatoron=0,    # eliminates circle indications
                              width = 375,      # sets width of radiobuttons
                              command=order)     # sets commands of radiobuttons to function
    radiobutton.pack(anchor=W)
window.mainloop()
