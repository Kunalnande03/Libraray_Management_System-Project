import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date,datetime
db = mysql.connector.connect(host="localhost", database="libreray", username="root", password="root")
cur = db.cursor()


class book_detail:
    def __init__(self):
        self.book_dt=Toplevel()
        self.book_dt.title("Add Book Detail")
        screen_width = self.book_dt.winfo_screenwidth()
        screen_height = self.book_dt.winfo_screenheight()

        # Define window size
        window_width = 620
        window_height = 460

        # Calculate position to center the window
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Set geometry with calculated position
        self.book_dt.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.book_dt.config(bg="#a4a791")
        self.create_widgets()

    def create_widgets(self):
        frame=Frame(self.book_dt,bg="#949781",bd=2,relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

        self.heading = Label(frame, text="Add Book Detail", font=("arial", 16, "bold"), width=55, fg="#fdfdfd",
                        bg="#0ba9aa")
        # l1 = Label(text="Enter Book Code ", font=("arial", 14, "bold"))
        self.l2 = Label(frame, text="Book Name ", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame, text="Book's Author Name ", font=("arial", 14, "bold"), bg="#949781")
        self.l5 = Label(frame, text="Book Publisher ", font=("arial", 14, "bold"), bg="#949781")
        self.l6 = Label(frame, text="Book Price ", font=("arial", 14, "bold"), bg="#949781")
        self.l7 = Label(frame, text="Book Category  ", font=("arial", 14, "bold"), bg="#949781")
        self.l8 = Label(frame, text="Total No. of Book ", font=("arial", 14, "bold"), bg="#949781")

        # t1 = Entry(font=("arila", 12))
        self.t2 = Entry(frame, font=("arial", 12))
        self.t3 = Entry(frame, font=("arial", 12))
        self.t4 = Entry(frame, font=("arial", 12))
        self.t5 = Entry(frame, font=("arial", 12))
        self.t6 = Entry(frame, font=("arial", 12))
        self.t7 = Entry(frame, font=("arial", 12))

        pub = (
        "B.P.B", "Penguin Random House India", "Rupa Publication India", "Jaico Publishing House", "Westland Books"
        , "Roli Books", "Pen Macmillan India", "Aleph Book Company", "Zubaan", "Niyogi Books"
        , "Arihant Publication Limited")

        self.cmb = ttk.Combobox(frame, font=("arial", 12), width=18)
        self.cmb1 = ttk.Combobox(frame, values=pub, font=("arial", 12), width=18)

        self.b1 = Button(frame, text="Save", font=("arial", 14, "bold"), command=self.save_book_dt, bg="#02a0a4", width=8)
        self.b2 = Button(frame, text="Close", font=("arial", 14, "bold"), command=self.cls, bg="#02a0a4")
        self.b3 = Button(frame, text="Reset", font=("arial", 14, "bold"), command=self.reset, bg="#02a0a4")

        #self. l1.grid(row=1, column=0, padx=10, pady=10)
        #self. t1.grid(row=1, column=1)
        self.heading.grid(row=0, column=0, pady=5, columnspan=10, sticky='ew')
        self.l2.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.t2.grid(row=2, column=1, sticky='w')
        self.l3.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.t3.grid(row=3, column=1, sticky='w')
        #self.l4.grid(row=4,column=0, padx=10, pady=10)
        #self.t4.grid(row=4,column=1)
        self.l5.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.cmb1.grid(row=5, column=1, sticky='w')
        self.l6.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.t5.grid(row=6, column=1, sticky='w')
        self.l7.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.cmb.grid(row=7, column=1, sticky='w')
        self.l8.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        self.t7.grid(row=8, column=1, sticky='w')
        self.b1.grid(row=9, column=0, padx=10, pady=10, sticky='e')
        self.b3.grid(row=9, column=1, sticky='w')
        self.b2.grid(row=10, column=1, sticky='w',)

        self.load_cat()


    def load_cat(self):
        sql = "select cat_name from book_cat"
        cur.execute(sql)
        dt = cur.fetchall()
        self.cmb.config(values=dt)

    def save_book_dt(self):
        try:
            #b_cd = t1.get()
            b_name = str.strip(str.title(self.t2.get()))
            auth_name =str.strip( str.title(self.t3.get()))
            #st = t4.get()
            pub = str.strip(str.title(self.cmb1.get()))
            price = str.strip(self.t5.get())
            cat_name = str.strip(str.title(self.cmb.get()))
            dat=datetime.today()
            t_no_b=int(str.strip(self.t7.get()))

            #cmb1.config(values=pub)
            sql3="select b_id from "


            if len(b_name) == 0 or len(auth_name) == 0 or len(pub) == 0 or len(cat_name) == 0 or len(price) == 0:
                messagebox.showwarning("Validation Error", "Fill The Entry Box")
                self.t2.focus()
                return

            sql = "select cat_cd from book_cat where cat_name=%s"
            dt = (cat_name,)
            cur.execute(sql, dt)
            cat_cd = cur.fetchone()
            cd = cat_cd[0]


    #(b_cd,b_name,author,stauts,publisher,price,cat_cd)
            for i in range(t_no_b):
                sql1 = "Select count(*) from book"
                cur.execute(sql1, )
                dt = cur.fetchone()
                print(dt[0])
                b_cd = dt[0] + 1

                sql2 = "insert into book values(%s,%s,%s,'Active',%s,%s,%s,%s)"
                val = ( b_cd,b_name, auth_name, pub, price, cd,dat)
                cur.execute(sql2, val)
                db.commit()

            messagebox.showinfo("INFO", "Data Saved")
            self.book_dt.focus()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Error", "Duplicate Code")
        except TypeError:
            messagebox.showinfo("INFO","Choose Book category")

    def cls(self):
        a=messagebox.askyesno("ASK","Are you sure")
        print(a)
        if a == True:
            self.book_dt.destroy()
        else:
            self.book_dt.focus()

    def reset(self):
        self.cmb.delete(0,END)
        self.cmb1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.t5.delete(0,END)
        self.t6.delete(0,END)
        self.t2.focus()



