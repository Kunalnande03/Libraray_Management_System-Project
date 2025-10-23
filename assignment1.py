from tkinter import*
import mysql.connector
db=mysql.connector.connect(host="localhost",username="root",passward="root",database="hospital")
cur=db.cursor()
top=Tk()
top.geometry("500x500")
l1=Label(text="NAME",font=("arial",20))
l2=Label(text="CONTACTN0",font=("arial",20))
l3=Label(text="EMERGENCYNO",font=("arial",20))
l4=Label("CONSULTATION FEE",font=("arial",20))
l5=Label(text="TOTAL PATIENTS",font=("arial",20))
