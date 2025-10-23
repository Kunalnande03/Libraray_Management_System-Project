def log_in():
    u_nm = str.strip(t1.get())
    pasword = str.strip(t2.get())

    sql = "select count(*),username,password from user where username=%s"
    val = (u_nm,)
    cur.execute(sql, val)
    detail = cur.fetchone()
    if detail[0] == 1:
        if pasword==detail[2]:
            log.destroy()
            import main_window

    else:
        messagebox.showerror("ERROR", "User Does Not Exist")
        messagebox.showinfo("Info", "Try Again")
        log.focus()
        l3.grid(row=5, column=1, padx=2, pady=2,sticky="w")

'''
def login():
    log=Toplevel()
    log.geometry("500x200+10+10")
    log.title("Login")
    log.config(bg="#a4a791")
'''
def sign():
    log.destroy()
    import Signup


def showpas():
    che = v1.get()
    if che == 1:
        t2.config(show="")
        ch1.config(text="Hide Password",)
    else:
        t2.config(show="*")
        ch1.config(text="Show Password")


from tkinter import *
from tkinter import messagebox
import mysql.connector.connection

log=Tk()
log.geometry("500x250+260+200")
log.title("Login")
log.config(bg="#a4a791")

db=mysql.connector.connect(username="root",password="root",database="libreray",host="localhost")
cur=db.cursor()

heading=Label(log,text="Login",font=("Times New Roman",14,"bold"),bg="#0ba9aa", fg="#ffffff", pady=5,width=50)
l1 = Label(log,text="User Name ", font=("arial", 14, "bold"), bg="#a4a791")
l2 = Label(log,text="Password ", font=("arial", 14, "bold"), bg="#a4a791")
l3 = Label(log,text="Create new account",bg="#a4a791")

t1 = Entry(log,font=("arial", 12, "bold"))
t2 = Entry(log,font=("arial", 12, "bold"),show='*')

v1=IntVar()
ch1=Checkbutton(log,text="Show Password",onvalue=1,variable=v1,command=showpas,bg="#a4a791")

b1 = Button(log,text="Log in", font=("arial", 14, "bold"), padx=5, border=3, bg="#02a0a4", command=log_in)
b2=Button(log,text="Sign Up",font=("arial",14,"bold"),padx=5, border=3, bg="#02a0a4",command=sign)

heading.grid(row=0,column=0,pady=5,columnspan=10,sticky='e')
l1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
t1.grid(row=1, column=1, sticky='w')
l2.grid(row=2, column=0, padx=10, pady=10, sticky='w')
t2.grid(row=2, column=1, sticky='w')
ch1.grid(row=3,column=0,padx=10,pady=10,sticky='w')
b1.grid(row=4, column=0, sticky='e', padx=5)
b2.grid(row=4,column=1,sticky='w',padx=5)

log.mainloop()
