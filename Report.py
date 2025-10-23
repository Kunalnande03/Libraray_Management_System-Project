from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date,datetime
from tkcalendar import DateEntry
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="root",database="libreray")
cur=db.cursor()

class show_report:
    def __init__(self):
        self.report=Toplevel()
        self.report.title("Rport")
        
        self.report.state("zoomed")
        self.create_widgets()
        
    def create_widgets(self):
        frame=Frame(self.report,bg="#949781",bd=2,relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

        self.heading = Label(frame,text="Data Report", font=("elephant", 16, "bold"), bg="#0ba9aa", fg="#ffffff", width=50)
        self.l1 = Label(frame,text="Report Date", font=("Times New Roman", 14, "bold"), bg="#949781")
        self.l2 = Label(frame,text="Total No. of Book's stock ", font=("Times New Roman", 12, "bold"), bg="#949781")
        self.l3 = Label(frame,text="Total No. of Member Join ", font=("Times New Roman", 12, "bold"), bg="#949781")
        self.l4 = Label(frame,text="Total No. of Book Issue ", font=("Times New Roman", 12, "bold"), bg="#949781")
        self.l5 = Label(frame,font=("arial", 12), bg="#949781")
        self.l6 = Label(frame,font=("arial", 12), bg="#949781")
        self.l7 = Label(frame,font=("arial", 12), bg="#949781")

        self.t1 = DateEntry(frame,date_pattern="yyyy/mm/dd", font=("Arial", 12), width=18, height=20)
        self.t1.bind("<<DateEntrySelected>>", self.repo)

        self.heading.grid(row=0, column=0, pady=5, columnspan=5)
        self.l1.grid(row=1, column=0, padx=15, pady=15, sticky='w')
        self.t1.grid(row=1, column=1, sticky='w')
        self.l2.grid(row=2, column=0, padx=15, pady=15, sticky='w')
        self.l5.grid(row=2, column=1, sticky='w')
        self.l3.grid(row=3, column=0, padx=15, pady=15, sticky='w')
        self.l6.grid(row=3, column=1, sticky='w')
        self.l4.grid(row=4, column=0, padx=15, pady=15, sticky='w')
        self.l7.grid(row=4, column=1, sticky='w')


    def repo(self,event):
        dt=self.t1.get()
        bsql="select count(*) from book where dt=%s"
        val=(dt,)
        cur.execute(bsql,val)
        b_no=cur.fetchone()
        self.l5.config(text=b_no[0])
    
        mesql="select count(*) from member_detail where doj=%s"
        cur.execute(mesql,val)
        m_no=cur.fetchone()
        self.l6.config(text=m_no[0])
    
        iss_sql="select count(*) from book_issue where issue_dt=%s"
        cur.execute(iss_sql,val)
        issue_no=cur.fetchone()
        self.l7.config(text=issue_no[0])

