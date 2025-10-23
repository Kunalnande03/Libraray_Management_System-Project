def save():
    gn = gen.get()
    if gn == 0:
        gn = "Male"
    else:
        gn = "Female"
    cd = t1.get()
    nm = t2.get()
    dep = cmb1.get()
    cons_d = cmb2.get()
    time1 = t5.get()
    time2 = t6.get()
    add = t7.get()
    co_no = t8.get()
    em_no = t4.get()
    total_pa = t3.get()
    fee = t9.get()
    date = t10.get()
    sql = "insert into doctors(srno,name,sex,department,day,time1,time2,adress,cont_no,emg_no,fee,patients,date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (cd, nm, gn, dep, cons_d, time1, time2, add, co_no, em_no, total_pa, fee, date,)
    messagebox.showinfo("saved", "new rocord added")
    cur.execute(sql, val)
    db.commit()


import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

top = Tk()
db = mysql.connector.connect(host="localhost", username="root", password="root", database="cricket")
cur = db.cursor()

top.geometry("500x800")
l0=Label(text="Doctor Dtail",font=("arail",16,"bold"))
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

t1 = Entry(font=("arail",12))
t2 = Entry(font=("arail",12))
t3 = Entry(font=("arail",12))
t4 = Entry(font=("arail",12))
t5 = Entry(font=("arail",12))
t6 = Entry(font=("arail",12))
t7 = Entry(font=("arail",12))
t8 = Entry(font=("arail",12))
t9 = Entry(font=("arail",12))
t10 = Entry(font=("arail",12))

dep = ("General Medican")
con_day = ("Mon", "Tue", "Wed", "Thus", "Fri", "Sat", "Sun")
cmb1 = ttk.Combobox(values=dep,font=("arail",12,"bold"))
cmb2 = ttk.Combobox(values=con_day,font=("arail",12,"bold"))

gen = IntVar()
rb1 = Radiobutton(text="Male", variable=gen, value=0,font=("arail",10,"bold"))
rb2 = Radiobutton(text="female", variable=gen, value=1,font=("arail",10,"bold"))

b1 = Button(text="save", command=save,font=("tahoma",14,"bold"))

l0.grid(row=0,column=5)
l1.grid(row=1, column=1, padx=10, pady=10)
t1.grid(row=1, column=2)
l2.grid(row=2, column=1, padx=10, pady=10)
t2.grid(row=2, column=2)
l3.grid(row=3, column=1, padx=10, pady=10)
rb1.grid(row=3, column=2, padx=10, pady=10)
rb2.grid(row=3, column=3, padx=10, pady=10)
l4.grid(row=4, column=1, padx=10, pady=10)
cmb1.grid(row=4, column=2)
l5.grid(row=5, column=1, padx=10, pady=10)
cmb2.grid(row=5, column=2)
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

b1.grid(row=13, column=1)

top.mainloop()
