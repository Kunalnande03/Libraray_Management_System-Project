import lib2to3.pgen2.token
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

db = mysql.connector.connect(host="localhost", database="libreray", username="root", password="root")
cur = db.cursor()


class add_membership:
    def __init__(self):
        self.add_membership_detail=Toplevel()
        self.add_membership_detail.title("Add Member Ship Detail")

        screen_width=self.add_membership_detail.winfo_screenwidth()
        screen_height=self.add_membership_detail.winfo_screenheight()

        window_width=500
        window_height=350

        position_x=(screen_width//2)-(window_width//2)
        position_y=(screen_height//2)-(window_height//2)

        self.add_membership_detail.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.add_membership_detail.config(bg="#a4a791")

        self.create_widgets()

    def create_widgets(self):
        frame=Frame(self.add_membership_detail,bg="#949781",bd=2,relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)
        self.heading = Label(frame,text="Add Membership Detail", font=("Times New Roman", 16, "bold"), width=50, fg="#fdfdfd",
                       bg="#0ba9aa")
        self.l1 = Label(frame,text="Membership Type", font=("arial", 14, "bold"), bg="#949781")
        self.l2 = Label(frame,text="Fee", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame,text="No. Of Book ", font=("arial", 14, "bold"), bg="#949781")

        self.t1 = Entry(frame,font=("arila", 12))
        self.t2 = Entry(frame,font=("arila", 12))
        self.t3 = Entry(frame,font=("arila", 12))

        self.b1 = Button(frame,text="Save", font=("arial", 14, "bold"), border=3, command=self.save_mem_ty, bg="#02a0a4")
        self.b2 = Button(frame,text="Reset", font=("arial", 14, 'bold'), border=3, command=self.reset, bg="#02a0a4")
        self.b3 = Button(frame,text="Close", font=("arial", 14, "bold"), border=3, command=self.cls, bg="#02a0a4")

        self.heading.grid(row=0, column=0, pady=5, columnspan=10, sticky='ew')
        self.l1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.t1.grid(row=1, column=1, sticky='w')
        self.l2.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.t2.grid(row=2, column=1, sticky='w')
        self.l3.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.t3.grid(row=3, column=1, sticky='w')
        self.b1.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.b2.grid(row=4, column=1, sticky='w')
        # self.b3.grid(row=5,column=0,sticky='ew',padx=10,pady=10)

    def save_mem_ty(self):
        try:
            ty = self.t1.get()
            fee =self.t2.get()
            nob =self.t3.get()

            ty=str.strip(str.title(ty))
            fee=str.strip(fee)
            nob=str.strip(nob)

            if len(ty)==0 or len(fee)==0 or len(nob)==0:
                messagebox.showerror("Error","Fill The Entry Box")
                self.t1.focus()
                self.add_membership_detail.focus()
                return

            sql = "Select count(*) from member_type where type=%s"
            val1 = (ty,)
            cur.execute(sql, val1)
            dt = cur.fetchone()
            print(dt[0])
            if dt[0] == 1:
                messagebox.showerror("Error", "Duplicate data")
                self.add_membership_detail.focus()
            else:
                sql = "insert into member_type(type,fee,nob) values(%s,%s,%s)"
                val = (ty, fee, nob)
                cur.execute(sql, val)
                db.commit()

                messagebox.showinfo("INFO", "Data Saved")
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("ERROR", "Duplicate Data")
            self.add_membership_detail.focus()

    def reset(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t1.focus()

    def cls(self):
        a=messagebox.askyesno("Ask","Are you Sure")
        if a== True:
            self.add_membership_detail.destroy()


