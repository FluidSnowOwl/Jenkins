from tkinter import *
from tkinter.ttk import *

root = Tk()
j = Frame(root)
n = Notebook(j)
f1 = Frame(n)
f2 = Frame(n)
n.add(f1, text='One')
n.add(f2, text='Two')
root.mainloop()