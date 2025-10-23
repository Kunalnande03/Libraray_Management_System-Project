from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry

db = mysql.connector.connect(host="localhost", database="libreray", username="root", password="root")
cur = db.cursor()

class edit_member:
    def __init__(self):
        self.edit_member_dt = Toplevel()
        self.edit_member_dt.title("Edit Membership Detail")

        screen_width = self.edit_member_dt.winfo_screenwidth()
        screen_height = self.edit_member_dt.winfo_screenheight()

        window_width = 550
        window_height = 500

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.edit_member_dt.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.edit_member_dt.config(bg="#a4a791")
        self.create_widgets()

    def create_widgets(self):
        frame = Frame(self.edit_member_dt, bg="#949781", bd=2, relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10, pady=10)

        self.heading = Label(frame,text="Edit Member Detail", font=("Times New Roman", 16, "bold"), width=50, bg="#0ba9aa")
        self.l0 = Label(frame,text="Member Code", font=("arial", 14, "bold"), bg="#949781")
        self.l1 = Label(frame,text="Members name", font=("arial", 14, "bold"), bg="#949781")
        self.l2 = Label(frame,text="Address ", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame,text="Contact No.  ", font=("arial", 14, "bold"), bg="#949781")
        self.l4 = Label(frame,text="Date of joining ", font=("arial", 14, "bold"), bg="#949781")
        self.l5 = Label(frame,text="Membership Type ", font=("arial", 14, "bold"), bg="#949781")
        # self.l6 = Label(text="Fee Rs. ", font=("arial", 14, "bold"))
        # self.l7 = Label(font=("arial", 14, "bold"))

        self.t1 = Entry(frame,font=("arial", 12))
        self.t2 = Text(frame,font=("arial", 12), width=20, height=4)
        self.t3 = Entry(frame,font=("arial", 12))
        self.t4 = DateEntry(frame,date_pattern="yyyy/mm/dd", font=("arial", 12), width=18)

        # self.val=("")
        self.cmb = ttk.Combobox(frame,font=("arila", 12), width=18)
        self.cmb.bind("<<ComboboxSelected>>", self.show)
        self.cmb1 = ttk.Combobox(frame,font=("arial", 12), width=18)

        self.b1 = Button(frame,text="Update", font=("arial", 14, "bold"), command=self.update, bg="#02a0a4", state=DISABLED)
        self.b2 = Button(frame,text="Delete", font=("arial", 14, "bold"), command=self.dele, bg="#02a0a4")

        self.V1 = IntVar()
        self.ch1 = Checkbutton(frame,text="If member pay the membership fee", onvalue=1, variable=self.V1, bg="#a4a791",
                               command=self.unable_button)

        self.heading.grid(row=0, column=0, pady=5, columnspan=10, sticky='ew')
        self.l0.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.cmb.grid(row=1, column=2, sticky='e')
        self.l1.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.t1.grid(row=2, column=2, sticky='e')
        self.l2.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.t2.grid(row=3, column=2, sticky='e')
        self.l3.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        self.t3.grid(row=4, column=2, sticky='e')
        self.l4.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        self.t4.grid(row=5, column=2, sticky='e')
        self.l5.grid(row=6, column=1, padx=10, pady=10, sticky='w')
        self.cmb1.grid(row=6, column=2, sticky='e')
        self.ch1.grid(row=7, column=1, padx=5, pady=5, sticky='w')
        self.b1.grid(row=8, column=1, padx=10, pady=10, sticky='w')
        self.b2.grid(row=8, column=2, padx=10, pady=10, sticky='w')

        self.loadmembership()
        self.load_member_cd()

    def loadmembership(self):
        sql = "select type from member_type "
        cur.execute(sql)
        ty = cur.fetchall()
        self.cmb1.config(values=ty)

    def load_member_cd(self):
        sql = "select m_cd from member_detail where status='A'"
        cur.execute(sql)
        cd = cur.fetchall()
        # print(cd)
        self.cmb.config(values=cd)

    def show(self, event):
        mem_cd = self.cmb.get()
        if len(mem_cd)==0:
            messagebox.showwarning("Warning","Select member Code")
            self.edit_member_dt.focus()
            self.cmb.focus()
            return

        sql = "select m_name,addr,con,doj,type from member_detail left join(member_type) using(mty_cd) where m_cd=%s"
        val = (mem_cd,)
        cur.execute(sql, val)
        data = cur.fetchone()
        # print(data)
        self.t1.config(bg="white")
        self.t2.config(bg="white")
        self.t3.config(bg="white")

        self.t1.delete(0, END)
        self.t2.delete('1.0', END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.cmb1.delete(0, END)

        self.t1.insert(0, data[0])
        self.t2.insert('1.0', data[1])
        self.t3.insert(0, data[2])
        self.t4.insert(0, data[3])
        self.cmb1.insert(0, data[4])

    def update(self):
        try:
            mem_cd = self.cmb.get()
            mem_nm = self.t1.get()
            addr = self.t2.get('1.0', END)
            con_no = self.t3.get()
            doj = self.t4.get()
            ty = self.cmb1.get()
            if len(mem_cd)==0:
                messagebox.showwarning("Warning","Select member Code")
                self.edit_member_dt.focus()
                self.cmb.focus()
                return
            sql = "select mty_cd from member_type where type=%s"
            val = (ty,)
            cur.execute(sql, val)
            ty_cd = cur.fetchone()[0]
            # print(ty_cd)
            sql1 = "update member_detail set m_name=%s,addr=%s,con=%s,doj=%s,mty_cd=%s where m_cd=%s"
            # print(sql1)
            data = (mem_nm, addr, con_no, doj, ty_cd, mem_cd)
            cur.execute(sql1, data)
            db.commit()
            messagebox.showinfo("INFO", "Data Successfully Update")
            self.edit_member_dt.focus()
        except TypeError:
            messagebox.showwarning("INFO", "Select Member code")
            self.edit_member_dt.focus()
            self.cmb.focus()


    def dele(self):
        mcd = self.cmb.get()
        mem_cnt = "select count(*) from book_issue where mem_cd=%s"
        val3 = (mcd,)
        cur.execute(mem_cnt, val3)
        tc_member = cur.fetchone()
        if tc_member[0] == 0:
            if len(mcd) == 0:
                messagebox.showwarning("Warning", "Select Member Code")
                self.edit_member_dt.focus()
                self.cmb.focus()

            else:
                a = messagebox.askquestion("ASK", "Are You Sure")
                if a == "yes":
                    sql = "update member_detail set status='D' where m_cd=%s"
                    val = (mcd,)
                    cur.execute(sql, val)
                    db.commit()
                    self.cmb.delete(0, END)
                    self.t1.delete(0, END)
                    self.t2.delete('1.0', END)
                    self.t3.delete(0, END)
                    self.t4.delete(0, END)
                    self.cmb1.delete(0, END)
                    self.loadmembership()
                    self.load_member_cd()
                    self.cmb.focus()
                else:
                    self.edit_member_dt.focus()
        else:
            messagebox.showwarning("Warning", "Member has Occupied book")
            self.edit_member_dt.focus()

    def unable_button(self):
        choice = self.V1.get()
        if choice == 1:
            self.b1.config(state=NORMAL)
        else:
            self.b1.config(state=DISABLED)



