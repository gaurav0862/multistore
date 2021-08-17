from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview

from pymysql import *

class admin_view:

    def __init__(self):
        self.top = Toplevel()
        self.top.state("zoomed")
        self.top.title("Add Admin")
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.var_3 = StringVar()
        self.top.geometry('500x500')
        self.labl = Label(self.top,text="ADD ADMIN", font= ("Gabriola","25","italic",'bold')).pack(side= TOP,pady=5)
        self.label_1 = Label(self.top, text="EMAIL ID :: ").pack(side=TOP, pady=10)
        self.en = Entry(self.top, textvariable=self.var_1).pack(side=TOP, pady=10)
        self.lable_2 = Label(self.top, text="Password").pack(side=TOP, pady=10)
        self.enp = Entry(self.top, textvariable=self.var_2).pack(side=TOP, pady=10)
        self.lable_2 = Label(self.top, text="Add Role").pack(side=TOP, pady=10)
        self.enp = Combobox(self.top, values=("Admin", "SuperAdmin"), state="readonly")
        self.enp.pack(side=TOP, pady=10)
        self.upnew = Button(self.top, text='Update', command=self.upnew).pack(side=TOP, pady=10)


    def upnew(self):
        self.eql = self.var_1.get()
        self.pml = self.var_2.get()
        self.pml_1 = self.enp.get()

        if self.eql=="" and self.pml=="" and self.pml_1=="":
            showinfo("ADD ADMIN","Please provide input")
        else:
            conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
            cr = conn.cursor()
            q = 'insert into admin values ("{}","{}",null,"{}")'.format(self.eql, self.pml, self.pml_1)
            cr.execute(q)
            print(q)
            conn.commit()
            showinfo('Add Admin','New Admin Added Successully')

            self.top.destroy()