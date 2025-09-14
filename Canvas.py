"""
canvas = widgets that are ised to draw graphs, plots and images in windows.
"""
from tkinter import *

window = Tk()
canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
# canvas.create_line(0, 500, 500, 0, fill="red", width=5)
# canvas.create_rectangle(50, 50, 250, 250, fill="skyblue")
# canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="orange", outline="black", width=5)
canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=15)
canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, start=180, width=15)
canvas.create_oval(190, 190, 310, 310, fill="white", width=15)
canvas.pack()

window.mainloop()