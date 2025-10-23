from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date, datetime, timedelta
import mysql.connector
from tkcalendar import DateEntry

db = mysql.connector.connect(host="localhost", username="root", password="root", database="libreray")
cur = db.cursor()


class edit_book_issue:
    def __init__(self):
        self.show_book_issue = Toplevel()
        self.show_book_issue.title("Add Book Issue")

        screen_width = self.show_book_issue.winfo_screenwidth()
        screen_height = self.show_book_issue.winfo_screenheight()

        window_width = screen_width
        window_height = 500

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.show_book_issue.geometry(f"{window_width}x{window_height}+{position_x}+50")
        self.create_widgets()

    def create_widgets(self):
        frame=Frame(self.show_book_issue,bd=2,bg="#949781",relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

        self.heading = Label(frame,text="Add Book Issue", font=("elephant", 16, "bold"), bg="#0ba9aa", fg="#ffffff", width=90)
        self.l1 = Label(frame,text="Book Code ", font=("arial", 14, "bold"), bg="#949781")
        self.l2 = Label(frame,text="Member Code ", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame,text="Issue Date ", font=("arial", 14, "bold"), bg="#949781")
        self.l4 = Label(frame,text="Due Date ", font=("arial", 14, "bold"), bg="#949781")
        self.l5 = Label(frame,text="Book Name ", font=("arial", 14, "bold"), bg="#949781")
        self.l31 = Label(frame,text="Fine Rs.", font=("arial", 14, "bold"), bg="#949781")
        self.l6 = Label(frame,text="Book's Author Name ", font=("arial", 14, "bold"), bg="#949781")
        self.l7 = Label(frame,text="Book status", font=("arila", 14, "bold"), bg="#949781")
        self.l8 = Label(frame,text="Book Publisher ", font=("arial", 14, "bold"), bg="#949781")
        self.l9 = Label(frame,text="Book Price Rs.", font=("arial", 14, "bold"), bg="#949781")
        self.l10 = Label(frame,text="Book Category  ", font=("arial", 14, "bold"), bg="#949781")
        self.l11 = Label(frame,text="Books in stock ", font=("arial", 14, "bold"), bg="#949781")
        self.l12 = Label(frame,font=("arial", 10), bg="#949781")
        self.l13 = Label(frame,font=("arial", 10), bg="#949781")
        self.l14 = Label(frame,font=("arial", 10), bg="#949781")
        self.l15 = Label(frame,font=("arial", 10), bg="#949781")
        self.l16 = Label(frame,font=("arial", 10), bg="#949781")
        self.l17 = Label(frame,font=("arial", 10), bg="#949781")
        self.l18 = Label(frame,font=("arial", 10), bg="#949781")
        self.l19 = Label(frame,text="Members name", font=("arial", 14, "bold"), bg="#949781")
        self.l20 = Label(frame,text="Address ", font=("arial", 14, "bold"), bg="#949781")
        self.l21 = Label(frame,text="Contact No.  ", font=("arial", 14, "bold"), bg="#949781")
        self.l22 = Label(frame,text="Date of joining ", font=("arial", 14, "bold"), bg="#949781")
        self.l23 = Label(frame,text="Membership Type ", font=("arial", 14, "bold"), bg="#949781")
        self.l24 = Label(frame,font=("arial", 10), bg="#949781")
        self.l25 = Label(frame,font=("arial", 10), bg="#949781")
        self.l26 = Label(frame,font=("arial", 10), bg="#949781")
        self.l27 = Label(frame,font=("arial", 10), bg="#949781")
        self.l28 = Label(frame,font=("arial", 10), bg="#949781")
        self.l29 = Label(frame,text="Total no of book Member have", font=("arial", 14, "bold"), bg="#949781")
        self.l30 = Label(frame,font=("arial", 10), bg="#949781")

        # Entry Box
        self.t1 = Entry(frame,font=("arial", 12))
        self.t2 = Entry(frame,font=("arial", 12))
        self.t3 = Entry(frame,font=("arial", 12))
        # Combo Boxframe,
        self.cmb0 = ttk.Combobox(frame,font=("arial", 12), width=18)
        self.cmb1 = ttk.Combobox(frame,font=("arial", 12), width=18)

        self.cmb0.bind("<<ComboboxSelected>>", self.showbook)
        self.cmb1.bind("<<ComboboxSelected>>", self.showmember)

        self.b1 = Button(frame,text="Return", font=("times new roman", 14, "bold"), command=self.ret, bg="#02a0a4")  # bg="#15a193"

        self.heading.grid(row=0, column=0, pady=10, columnspan=10, sticky='ew')
        self.l2.grid(row=1, column=0, padx=15, pady=15, sticky='w')
        self.cmb1.grid(row=1, column=1, sticky='w')
        self.l1.grid(row=2, column=0, padx=15, pady=15, sticky='w')
        self.cmb0.grid(row=2, column=1, sticky='w')
        self.l3.grid(row=3, column=0, padx=15, pady=15, sticky='w')
        self.t1.grid(row=3, column=1, sticky='w')
        self.l4.grid(row=4, column=0, padx=15, pady=15, sticky='w')
        self.t2.grid(row=4, column=1, sticky='w')
        self.l31.grid(row=5, column=0, sticky='w', padx=15, pady=15)
        self.t3.grid(row=5, column=1, sticky='w')
        '''
        self.l5.grid(row=1, column=4, padx=10, pady=10, sticky='w')
        self.l6.grid(row=2, column=4, padx=10, pady=10, sticky='w')
        self.l7.grid(row=3, column=4, padx=10, pady=10, sticky='w')
        self.l8.grid(row=4, column=4, padx=10, pady=10, sticky='w')
        self.l9.grid(row=5, column=4, padx=10, pady=10, sticky='w')
        self.l10.grid(row=6, column=4, padx=10, pady=10, sticky='w')
        self.# l11.grid(row=7, column=4, padx=10, pady=10,sticky='w')
        self.l19.grid(row=1, column=2, padx=10, pady=10, sticky='w')
        self.l20.grid(row=2, column=2, padx=10, pady=10, sticky='w')
        self.l21.grid(row=3, column=2, padx=10, pady=10, sticky='w')
        self.l22.grid(row=4, column=2, padx=10, pady=10, sticky='w')
        self.l23.grid(row=5, column=2, padx=10, pady=10, sticky='w')
        self.# l18.grid(row=6, column=2, padx=10, pady=10)
        self.# l19.grid(row=7, column=2, padx=10, pady=10)
        self.'''
        self.b1.grid(row=6, column=0, padx=10, pady=15, sticky='e')
        # loadbook()
        self.loadmember()
        # fine()

    def loadbook(self):
        m_cd = self.cmb1.get()
        sql = "select book_cd from book_issue where mem_cd=%s "
        val = (m_cd,)
        cur.execute(sql, val)
        book_cd = cur.fetchall()
        # print(book_cd)
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.cmb0.delete(0, END)
        self.t3.delete(0, END)
        self.cmb0.config(values=book_cd)


    def loadmember(self):
        sql = "select distinct(mem_cd) from book_issue "
        cur.execute(sql)
        member_cd = cur.fetchall()
        # print(member_cd)
        self.cmb1.delete(0, END)
        self.cmb1.config(values=member_cd)


    def show_issue_dtail(self):
        b_cd = self.cmb0.get()
        m_cd = self.cmb1.get()
        sql = "select issue_dt,due_dt,fine from book_issue where book_cd=%s and mem_cd=%s"
        val = (b_cd, m_cd)
        cur.execute(sql, val)
        dt = cur.fetchone()
        # print(dt)

        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)

        self.t1.insert(0, dt[0])
        self.t2.insert(0, dt[1])


    def showbook(self,event):
        cd = self.cmb0.get()
        print(cd)
        sql = " select b_name,author,stauts,publisher,price,cat_name from book left join(book_cat) using(cat_cd) where b_id=%s "
        val = (cd,)
        cur.execute(sql, val)
        book_data = cur.fetchone()
        # print(book_data[0])
        nm = book_data[0]
        sql1 = "select count(*) from book where b_name=%s and stauts='Active'"
        val1 = (nm,)
        cur.execute(sql1, val1)
        tc = cur.fetchone()
        self.l12.config(text=book_data[0])
        self.l13.config(text=book_data[1])
        self.l14.config(text=book_data[2])
        self.l15.config(text=book_data[3])
        self.l16.config(text=book_data[4])
        self.l17.config(text=book_data[5])
        self.l18.config(text=tc[0])

        self.l5.grid(row=1, column=4, padx=15, pady=15, sticky='w')
        self.l12.grid(row=1, column=5, sticky='w')
        self.l6.grid(row=2, column=4, padx=15, pady=15, sticky='w')
        self.l13.grid(row=2, column=5, sticky='w')
        self.l7.grid(row=3, column=4, padx=15, pady=15, sticky='w')
        self.l14.grid(row=3, column=5, sticky='w')
        self.l8.grid(row=4, column=4, padx=15, pady=15, sticky='w')
        self.l15.grid(row=4, column=5, sticky='w')
        self.l9.grid(row=5, column=4, padx=15, pady=15, sticky='w')
        self.l16.grid(row=5, column=5, sticky='w')
        self.l10.grid(row=6, column=4, padx=15, pady=15, sticky='w')
        self.l17.grid(row=6, column=5, sticky='w')
        # self.l11.grid(row=7, column=2, padx=10, pady=10,sticky='w')
        # self.l18.grid(row=7, column=3,sticky='w')
        self.show_issue_dtail()
        self.fine()


    def showmember(self,event):
        me_cd = self.cmb1.get()
        sql = "select m_name,addr,con,doj,type from member_detail left join(member_type) using(mty_cd) where m_cd=%s"
        val = (me_cd,)
        cur.execute(sql, val)
        member_data = cur.fetchone()
        mem_cnt = "select count(*) from book_issue where mem_cd=%s"
        val3 = (me_cd,)
        cur.execute(mem_cnt, val3)
        tc_member = cur.fetchone()

        # print(member_data)
        self.l24.config(text=member_data[0])
        self.l25.config(text=member_data[1])
        self.l26.config(text=member_data[2])
        self.l27.config(text=member_data[3])
        self.l28.config(text=member_data[4])
        self.l30.config(text=tc_member[0])

        self.l19.grid(row=1, column=2, padx=15, pady=15, sticky='w')
        self.l24.grid(row=1, column=3, sticky='w')
        self.l20.grid(row=2, column=2, padx=15, pady=15, sticky='w')
        self.l25.grid(row=2, column=3, sticky='w')
        self.l21.grid(row=3, column=2, padx=15, pady=15, sticky='w')
        self.l26.grid(row=3, column=3, sticky='w')
        self.l22.grid(row=4, column=2, padx=15, pady=15, sticky='w')
        self.l27.grid(row=4, column=3, sticky='w')
        self.l23.grid(row=5, column=2, padx=15, pady=15, sticky='w')
        self.l28.grid(row=5, column=3, sticky='w')
        self.l29.grid(row=6, column=2, padx=15, pady=15, sticky='w')
        self.l30.grid(row=6, column=3, sticky='w')
        self.loadbook()
        self.l12.config(text='')
        self.l13.config(text='')
        self.l14.config(text='')
        self.l15.config(text='')
        self.l16.config(text='')
        self.l17.config(text='')


    # book_cd,mem_cd

    def ret(self):
        b_cd = self.cmb0.get()
        mcd = self.cmb1.get()
        fine = int(self.t3.get())
        # print(fine)

        if fine == 0:
            sql = "delete from book_issue where book_cd=%s and mem_cd=%s"
            val1 = (b_cd, mcd)
            cur.execute(sql, val1)
            messagebox.showinfo("INFO", "Member Return the book and pay the fine")
            self.show_book_issue.focus()
            self.cmb0.delete(0, END)
            self.t1.delete(0, END)
            self.t2.delete(0, END)
            self.t3.delete(0, END)

            self.l12.config(text="")
            self.l13.config(text="")
            self.l14.config(text="")
            self.l15.config(text="")
            self.l16.config(text="")
            self.l17.config(text="")
            self.l18.config(text="")

            self.loadbook()
            self.loadmember()
            self.cmb1.focus()
            sql1 = "update book set stauts='Active' where b_id=%s"
            val = (b_cd,)
            cur.execute(sql1, val)
            db.commit()

        else:
            messagebox.showwarning("Warning", "Pay the fine first")
            self.show_book_issue.focus()



    def fine(self):
        bok_cd = self.cmb0.get()
        due_dt = self.t2.get()
        print(due_dt)
        dt = datetime.strptime(due_dt, '%Y-%m-%d')

        overdue_dt = (datetime.today() - dt).days
        fine = overdue_dt * 5
        print(overdue_dt)
        print(fine)

        if fine >= 0:
            UPsql3 = "update book_issue set fine=%s where book_cd=%s"
            val = (fine, bok_cd)
            cur.execute(UPsql3, val)
            db.commit()
            sql = "select fine from book_issue where book_cd=%s"
            val = (bok_cd,)
            cur.execute(sql, val)
            fien = cur.fetchone()
            self.t3.delete(0, END)
            self.t3.insert(0, fien[0])
        else:
            sql = "select fine from book_issue where book_cd=%s"
            val = (bok_cd,)
            cur.execute(sql, val)
            fien = cur.fetchone()
            self.t3.delete(0, END)
            self.t3.insert(0, fien[0])
        '''
        #print(type(cnt[0]))
        #print(type(fi))
        #Sesql2="select stauts from book where b_id=%s"
        #cur.execute(Sesql2,val)
        #B_status=cur.fetchone()
        #print(type(B_status))
        #print(type(date.today()))
        
        tup=("","")
        while B_status[0]!='Active':
            if tup[0]!=date.today() or tup[1]!=bok_cd:
                if dt[0]<date.today():
                    fi+=5
                    val=(fi,bok_cd)
                    UPsql3="update book_issue set fine=%s where book_cd=%s"
                    cur.execute(UPsql3,val)
                    db.commit()
                    sql="select fine from book_issue where book_cd=%s"
                    val=(bok_cd,)
                    cur.execute(sql,val)
                    fien=cur.fetchone()
                    t3.delete(0,END)
                    t3.insert(0,fien)
                    li=list(tup)
                    li.insert(0,date.today())
                    li.insert(1,bok_cd)
                    tup=tuple(li)
                    break
        '''

        '''#if tup[0] != date.today() or tup[1] != bok_cd:
        if dt < datetime.today():
                fi += 5
                val = (fi, bok_cd)
                UPsql3 = "update book_issue set fine=%s where book_cd=%s"
                cur.execute(UPsql3, val)
                db.commit()
                sql = "select fine from book_issue where book_cd=%s"
                val = (bok_cd,)
                cur.execute(sql, val)
                fien = cur.fetchone()
                t3.delete(0, END)
                t3.insert(0, fien[0])
    
        
        '''

