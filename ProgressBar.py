from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    Download = 0
    Speed = 1
    while(Download<GB):
        time.sleep(0.05)
        bar['value']+= (Speed/GB)* 100
        Download += Speed
        percent.set(str(int((Download/GB)*100)) + "%")
        text.set(str(Download)+ "/" + str(GB) + " " + "GB completed")
        window.update_idletasks()

window = Tk()
percent = StringVar()
text = StringVar()
bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)
percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()