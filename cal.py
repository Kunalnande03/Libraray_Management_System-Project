from tkinter import *
from tkinter import messagebox
import calendar
top=Tk()
top.geometry("100x100")
cal=calendar.month(2003,1)
l1=Entry(text=cal)
l1.pack()
a=messagebox.askquestion("Are you sure")
print(a)

top.mainloop()
