from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(host="localhost", username="root", password="root", database="libreray")
cur = db.cursor()


class edit_bookcategory:
    def __init__(self):
        self.edit_bok_cat=Toplevel()
        self.edit_bok_cat.title("Edit Book Category")

        screen_width=self.edit_bok_cat.winfo_screenwidth()
        screen_height=self.edit_bok_cat.winfo_screenheight()

        window_width=500
        window_height=300

        position_x = (screen_width//2)-(window_width//2)
        position_y = (screen_height//2)-(window_height//2)

        self.edit_bok_cat.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.edit_bok_cat.config(bg="#a4a791")
        self.create_widgets()

    def create_widgets(self):

        frame=Frame(self.edit_bok_cat,bg="#949781", bd=2, relief="solid")
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.heading = Label(frame, text="Book Category", font=("Times New Roman", 16, "bold"),bg="#0ba9aa", fg="#ffffff",width=50, pady=5)
        self.l0 = Label(frame, text="Book Category Code", font=("arial", 12, "bold"), bg="#a4a791")
        self.l1 = Label(frame, text="Book Category ", font=("arial", 12, "bold"), bg="#a4a791")

        self.t1 = Entry(frame, font=("arila", 12))

        self.cmb = ttk.Combobox(frame, font=("arial", 12), width=18)
        self.cmb.bind("<<ComboboxSelected>>", self.show)

        self.b1 = Button(frame, text="Update", font=("arila", 12, "bold"),  command=self.updte, bg="#02a0a4")
        self.b2 = Button(frame, text="Delete", font=("arila", 12, "bold"),  command=self.delte, bg="#02a0a4")

        self.heading.grid(row=0, column=0, columnspan=10, pady=5, sticky='ew')
        self.l0.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.cmb.grid(row=1, column=1, sticky='w')
        self.l1.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.t1.grid(row=2, column=1, sticky='w')
        self.b1.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.b2.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.cat_sr()

    def cat_sr(self):
        sql="select cat_cd from book_cat"
        cur.execute(sql)
        srno=cur.fetchall()
        #print(srno)
        self.cmb.config(values=srno)

    def show(self,event):
        cd=self.cmb.get()
        sql="select cat_name from book_cat where cat_cd=%s"
        val=(cd,)
        cur.execute(sql,val)
        dt=cur.fetchone()

        self.t1.delete(0,END)
        self.t1.insert(0,dt[0])

    def updte(self):
        cd=self.cmb.get()
        nm=self.t1.get()

        if len(cd)==0:
            messagebox.showwarning("Warning","Select Member Code")
            self.edit_bok_cat.focus()
            self.cmb.focus()
            return

        sql="update book_cat set cat_name=%s where cat_cd=%s"
        val=(nm,cd)
        cur.execute(sql,val)
        db.commit()
        messagebox.showinfo("INFO","Data Update")

    def delte(self):
        cd = self.cmb.get()
        nm = self.t1.get()

        if len(cd)==0:
            messagebox.showwarning("Warning","Select Member Code")
            self.edit_bok_cat.focus()
            self.cmb.focus()
            return

        sql="delete from book_cat where cat_cd=%s"
        val=(cd,)
        cur.execute(sql,val)
        db.commit()

        messagebox.showinfo("Delete","Successfully Delete")
        self.edit_bok_cat.focus()
        self.cmb.delete(0,END)
        self.t1.delete(0,END)
        self.cat_sr()
        self.cmb.focus()

