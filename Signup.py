def signup():
    u_name=str.strip(t1.get())
    pasword=str.strip(t2.get())
    conf_pasword=str.strip(t3.get())
    #print(pasword)

    if len(u_name)==0 or len(pasword)==0:
        messagebox.showerror("ERROR","Enter UserName and Password ")
        t1.focus()
        return

    if pasword==conf_pasword:
        sql="select count(*) from user where username=%s"
        val=(u_name,)
        cur.execute(sql,val)
        cnt=cur.fetchone()
        if cnt[0]==0:
            sql="Insert into user values(%s,%s,'Active')"
            val=(u_name,pasword)
            cur.execute(sql,val)
            db.commit()
            messagebox.showinfo("INFO","Sign Up Succecfully")
            sign.destroy()
            import main_window
        else:
            messagebox.showwarning("Warning","User Alredy Exist")
            l4.grid(row=6,column=2,sticky='w')
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.focus()

    else:
        messagebox.showerror("Error","Password Do not Match")
        t2.focus()
        t2.config()

def showpas():
    che=a1.get()
    if che==1:
        t2.config(show="")
        t3.config(show="")
        ch1.config(text="Hide Password")
    else:
        t2.config(show="*")
        t3.config(show="*")
        ch1.config(text="Show Password")

def log():
    sign.destroy()
    import login


from tkinter import *
from tkinter import messagebox
import mysql.connector

sign=Tk()
sign.geometry("500x320+250+200")
sign.title("Sign Up")
sign.config(bg="#a4a791")
db=mysql.connector.connect(username="root",password="root",database="libreray",host="localhost")
cur=db.cursor()
Heading=Label(sign,text="Sign Up",font=("Times New Roman",16,"bold"),bg="#0ba9aa", fg="#ffffff", pady=5,width=48)
l1=Label(sign,text="UserName ",font=("Times New Roman",14,"bold"),bg="#a4a791")
l2=Label(sign,text="Password ",font=("Times New Roman",14,"bold"),bg="#a4a791")
l3=Label(sign,text="Conform Password",font=("Times New Roman",14,"bold"),bg="#a4a791")
l4=Label(sign,text="Login Here",font=("arial",10),bg="#a4a791")

t1=Entry(sign,font=("arial",12))
t2=Entry(sign,font=("arial",12),show="*")
t3=Entry(sign,font=("arial",12),show="*")

a1=IntVar(sign)
ch1=Checkbutton(sign,text="Show Password",font=("arial",12,"bold"),onvalue=1,variable=a1,command=showpas,bg="#a4a791")
#ch1.bind('<Button-1>',showpas)
b1=Button(sign,text="SIGN UP",font=("arial",14,"bold"),border=3,bg="#02a0a4",command=signup)
b2=Button(sign,text="Login",font=("arial",14,"bold"),border=3,bg="#02a0a4",command=log)

Heading.grid(row=0,column=1,pady=5,columnspan=10,sticky='ew')
l1.grid(row=1,column=1,padx=10,pady=10,sticky='w')
t1.grid(row=1,column=2,sticky='w')
l2.grid(row=2,column=1,padx=10,pady=10,sticky='w')
t2.grid(row=2,column=2,sticky='w')
l3.grid(row=3,column=1,padx=10,pady=10,sticky='w')
t3.grid(row=3,column=2,sticky='w')
ch1.grid(row=4,column=1,sticky='w',padx=10,pady=10)
b1.grid(row=5,column=1,padx=10,pady=10,sticky='e')
b2.grid(row=5,column=2,sticky='w')


sign.mainloop()