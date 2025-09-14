from tkinter import *

def submit():
    print("The Temperature is : " + str(scale.get()) + " degrees C")

window = Tk()

# Load images
hotImage = PhotoImage(file="resize-1749568226108724098hot.png")
coldImage = PhotoImage(file="resize-1749568444909155660cold.png")

# Hot image label
hotLabel = Label(window, image=hotImage)
hotLabel.pack()

# Scale widget
scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10,
              showvalue=0,
              resolution=5,
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="#111111")
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()

# Cold image label
coldLabel = Label(window, image=coldImage)
coldLabel.pack()

# Submit button
button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()