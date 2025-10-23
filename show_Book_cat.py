from tkinter import *
from tkinter import ttk

class show_book_cat:
    def __init__(self):
        self.show_book_category=Toplevel()
        self.show_book_category.title("Show Book Category")

        self.show_book_category.state("zoomed")
        self.create_widgets()
    def create_widgets(self):
        heading = Label(self.show_book_category, text="Show All Book Category",font=("arial", 18, "bold"), fg="#ffffff", bg="#0ba9aa")#, width=150)
        heading.pack(fill=BOTH)

        frame=Frame(self.show_book_category,bg="#ffffff",bd=2,relief="solid")
        frame.pack(fill=BOTH,expand=True,padx=10,pady=10)
        scrollbarx=Scrollbar(frame,orient=HORIZONTAL)
        scrollbary=Scrollbar(frame,orient=VERTICAL)
        cat_table=ttk.Treeview(frame,column=('Categorie Code','Categorie Name'))

        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT,fill=Y)
        cat_table.pack(fill=BOTH,expand=1)

        cat_table.heading('Categorie Code',text='Code')
        cat_table.heading("Categorie Name",text='Name')

    def show_data(self):
        pass




