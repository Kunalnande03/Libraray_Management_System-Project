import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

db = mysql.connector.connect(host="localhost", database="libreray", username="root", password="root")
cur = db.cursor()


class edit_membership:
    def __init__(self):
        self.edit_membership_detail=Toplevel()
        self.edit_membership_detail.title("Edit Membership Detail")

        screen_width=self.edit_membership_detail.winfo_screenwidth()
        screen_height=self.edit_membership_detail.winfo_screenheight()

        window_width=500
        window_height=350

        position_x=(screen_width//2)-(window_width//2)
        position_y=(screen_height//2)-(window_height//2)

        self.edit_membership_detail.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.edit_membership_detail.config(bg="#a4a791")
        self.create_widgets()

    def create_widgets(self):
        frame=Frame(self.edit_membership_detail,bg="#949781",bd=2,relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

        self.heading = Label(frame,text="Edit Membership Detail", font=("Times New Roman", 16, "bold"), width=49, fg="#fdfdfd",
                        bg="#0ba9aa")
        self.l0 = Label(frame,text="Membership Code", font=("arial", 14, "bold"), bg="#949781")
        self.l1 = Label(frame,text="Membership Type", font=("arial", 14, "bold"), bg="#949781")
        self.l2 = Label(frame,text="Fee", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame,text="No. Of Book ", font=("arial", 14, "bold"), bg="#949781")

        self.t1 = Entry(frame,font=("arila", 14))
        self.t2 = Entry(frame,font=("arila", 14))
        self.t3 = Entry(frame,font=("arila", 14))

        self.cmb = ttk.Combobox(frame,font=("arial", 14), width=18)
        self.cmb.bind("<<ComboboxSelected>>", self.show_mem_ty)

        self.b1 = Button(frame,text="Update", font=("arila", 14, "bold"), command=self.update, bg="#02a0a4")
        self.b2 = Button(frame,text="Delete", font=("arila", 14, "bold"), command=self.dele, bg="#02a0a4")

        self.heading.grid(row=0, column=0, pady=5, columnspan=10, sticky='ew')
        self.l0.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.cmb.grid(row=1, column=1, sticky='w')
        self.l1.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.t1.grid(row=2, column=1, sticky='w')
        self.l2.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.t2.grid(row=3, column=1, sticky='w')
        self.l3.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.t3.grid(row=5, column=1, sticky='w')
        self.b1.grid(row=6, column=0, padx=10, pady=10, sticky='e')
        self.b2.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        self.loadcd()


    def loadcd(self):
        sql="select mty_cd from member_type"
        cur.execute(sql)
        dt=cur.fetchall()
        self.cmb.config(values=dt)

    def show_mem_ty(self,event):
        cd=self.cmb.get()
        sql="select * from member_type where mty_cd=%s"
        val=(cd,)
        cur.execute(sql,val)
        dt=cur.fetchone()
        print(dt)

        self.t1.delete(0,END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)

        self.t1.insert(0,dt[1])
        self.t2.insert(0, dt[2])
        self.t3.insert(0, dt[3])

    def update(self):
        cd = self.cmb.get()
        mem_ty = self.t1.get()
        fee = self.t2.get()
        no_bk = self.t3.get()

        sql="update member_type set type=%s,fee=%s,nob=%s where mty_cd=%s"
        val=(mem_ty,fee,no_bk,cd)
        cur.execute(sql,val)
        db.commit()
        messagebox.showinfo("INFO","Data Successfully Update")

    def dele(self):
        try:
            mt_cd=self.cmb.get()
            if len(mt_cd)==0:
                messagebox.showerror("Error","Choose Member Code")
                self.cmb.focus()
                return

            sql="delete from member_type where mty_cd=%s"
            val=(mt_cd,)
            cur.execute(sql,val)
            messagebox.showinfo("INFO","Delete")
            self.t1.delete(0,END)
            self.t2.delete(0,END)
            self.t3.delete(0,END)
            self.cmb.delete(0,END)
            self.loadcd()
            self.cmb.focus()
        except mysql.connector.errors.IntegrityError:
            messagebox.showwarning("Warning","User Occupied book")


