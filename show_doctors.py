def load():
    sql="select srno from doctors"
    cur.execute(sql)
    data=cur.fetchall()
    #print(data)
    cmb3.config(values=data)

def show1(event):
    srno=cmb3.get()
    sql="select * from doctors where srno="+srno
    cur.execute(sql)
    data=cur.fetchone()
    print(data)
    t2.delete(0,END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    t8.delete(0, END)
    t9.delete(0, END)
    t10.delete(0, END)

    t2.insert(0,data[1])
    l15.config(text=data[2])
    l16.config(text=data[3])
    l17.config(text=data[4])
    t5.insert(0, data[5])
    t6.insert(0, data[6])
    t7.insert(0, data[7])
    t8.insert(0, data[8])
    t4.insert(0, data[9])
    t3.insert(0, data[10])
    t9.insert(0,data[11])
    t10.insert(0,data[12])



from tkinter import *
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(host="localhost", username="root", password="root", database="cricket")
cur = db.cursor()

top=Tk()
top.geometry("500x500")
top.geometry("500x800")
l0=Label(text="Doctor Dtail",font=("tahoma",16,"bold"))
l1 = Label(text="Enter Doctor code",font=("arail",12,"bold"))
l2 = Label(text="Enter Doctor Name",font=("arail",12,"bold"))
l3 = Label(text="Gender",font=("arail",12,"bold"))
l4 = Label(text="Department",font=("arail",12,"bold"))
l5 = Label(text="Consultation Day",font=("arail",12,"bold"))
l6 = Label(text="Consultation time",font=("arail",12,"bold"))
l7 = Label(text="From ",font=("arail",12,"bold"))
l8 = Label(text="To",font=("arail",12,"bold"))
l9 = Label(text="Address",font=("arail",12,"bold"))
l10 = Label(text="Contact Number",font=("arail",12,"bold"))
l11 = Label(text="Emergency No",font=("arail",12,"bold"))
l12 = Label(text="Total Patients",font=("arail",12,"bold"))
l13 = Label(text="fee",font=("arail",12,"bold"))
l14 = Label(text="Date",font=("arail",12,"bold"))
l15 = Label(font=("arail",12))
l16 = Label(font=("arail",12))
l17 = Label(font=("arail",12))

t2 = Entry(font=("arail",12))
t3 = Entry(font=("arail",12))
t4 = Entry(font=("arail",12))
t5 = Entry(font=("arail",12))
t6 = Entry(font=("arail",12))
t7 = Entry(font=("arail",12))
t8 = Entry(font=("arail",12))
t9 = Entry(font=("arail",12))
t10 = Entry(font=("arail",12))


'''dep = ("General Medican")
con_day = ("Mon", "Tue", "Wed", "Thus", "Fri", "Sat", "Sun")
cmb1 = ttk.Combobox(values=dep,font=("arail",12,"bold"))
cmb2 = ttk.Combobox(values=con_day,font=("arail",12,"bold"))'''
cmb3=ttk.Combobox(font=("arial",12,"bold"))
cmb3.bind("<<ComboboxSelected>>",show1)
'''
gen = IntVar()
rb1 = Radiobutton(text="Male", variable=gen, value=0,font=("arail",10,"bold"))
rb2 = Radiobutton(text="female", variable=gen, value=1,font=("arail",10,"bold"))
'''


l0.grid(row=0,column=5)
l1.grid(row=1, column=1, padx=10, pady=10)
cmb3.grid(row=1, column=2)
l2.grid(row=2, column=1, padx=10, pady=10)
t2.grid(row=2, column=2)
l3.grid(row=3, column=1, padx=10, pady=10)
l15.grid(row=3, column=2, padx=10, pady=10)
l4.grid(row=4, column=1, padx=10, pady=10)
l16.grid(row=4, column=2)
l5.grid(row=5, column=1, padx=10, pady=10)
l17.grid(row=5, column=2)
l6.grid(row=6, column=1, padx=10, pady=10)
l7.grid(row=6, column=2)
t5.grid(row=6, column=3, padx=10, pady=10)
l8.grid(row=6, column=4)
t6.grid(row=6, column=5, padx=10, pady=10)
l9.grid(row=7, column=1, padx=10, pady=10)
t7.grid(row=7, column=2)
l10.grid(row=8, column=1, padx=10, pady=10)
t8.grid(row=8, column=2)
l11.grid(row=9, column=1, padx=10, pady=10)
t4.grid(row=9, column=2)
l12.grid(row=10, column=1, padx=10, pady=10)
t3.grid(row=10, column=2)
l13.grid(row=11, column=1, padx=10, pady=10)
t9.grid(row=11, column=2)
l14.grid(row=12, column=1, padx=10, pady=10)
t10.grid(row=12, column=2)

load()


top.mainloop()
