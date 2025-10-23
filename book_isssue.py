from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date, datetime,timedelta
from tkcalendar import DateEntry
import mysql.connector

db = mysql.connector.connect(host="localhost", username="root", password="root", database="libreray")
cur = db.cursor()

class add_book_issue:
    def __init__(self):
        self.addbook_issue=Toplevel()
        self.addbook_issue.title("Add Book Issue")

        screen_width=self.addbook_issue.winfo_screenwidth()
        screen_height=self.addbook_issue.winfo_screenheight()

        window_width = screen_width
        window_height = 500

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.addbook_issue.geometry(f"{window_width}x{window_height}+{position_x}+50")
        self.create_widgets()


    def create_widgets(self):
        frame=Frame(self.addbook_issue,bg="#949781",bd=2,relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

        self.heading = Label(frame,text="Add Book Issue", font=("elephant", 16, "bold"), bg="#0ba9aa", width=90, fg="#ffffff")
        self.l1 = Label(frame,text="Book Code ", font=("arial", 14, "bold"), bg="#949781")
        self.l2 = Label(frame,text="Member Code ", font=("arial", 14, "bold"), bg="#949781")
        self.l3 = Label(frame,text="Issue Date ", font=("arial", 14, "bold"), bg="#949781")
        #self.l4 = Labelframe,(text="Due Date ", font=("arial", 14, "bold"),bg="#a4a791")
        self.l5 = Label(frame,text="Book Name ", font=("arial", 14, "bold"), bg="#949781")
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
        self.l31 = Label(frame,text="Fine Per Day ",font=("arial",14,"bold"),bg="#949781")
        self.l32 = Label(frame, text="5 Rs./ ", font=("arial", 14), bg="#949781")

        #self.Entry Box
        self.t1 = DateEntry(frame,date_pattern="yyyy/mm/dd", width=27)
        #self.t2 = DateEntry(date_pattern="yyyy/mm/dd",width=27)
        #self.t3 = Entry(font=("arial", 12))
        self.t1.bind('<FocusOut>', self.check)
        # Combo Box
        self.cmb0 = ttk.Combobox(frame,font=("arial", 12), width=18)
        self.cmb1 = ttk.Combobox(frame,font=("arial", 12), width=18)

        self.cmb0.bind("<<ComboboxSelected>>", self.showbook)
        self.cmb1.bind("<<ComboboxSelected>>", self.showmember)

        self.b1 = Button(frame,text="Issue", font=("times new roman", 14, "bold"), command=self.save, border=4,
                    bg="#02a0a4")  # bg="#15a193"

        self.heading.grid(row=0, column=0, pady=5, columnspan=10, sticky='ew')
        self.l1.grid(row=1, column=0, padx=15, pady=15, sticky='w')
        self.cmb0.grid(row=1, column=1, sticky='w')
        self.l2.grid(row=2, column=0, padx=15, pady=15, sticky='w')
        self.cmb1.grid(row=2, column=1, sticky='w')
        self.l3.grid(row=3, column=0, padx=15, pady=15, sticky='w')
        self.t1.grid(row=3, column=1, sticky='w')
        self.l31.grid(row=4,column=0,sticky='w',padx=15,pady=15)
        self.l32.grid(row=4,column=1,sticky='w')
        # self.l4.grid(row=4,column=0,padx=15,pady=15,sticky='w')
        # self.t2.grid(row=4,column=1,sticky='w')

        '''
        self.l5.grid(row=1, column=2, padx=10, pady=10,sticky='w')
        self.l12.grid(row=1,column=3,sticky='w')
        self.l6.grid(row=2, column=2, padx=10, pady=10,sticky='w')
        self.l13.grid(row=2,column=3,sticky='w')
        self.l7.grid(row=3, column=2, padx=10, pady=10,sticky='w')
        self.l14.grid(row=3,column=3,sticky='w')
        self.l8.grid(row=4, column=2, padx=10, pady=10,sticky='w')
        self.l15.grid(row=4,column=3,sticky='w')
        self.l9.grid(row=5, column=2, padx=10, pady=10,sticky='w')
        self.l16.grid(row=5,column=3,sticky='w')
        self.l10.grid(row=6, column=2, padx=10, pady=10,sticky='w')
        self.l17.grid(row=6,column=3,sticky='w')
        self.l11.grid(row=7, column=2, padx=10, pady=10,sticky='w')
        self.l18.grid(row=7,column=3,sticky='w')
        self.l19.grid(row=1, column=4, padx=10, pady=10,sticky='w')
        self.l24.grid(row=1,column=5,sticky='w')
        self.l20.grid(row=2, column=4, padx=10, pady=10,sticky='w')
        self.l25.grid(row=2,column=5,sticky='w')
        self.l21.grid(row=3, column=4, padx=10, pady=10,sticky='w')
        self.l26.grid(row=3,column=5,sticky='w')
        self.l22.grid(row=4, column=4, padx=10, pady=10,sticky='w')
        self.l27.grid(row=4,column=5,sticky='w')
        self.l23.grid(row=5, column=4, padx=10, pady=10,sticky='w')
        self.l28.grid(row=5,column=5,sticky='w')
        self.#l18.grid(row=6, column=4, padx=10, pady=10)
        self.#l19.grid(row=7, column=2, padx=10, pady=10)
        '''
        self.b1.grid(row=5, column=0, padx=10, pady=10)

        self.loadbook()
        self.loadmember()


    def loadbook(self):
        sql = "select b_id from book where stauts='Active' "
        cur.execute(sql)
        book_cd = cur.fetchall()
        self.cmb0.config(values=book_cd)


    def loadmember(self):
        sql = "select m_cd from member_detail where status='A'"
        cur.execute(sql)
        member_cd = cur.fetchall()
        self.cmb1.config(values=member_cd)


    def save(self):
        #check()
        try:
            b_cd = self.cmb0.get()
            m_cd = self.cmb1.get()
            issu_dt = datetime.today()
            due_date = issu_dt+timedelta(days=10)
            #print(issu_dt)
            #print(type(issu_dt))

            sql = " select b_name from book left join(book_cat) using(cat_cd) where b_id=%s "
            val = (b_cd,)
            cur.execute(sql, val)
            book_data = cur.fetchone()
            # print(book_data[0])
            nm = book_data[0]
            sql1 = "select count(*) from book where b_name=%s and stauts='Active'"
            val1 = (nm,)
            cur.execute(sql1, val1)
            tc_book = cur.fetchone()

            mem_ty="select type,nob from member_detail left join(member_type) using(mty_cd) where m_cd=%s"
            val4=(m_cd,)
            cur.execute(mem_ty,val4)
            data=cur.fetchone()
            print(data)



            if tc_book[0]<=1:
                messagebox.showwarning("Warning","Book is Out of limit")
                self.cmb0.delete(0, END)
                self.cmb1.delete(0,END)
                self.cmb0.focus()
                self.loadbook()
                self.loadmember()
                self.addbook_issue.focus()

            else:

                if len(b_cd)==0 or len(m_cd)==0:
                    messagebox.showwarning("Warning","Entry the value")
                    self.cmb0.focus()
                    return


                sql = "insert into book_issue(book_cd,mem_cd,issue_dt,due_dt,fine) values(%s,%s,%s,%s,0)"
                val = (b_cd, m_cd, issu_dt, due_date)
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo("INFO", "Book Issued")

                tcmsql = "select count(*) from book_issue where mem_cd=%s"
                val = (m_cd,)
                cur.execute(tcmsql, val)
                tc_member = cur.fetchone()

                sql1 = "update book set stauts='D' where b_id=%s"
                val1 = (b_cd,)
                cur.execute(sql1, val1)
                db.commit()
                self.cmb0.delete(0,END)
                self.cmb1.delete(0,END)
                self.l30.config(text=tc_member[0])
                self.cmb0.focus()
                self.loadbook()
                self.loadmember()

        except TypeError:
            messagebox.showerror("ERROR","Select Member and Book Code")
            self.cmb0.focus()



    def showbook(self,event):
        cd = self.cmb0.get()
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

        if tc[0]<5:
            messagebox.askokcancel("INFO","Stock is Out of Limit")
            self.addbook_issue.focus()

        self.l12.config(text=book_data[0])
        self.l13.config(text=book_data[1])
        self.l14.config(text=book_data[2])
        self.l15.config(text=book_data[3])
        self.l16.config(text=book_data[4])
        self.l17.config(text=book_data[5])
        self.l18.config(text=tc[0])
        self.l5.grid(row=1, column=2, padx=15, pady=15, sticky='w')
        self.l12.grid(row=1, column=3, sticky='w')
        self.l6.grid(row=2, column=2, padx=15, pady=15, sticky='w')
        self.l13.grid(row=2, column=3, sticky='w')
        self.l7.grid(row=3, column=2, padx=15, pady=15, sticky='w')
        self.l14.grid(row=3, column=3, sticky='w')
        self.l8.grid(row=4, column=2, padx=15, pady=15, sticky='w')
        self.l15.grid(row=4, column=3, sticky='w')
        self.l9.grid(row=5, column=2, padx=15, pady=15, sticky='w')
        self.l16.grid(row=5, column=3, sticky='w')
        self.l10.grid(row=6, column=2, padx=15, pady=15, sticky='w')
        self.l17.grid(row=6, column=3, sticky='w')
        self.l11.grid(row=7, column=2, padx=15, pady=15, sticky='w')
        self.l18.grid(row=7, column=3, sticky='w')


    def showmember(self,event):
        me_cd = self.cmb1.get()
        sql = "select m_name,addr,con,doj,type,nob from member_detail left join(member_type) using(mty_cd) where m_cd=%s"
        val = (me_cd,)
        cur.execute(sql, val)
        member_data = cur.fetchone()
        # print(member_data)

        mem_cnt = "select count(*) from book_issue where mem_cd=%s"
        val3 = (me_cd,)
        cur.execute(mem_cnt, val3)
        tc_member = cur.fetchone()



        if tc_member[0]>member_data[5]:
            messagebox.showwarning("Warning","Member Limit Cross")
            self.addbook_issue.focus()
            self.cmb0.delete(0, END)
            self.cmb1.delete(0,END)

            self.l12.config(text="")
            self.l13.config(text="")
            self.l14.config(text="")
            self.l15.config(text="")
            self.l16.config(text="")
            self.l17.config(text="")
            self.l18.config(text="")
            self.loadbook()
            self.loadmember()

        else:
            self.l24.config(text=member_data[0])
            self.l25.config(text=member_data[1])
            self.l26.config(text=member_data[2])
            self.l27.config(text=member_data[3])
            self.l28.config(text=member_data[4])
            self.l30.config(text=tc_member[0])

        self.l19.grid(row=1, column=4, padx=15, pady=15, sticky='w')
        self.l24.grid(row=1, column=5, sticky='w')
        self.l20.grid(row=2, column=4, padx=15, pady=15, sticky='w')
        self.l25.grid(row=2, column=5, sticky='w')
        self.l21.grid(row=3, column=4, padx=15, pady=15, sticky='w')
        self.l26.grid(row=3, column=5, sticky='w')
        self.l22.grid(row=4, column=4, padx=15, pady=15, sticky='w')
        self.l27.grid(row=4, column=5, sticky='w')
        self.l23.grid(row=5, column=4, padx=15, pady=15, sticky='w')
        self.l28.grid(row=5, column=5, sticky='w')
        self.l29.grid(row=6,column=4,padx=15,pady=15,sticky='w')
        self.l30.grid(row=6,column=5,sticky='w')
    # book_cd,mem_cd

    '''def fine():
        bok_cd=cmb0.get()
        sql = "select due_dt from book_issue"
        cur.execute(sql)
        dt = cur.fetchall()
        # print(dt)
        SQL1 = "SELEct count(*) from book_issue"
        cur.execute(SQL1)
        cnt = cur.fetchone()
        print(cnt)
    
        sql2="select stauts from book"
    
        for i in range(cnt[0]):
            if dt[i][0] < date.today():
                sql = "update book_issue set fine=50 where due_dt=%s"
                val = (dt[i])
                cur.execute(sql, val)
                db.commit()
        td=date.today()
        print(dt[2][0])
       print(td)
      print(type(td))
     print(type(dt))
     print(dt[3][0]<td)
    
        for i in range(cnt[0]):
            print(dt[i])
            print(date.today())
            print(str(dt[i]) < str(date.today()))
    '''

    def check(self,event):
        issue_dt=self.t1.get()
        dt=datetime.strptime(issue_dt,'%Y/%m/%d')
        #print(dt)
        #print(type(dt))

        if dt>datetime.today():
            messagebox.showwarning("Warning","Issue Date can not be grater then today")
            self.t1.focus()



#today + timedelta(days=3)



