from tkinter import *
from tkinter import ttk
top=Tk()
top.state("zoomed")
cls=("AC-1","AC-2","AC-3")
cmb=ttk.Combobox(values=cls,font=("arial",20))
l1=Label(text="select class",font=("arial",20))
l2=Label(text="fare/seat",font=("arial",20))
l3=Label(text="0",font=("arial",20))
l4=Label(text="no of passengers",font=("arial",20))
l5=Label(text="total fare",font=("arial",20))
l6=Label(text="0",font=("arial",20))
l7=Label(text="senior citizen",font=("arial",20))
l8=Label(text="discount",font=("arial",20))
l9=Label(text="0",font=("arial",20))
l10=Label(text="net amount",font=("arial",20))
l11=Label(text="0",font=("arial",20))
t1=Entry(font=("arial",20))
l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()
l8.pack()
l9.pack()
l10.pack()
l11.pack()







top.mainloop()