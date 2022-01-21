from tkinter import *
from time import *

window = Tk()
window.config(background="black")

def update():
    
    time_str = strftime("%I:%M:%S %p")
    time_label.config(text=time_str)
    
    day_str = strftime("%A")
    day_label.config(text=day_str)
    
    date_str = strftime("%B %d ,%Y")
    date_label.config(text=date_str)
    
    window.after(1000,update)
    
time_label = Label(window,font=("Arial",50),fg="cyan",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",35),fg="blue",bg="black")
day_label.pack()

date_label = Label(window,font=("Ink Free",35),fg="green",bg="black")
date_label.pack()

update()

window.mainloop()