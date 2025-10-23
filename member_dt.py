from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import date,datetime
from tkcalendar import DateEntry

db = mysql.connector.connect(host="localhost", database="libreray", username="root", password="root")
cur = db.cursor()

class add_member:
    def __init__(self):
        self.add_member_dt=Toplevel()
        self.add_member_dt.title("Add Member Detail")

        screen_width=self.add_member_dt.winfo_screenheight()
        screen_height=self.add_member_dt.winfo_screenheight()

        window_width=670
        window_height=500

        position_x=(screen_width//2)-(window_width//2)
        position_y=(screen_height//2)-(window_height//2)

        self.add_member_dt.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.add_member_dt.config(bg="#a4a791")
        self.create_widgets()

    def create_widgets(self):
        frame=Frame(self.add_member_dt,bg="#949781",bd=2,relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

        self.heading = Label(frame, text="Add Member Detail", font=("Times New Roman", 16, "bold"), width=55, bg="#0ba9aa")
        self.l1 = Label(frame, text="Members name", font=("arial", 14, "bold"), bg="#949781")
        self.l2 = Label(frame, text="Address ", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame, text="Contact No.  ", font=("arial", 14, "bold"), bg="#949781")
        self.l4 = Label(frame, text="Date of joining ", font=("arial", 14, "bold"), bg="#949781")
        self.l5 = Label(frame, text="Select membership type ", font=("arial", 14, "bold"), bg="#949781")
        self.l6 = Label(frame, text="Fee Rs. ", font=("arial", 14, "bold"), bg="#949781")
        self.l7 = Label(frame, font=("arial", 12, "bold"), bg="#949781")
        self.l8 = Label(frame, font=(10), bg="#949781")
        self.l10 = Label(frame, text="No. Of Book in a week", font=("arial", 14, "bold"), bg="#949781")
        self.l9 = Label(frame, font=("arial", 12, "bold"), bg="#949781")

        self.t1 = Entry(frame, font=("arial", 12), )
        self.t2 = Text(frame,font=("arial", 12), width=20, height=4)
        self.t3 = Entry(frame, font=("arial", 12))
        self.t4 = DateEntry(frame, date_pattern="yyyy/mm/dd", font=("arial", 12), width=18)
        #self.t1.bind('<FocusOut>',check)
        #self.t2.bind('<FocusOut>',check1)
        self.t3.bind('<FocusOut>', self.check2)
        self.t4.bind('<FocusOut>', self.check3)

        self.cmb = ttk.Combobox(frame, font=("arila", 12), width=18)
        self.cmb.bind("<<ComboboxSelected>>", self.fee)

        self.b1 = Button(frame, text="Save", font=("arial", 14, "bold"), command=self.save, bg="#02a0a4")

        self.heading.grid(row=0, column=1, pady=5, columnspan=10, sticky='ew')
        self.l1.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.t1.grid(row=1, column=2, sticky='w')
        self.l2.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.t2.grid(row=2, column=2, sticky='w')
        self.l3.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.t3.grid(row=3, column=2, sticky='w')
        self.l4.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        self.t4.grid(row=4, column=2, sticky='w')
        self.l5.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        self.cmb.grid(row=5, column=2, sticky='w')
        self.l6.grid(row=6, column=1, padx=10, pady=10, sticky='w')
        self.l10.grid(row=7, column=1, padx=10, pady=10, sticky='w')
        self.l8.grid(row=3, column=3, sticky='w')
        self.b1.grid(row=8, column=1, padx=10, pady=10, sticky='e')

        self.loadmembership()


    def loadmembership(self):
        sql = "select type from member_type"
        cur.execute(sql)
        ty = cur.fetchall()
        self.cmb.config(values=ty)


    def fee(self,event):
        ty = self.cmb.get()
        sql = "select * from member_type where type=%s"
        val = (ty,)
        cur.execute(sql, val)
        fee = cur.fetchone()
        #print(fee)
        self.l7.config(text=fee[2])
        self.l9.config(text=fee[3])

        self.l7.grid(row=6, column=2, sticky='e')
        self.l9.grid(row=7,column=2,sticky='e')


    def save(self):
        ty = self.cmb.get()
        nm = str.strip(str.title(self.t1.get()))
        adr = str.strip(self.t2.get('1.0',END))
        cont = str.strip(self.t3.get())
        doj = str.strip(self.t4.get())

        if len(ty)==0 or len(nm)==0 or len(adr)==0 or len(cont)==0 or len(doj)==0:
            messagebox.showerror("Error","Fill The Entry Box")
            self.t1.focus()
            self.add_member_dt.focus()
            return

        sql = "select mty_cd from member_type where type=%s"
        val = (ty,)
        cur.execute(sql, val)
        mty = cur.fetchone()
        # print(mty)
        mty_cd = mty[0]

        sql = "insert into member_detail(m_name,addr,con,doj,mty_cd,status) values(%s,%s,%s,%s,%s,'A')"
        val = (nm, adr, cont, doj, mty_cd)
        cur.execute(sql, val)
        db.commit()

        a = messagebox.showinfo("INFo", "Information Save")
        self.add_member_dt.focus()
        print(a)

    '''
    def check(event):
        nm=t1.get()
        if len(nm)<2:
            t1.focus()
    
    def check1(event):
        pass
    #    addr=t2.get()
    #   if len(addr)<10:
    #      t2.focus()
    '''
    def check2(self,event):
        cont=self.t3.get()
        if len(cont)<10 or len(cont)>10 or len(cont)==0:
            self.t3.focus()
            self.l8.config(text="*Number should be 10 digits",fg="red")


    def check3(self,event):
        dt=datetime.strptime(self.t4.get(),'%Y/%m/%d')
        #print(dt)
        if dt>datetime.today():
            messagebox.showwarning("Error","Date can not be greater then today date")
            self.add_member_dt.focus()

    def reset(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.cmb.delete(0,END)


