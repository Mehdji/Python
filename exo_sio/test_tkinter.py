#Tk is a python's module which allow user to create GUI.
from tkinter import *
from tkinter import ttk

#Create a instance from tk class name 'root'
#It's the root window.
root = Tk()

frm = ttk.Frame(root, padding=10)

frm_2 = ttk.Frame(root, padding=10)
frm.grid()
frm_2.grid()

ttk.Label(frm, text="Hello, world!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


