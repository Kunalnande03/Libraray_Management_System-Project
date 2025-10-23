import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

db = mysql.connector.connect(host="localhost", database="libreray", username="root", password="root")
cur = db.cursor()

class edit_book_detail:
    def __init__(self):
        self.show_bk_detail=Toplevel()
        self.show_bk_detail.title("Edit Book Detail")

        screen_width=self.show_bk_detail.winfo_screenwidth()
        screen_height=self.show_bk_detail.winfo_screenheight()

        window_width = 620
        window_height = 520

        # Calculate position to center the window
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Set geometry with calculated position
        self.show_bk_detail.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.show_bk_detail.config(bg="#a4a791")
        self.create_widgets()

    def create_widgets(self):
        frame = Frame(self.show_bk_detail, bg="#949781", bd=2, relief="solid")
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.heading = Label(frame,text="Edit Book Detail", font=("arial", 16, "bold"), width=50, fg="#fdfdfd", bg="#0ba9aa")
        self.l1 = Label(frame,text="Book Code ", font=("arial", 14, "bold"), bg="#949781")
        self.l2 = Label(frame,text="Book Name ", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame,text="Book's Author Name ", font=("arial", 14, "bold"), bg="#949781")
        self.l4 = Label(frame,text="Book status", font=("arila", 14, "bold"), bg="#949781")
        self.l5 = Label(frame,text="Book Publisher ", font=("arial", 14, "bold"), bg="#949781")
        self.l6 = Label(frame,text="Book Price Rs.", font=("arial", 14, "bold"), bg="#949781")
        self.l7 = Label(frame,text="Book Category  ", font=("arial", 14, "bold"), bg="#949781")
        self.l8 = Label(frame,text="Total Number of Active Book ", font=("arial", 14, "bold"), bg="#949781")

        self.t1 = Entry(frame,font=("arila", 12))
        self.t2 = Entry(frame,font=("arila", 12))
        self.t3 = Entry(frame,font=("arila", 12))
        self.t4 = Entry(frame,font=("arila", 12))
        self.t5 = Entry(frame,font=("arila", 12))
        self.t6 = Entry(frame,font=("arila", 12))

        pub = (
        "B.P.B", "Penguin Random House India", "Rupa Publication India", "Jaico Publishing House", "Westland Books",
        "Roli Books", "Pen Macmillan India", "Aleph Book Company", "Zubaan", "Niyogi Books",
        "Arihant Publication Limited")
        self.cmb = ttk.Combobox(frame,font=("arial", 12), width=18)
        self.cmb2 = ttk.Combobox(frame,font=("arial", 12), width=18)
        self.cmb1 = ttk.Combobox(frame,values=pub, font=("arial", 12), width=18)
        self.cmb2.bind("<<ComboboxSelected>>", self.show_dt)

        self.b1 = Button(frame,text="Update", font=("arial", 14, "bold"), command=self.udate, bg="#02a0a4")
        self.b2 = Button(frame,text="Close", font=("arial", 14, "bold"), command=self.cls, bg="#02a0a4")
        self.b3 = Button(frame,text="Delete", font=("arial", 14, "bold"), command=self.dele, bg="#02a0a4")

        self.heading.grid(row=0, column=0, pady=5, columnspan=10, sticky='ew')
        self.l1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.cmb2.grid(row=1, column=1, sticky='e')
        self.l2.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.t1.grid(row=2, column=1, sticky='e')
        self.l3.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.t3.grid(row=3, column=1, sticky='e')
        self.l4.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.t4.grid(row=4, column=1, sticky='e')
        self.l5.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.cmb1.grid(row=5, column=1, sticky='e')
        self.l6.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.t5.grid(row=6, column=1, sticky='e')
        self.l7.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.cmb.grid(row=7, column=1, sticky='e')

        #self. l8.grid(row=8,column=0,padx=10,pady=10)
        #self. t6.grid(row=8,column=1)

        self.b1.grid(row=9, column=0, padx=10, pady=10, sticky='e')
        self.b3.grid(row=9, column=1, sticky='w')
        self.b2.grid(row=10, column=1, sticky='w')

        self.load_bookcd()
        self.load_cat()



    def load_cat(self):
        sql = "select cat_name from book_cat"
        cur.execute(sql)
        dt = cur.fetchall()
        self.cmb.delete(0,END)
        self.cmb.config(values=dt)


    def load_bookcd(self):
        sql = "select b_id from book"
        cur.execute(sql)
        cd = cur.fetchall()
        self.cmb2.delete(0, END)
        self.cmb2.config(values=cd)


    def show_dt(self,event):
        cd = self.cmb2.get()
        if len(cd)==0:
            messagebox.showwarning("Validation Error", "Enter The Value")
            self.cmb2.focus()
            self.show_bk_detail.focus()
            return

        sql = " select b_name,author,stauts,publisher,price,cat_name from book left join(book_cat) using(cat_cd) where b_id=%s "
        val = (cd,)
        cur.execute(sql, val)
        data = cur.fetchone()
        #print(data[0])
        nm = data[0]

        sql1 = "select count(*) from book where b_name=%s "
        val1 = (nm,)
        cur.execute(sql1, val1)
        tc = cur.fetchone()
        #print(tc)

        self.t1.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.cmb.delete(0, END)
        self.cmb1.delete(0, END)

        self.t1.insert(0, data[0])
        self.t3.insert(0, data[1])
        self.t4.insert(0, data[2])
        self.cmb1.insert(0, data[3])
        self.t5.insert(0, data[4])
        self.cmb.insert(0, data[5])


    def udate(self):
        b_cd = self.cmb2.get()
        nm = self.t1.get()
        auth = self.t3.get()
        pub=self.cmb1.get()
        st = self.t4.get()
        b_ctnm = self.cmb.get()
        pr = self.t5.get()

        if len(b_cd)==0 or len(nm) == 0 or len(auth) == 0 or len(pub) == 0 or len(b_ctnm) == 0 or len(pr) == 0:
            messagebox.showwarning("Validation Error", "Enter The Value")
            self.cmb2.focus()
            self.show_bk_detail.focus()
            return

        sql = "select cat_cd from book_cat where cat_name=%s "
        data = (b_ctnm,)
        print(data)
        cur.execute(sql,data)
        cat_cd = cur.fetchone()
        ct_cd = cat_cd[0]


        sql = "update book set b_name=%s,author=%s,stauts=%s,publisher=%s,price=%s,cat_cd=%s where b_id=%s"
        val = (nm,auth,st,pub,pr,ct_cd,b_cd)
        cur.execute(sql, val)
        db.commit()

        messagebox.showinfo("INFO", "Data update")


    def cls(self):
        a = messagebox.askyesno("ASK", "Are you sure")
        print(a)
        if a == True:
            self.show_bk_detail.destroy()

    def dele(self):
        cd=self.cmb2.get()

        if len(cd)==0:
            messagebox.showwarning("Validation Error", "Kuchh to likh bhai")
            self.cmb2.focus()
            return

        sql="delete from book where b_id=%s"
        val=(cd,)
        cur.execute(sql,val)
        db.commit()
        messagebox.showinfo("INFO","Delete Successfully")

        self.cmb2.delete(0, END)
        self.t1.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.cmb.delete(0, END)
        self.cmb1.delete(0, END)
        self.cmb2.focus()




