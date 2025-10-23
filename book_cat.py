'''
class book:
    def __init__(self):
        bok_cat=Toplevel()
        bok_cat.geometry("400x190")
        bok_cat.mainloop()
    def widtge(self):
        heading = Label(bok_cat, text="Book Category", font=("Times New Roman", 14, "bold"), bg="#0ba9aa", fg="#ffffff",
                        pady=5, width=40)
        l1 = Label(bok_cat, text="Book Category ", font=("arial", 12, "bold"), bg="#a4a791")
        # Entry
        t1 = Entry(bok_cat, font=("arila", 12), border=2)
        # button
        b1 = Button(bok_cat, text="Save", font=("arial", 12, "bold"), command=save, bg="#02a0a4", border=3)
        b2 = Button(bok_cat, text="Reset", font=("arial", 12, "bold"), command=reset, bg="#02a0a4", border=3)
        # grid
        heading.grid(row=0, column=0, columnspan=10, pady=5, sticky='ew')
        l1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        t1.grid(row=1, column=1, sticky='w')
        b1.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        b2.grid(row=2, column=1, sticky='w')
        # b2.grid(row=2, column=1)
        save()
        reset()
def save():
    book_cat = str.strip(str.title(t1.get()))

    val = (book_cat,)

    if len(book_cat)==0:
        messagebox.showwarning("Validation Error", "Kuchh to likh bhai")
        t1.focus()
    else:
        sql = "Select count(*) from book_cat where cat_name=%s"
        cur.execute(sql, val)
        dt = cur.fetchone()
        print(dt[0])
        if dt[0] == 1:
            messagebox.showerror("Error", "Duplicate data")
        else:
            sql = "insert into book_cat(cat_name) values(%s)"
            cur.execute(sql, val)
            db.commit()

            messagebox.showinfo("Save", "Data save")


def reset():
    t1.delete(0,END)
    t1.focus()


import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

db = mysql.connector.connect(host="localhost", database="libreray", username="root", password="root")
cur = db.cursor()

bok_cat = Tk()
bok_cat.geometry("400x190+350+200")
bok_cat.config(bg="#a4a791")
#label
heading = Label(bok_cat,text="Book Category", font=("Times New Roman", 14, "bold"), bg="#0ba9aa", fg="#ffffff", pady=5,width=40)
l1 = Label(bok_cat,text="Book Category ", font=("arial", 12, "bold"), bg="#a4a791")
#Entry
t1 = Entry(bok_cat,font=("arila", 12),border=2)
#button
b1 = Button(bok_cat,text="Save", font=("arial", 12, "bold"), command=save,bg="#02a0a4",border=3 )
b2=Button(bok_cat,text="Reset",font=("arial",12,"bold"),command=reset,bg="#02a0a4",border=3)
#b2 = Button(text="Show", font=("arila", 12, "bold"), command=show, bg="lightgray")
#grid
heading.grid(row=0, column=0, columnspan=10,pady=5, sticky='ew')
l1.grid(row=1, column=0, padx=10, pady=10,sticky='w')
t1.grid(row=1, column=1,sticky='w')
b1.grid(row=2, column=0,padx=10,pady=10,sticky='w')
b2.grid(row=2,column=1,sticky='w')
#b2.grid(row=2, column=1)
bok_cat.mainloop()
'''

from tkinter import *
from tkinter import messagebox
import mysql.connector

db=mysql.connector.connect(username="root",password="root",database="libreray",host="localhost")
cur=db.cursor()

class bookcategory:
    def __init__(self):
        self.bok_cat = Toplevel()

        # Set the title for the child window
        self.bok_cat.title("New Book Category Window")

        screen_width = self.bok_cat.winfo_screenwidth()
        screen_height = self.bok_cat.winfo_screenheight()

        # Define window size
        window_width = 480
        window_height = 250

        # Calculate position to center the window
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Set geometry with calculated position
        self.bok_cat.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.bok_cat.config(bg="#a4a791")

        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):


        frame = Frame(self.bok_cat, bg="#949781", bd=2, relief="solid")
        frame.pack(fill=BOTH,expand=True, padx=10, pady=10)


        # Heading Label
        heading = Label(frame, text="Add Book Category", font=("Times New Roman", 14, "bold"),
                        bg="#0ba9aa", fg="#ffffff", pady=5, width=42)
        heading.grid(row=0, column=0, columnspan=2, pady=5, sticky='ew')

        # Book Category Label
        self.l1 = Label(frame, text="Book Category ", font=("arial", 12, "bold"), bg="#a4a791")
        self.l1.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        # Entry widget
        self.t1 = Entry(frame, font=("arial", 12), border=2)
        self.t1.grid(row=1, column=1, sticky='w')

        # Buttons (Save and Reset)
        self.b1 = Button(frame, text="Save", font=("arial", 12, "bold"), bg="#02a0a4", border=3, command=self.save)
        self.b1.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.b2 = Button(frame, text="Reset", font=("arial", 12, "bold"), bg="#02a0a4", border=3, command=self.reset)
        self.b2.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    def save(self):
        book_cat = str.strip(str.title(self.t1.get()))

        val = (book_cat,)

        if len(book_cat) == 0:
            messagebox.showwarning("Validation Error", "Enter the value")
            self.t1.focus()
        else:
            sql = "Select count(*) from book_cat where cat_name=%s"
            cur.execute(sql, val)
            dt = cur.fetchone()
            print(dt[0])
            if dt[0] == 1:
                messagebox.showerror("Error", "Duplicate data")
            else:
                sql = "insert into book_cat(cat_name) values(%s)"
                cur.execute(sql, val)
                db.commit()

                messagebox.showinfo("Save", "Data save")

    def reset(self):
        self.t1.delete(0, END)
        self.t1.focus()


