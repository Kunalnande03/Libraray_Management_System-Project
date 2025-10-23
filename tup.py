def loading_bar():
    for i in range(100):
        l1.config(text=i,font=("arial",12,"bold"),width=i,bg="lightgray")

from datetime import date
tup=("","")
print(tup)
if tup[0]!=date.today() or tup[1]!=3:
    li=list(tup)
    li.insert(0,date.today())
    tup=tuple(li)
    print(type(tup[0]))
    print(type(date.today()))
import time
from tkinter import *
top=Tk()
top.geometry("100x100")

l1=Label()
l1.pack()

top.mainloop()
