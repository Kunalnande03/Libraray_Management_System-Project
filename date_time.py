def sv():
    #dt=t1.get()
    str1=date.today()
    st2="2025-03-01"
    dt=str1
    print(str1)
    print(dt)

    '''if st2[8:]<str1[8:]:
        print("hii")
    if len(dt)==0 or dt<str(date.today):
        print("hello")
        '''
def timme():
    l1.config(text="Time is")
    l1.pack()

from tkinter import *
import time
from tkinter import ttk
from datetime import date,datetime
import threading
if '2025-01-02'<str(date.today()):
    tm=threading.Timer(5,timme)
    tm.start()

print(type(datetime.today()))
top=Tk()
top.geometry("200x200")
t1=Entry()
t1.pack()
l1=Label()
b1 = Button(text="sv", command=sv)
b1.pack()
dt=(date.today(),)
cmb=ttk.Combobox(values=dt)
i=4
j=2
print("j",i%j)

print(date.today())
cmb.pack()
top.mainloop()