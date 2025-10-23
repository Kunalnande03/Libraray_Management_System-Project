'''class login:
    def __init__(self,t1,t2):
        self.u_name=t1
        self.pas=t2


    def log(self):
        sql="select count(*),username,password from user where username=%s"
        val=(self.u_name,)
        cur.execute(sql,val)
        dt=cur.fetchone()
        #print(dt)

        if dt[0]==1:
            if dt[1]==self.u_name and dt[2]==self.pas:
                log.destroy()
                top.config(menu=menu1,bg="#a4a791")
                messagebox.showinfo("Welcome","Welcome")
            else:
                messagebox.showerror("ERROR","Incorrect Username or Password")

        else:
            messagebox.showwarning("Error","member Not found")

def newfun():
    u_name=t1.get()
    pas=t2.get()

    us=login(u_name,pas)
    us.log()
'''

def add_cat():
    bookcategory()

def edit_cat():
    edit_bookcategory()

def add_book_detail():
    book_detail()

def edit_book_dt():
    edit_book_detail()

def add_membership_dt():
    add_membership()

def edit_membership_dt():
    edit_membership()

def add_member_detail():
    add_member()

def edit_member_dt():
    edit_member()

def add_bok_issue():
    add_book_issue()

def edit_book_issue():
    edit_book_issue()

def show_all_report():
    show_report()

def show_cat():
    show_book_cat()

from tkinter import *
from tkinter import messagebox
from book_cat import bookcategory
from show_bk_dt import edit_bookcategory
from book_dtail import book_detail
from Show_bk_dtail import edit_book_detail
from member_type import add_membership
from show_mem_ty import edit_membership
from member_dt import add_member
from show_member_dt import edit_member
from book_isssue import add_book_issue
from Show_book_issue import edit_book_issue
from Report import show_report
from show_Book_cat import show_book_cat
#import mysql.connector.connection


#db=mysql.connector.connect(username="root",password="root",database="libreray",host="localhost")
#cur=db.cursor()

top=Tk()
top.state("zoomed")
#messagebox.showinfo("INFO","Welcome")
top.title("Main Window")
menubar = Menu(top)
menu1=Menu(top)
catMenu = Menu(tearoff=0)
catMenu.add_command(label="Add Book Categories",command=add_cat)
catMenu.add_command(label="Edit Book Categories",command=edit_cat)
#catMenu.add_command(label="Show Book Category",command=show_cat)

bookMenu=Menu(tearoff=0)
bookMenu.add_command(label="Add Book Detail",command=add_book_detail)
bookMenu.add_command(label="Edit Book Detail",command=edit_book_detail)

membershipMenu=Menu(tearoff=0)
membershipMenu.add_command(label="Add Membership detail",command=add_membership_dt)
membershipMenu.add_command(label="Edit Membership Detail",command=edit_membership_dt)

Membermenu=Menu(tearoff=0)
Membermenu.add_command(label="Add Member Detail",command=add_member_detail)
Membermenu.add_command(label="Edit Member Detail",command=edit_member_dt)

book_issue=Menu(tearoff=0)
book_issue.add_command(label="Add Book Issue Dtail",command=add_bok_issue)
book_issue.add_command(label="Show Book Isuue Detail",command=edit_book_issue)

report=Menu(tearoff=0)
report.add_command(label="Show Report",command=show_all_report)

menu1.add_cascade(label='Book Categories',menu=catMenu)
menu1.add_cascade(label="Book Detail",menu=bookMenu)
menu1.add_cascade(label="Member Ship Detail",menu=membershipMenu)
menu1.add_cascade(label="Member Detail",menu=Membermenu)
menu1.add_cascade(label="Book Issue Detail",menu=book_issue)
menu1.add_cascade(label="Show Report",menu=report)

top.config(menu=menu1,bg="#a4a791")
img=PhotoImage(file="Capture.PNG")
l1=Label(image=img,bg="#a4a791",relief="solid")
l1.pack(expand=True)
#l1.grid(row=1,column=1)


'''
a=messagebox.askquestion("Qustion","Do you have Alredy Account")

if a =='yes':
    log=Toplevel()
    log.geometry("500x200")
    log.title("Log in")
    log.config(bg="#a4a791")
    l1=Label(log,text="Username",font=("arial",12,"bold"),bg="#a4a791")
    l2=Label(log,text="Password",font=("arial",12,"bold"),bg="#a4a791")
    l3=Label(text="")
    t1=Entry(log)
    t2=Entry(log)

    b1=Button(log,text="Login",border=3,font=("arial",12,"bold"),command=newfun,bg="#02a0a4")

    l1.grid(row=1, column=0, padx=10, pady=10)
    t1.grid(row=1, column=1)
    l2.grid(row=2, column=0, padx=10, pady=10)
    t2.grid(row=2, column=1)
    #l3.grid(row=2,column=2)
    b1.grid(row=3, column=0, padx=10, pady=10)
    log.mainloop()

else:
    import Signup
print(a)
'''

top.mainloop()
