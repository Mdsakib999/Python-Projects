#Digital clock

from cProfile import label
from cgitb import text
import string
from tkinter import*
from tkinter.ttk import*

from time import strftime
from turtle import title

root = Tk()
root = title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("sans-serif", 60), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()