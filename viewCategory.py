from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class viewcat:

    def __init__(self):
        self.top=Toplevel()
        self.top.title("View Category")
        self.top.label_3 = Label(self.top, text="CATEGORY",font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,pady=20)
        self.top.waraper = LabelFrame(self.top,text="Categoery View")
        self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
        self.trv = Treeview(self.top.waraper, columns=(1, 2), show="headings", height="5")
        self.trv.pack(padx=10, pady=50)
        self.trv.heading(1, text="Category")
        self.trv.heading(2, text="Category Description")
        self.trv.bind("<Double-1>", self.delcat)
        conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
        cr = conn.cursor()
        q = 'select * from category'
        cr.execute(q)
        self.result = cr.fetchall()

        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)



    #------------------Show Details---------------------------


    def delcat(self,event):
        self.temp_data = self.trv.item(self.trv.focus())['values']


        self.new= messagebox.askquestion("Delete", "Are you sure?")
        if self.new == "yes":
            conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
            cr = conn.cursor()
            q= 'delete from category where CategoryName = "{}"'.format(self.temp_data[0])
            print(q)
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchone()
        else:
            pass