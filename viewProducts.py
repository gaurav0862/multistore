from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class viewpro:

    def __init__(self):
        self.top = Toplevel()
        self.top.label_3 = Label(self.top, text="Products", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,pady=20)
        self.top.title("View Products")
        self.top.waraper = LabelFrame(self.top, text="Categoery View")
        self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
        self.trv1 = Treeview(self.top.waraper, columns=(1, 2, 3, 4, 5), show="headings", height="5")
        self.trv1.pack(padx=10, pady=50)
        self.trv1.heading(1, text="Product ID")
        self.trv1.heading(2, text="Product Name")
        self.trv1.heading(3, text="Product Price")
        self.trv1.heading(4, text="Product Description")
        self.trv1.heading(5, text="category Name")
        self.trv1.bind("<Double-1>", self.show_details)
        conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
        cr = conn.cursor()
        q = 'select * from products'
        cr.execute(q)
        self.result = cr.fetchall()

        for i in self.trv1.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv1.insert("", END, value=i)

    def show_details(self, event):
            self.temp_data = self.trv1.item(self.trv1.focus())['values']
            self.top = Toplevel()
            self.top.geometry('500x500')
            self.label_1 = Label(self.top, text="Product ID :: ").pack(side=TOP, pady=10)
            self.em1 = Entry(self.top)
            self.em1.insert(0, self.temp_data[0])
            self.em1.pack(side=TOP, pady=10)
            self.label_2 = Label(self.top, text="Product Name :: ").pack(side=TOP, pady=10)
            self.pm2 = Entry(self.top)
            self.pm2.insert(0, self.temp_data[1])
            self.pm2.pack(side=TOP, pady=10)
            self.label_3 = Label(self.top, text="Product Price :: ").pack(side=TOP, pady=10)
            self.ll2 = Entry(self.top)
            self.ll2.insert(0, self.temp_data[2])
            self.ll2.pack(side=TOP, pady=10)
            self.label_4 = Label(self.top, text="Product Description :: ").pack(side=TOP, pady=10)
            self.ll3 = Entry(self.top)
            self.ll3.insert(0, self.temp_data[3])
            self.ll3.pack(side=TOP, pady=10)
            self.label_5 = Label(self.top, text="Category Name :: ").pack(side=TOP, pady=10)
            conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
            cr = conn.cursor()
            q = 'select CategoryName from Category'
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchall()
            x = []
            for i in self.result:
                x.append(i[0])
            self.enl = Combobox(self.top, values=x, state="readonly")
            print(self.enl)
            self.current = x.index(str(self.temp_data[4]))
            self.enl.current(self.current)
            self.enl.pack(side=TOP, pady=10)
            self.enl.config(state='readonly')
            self.enl.insert(0, self.temp_data[4])

            self.upbtn = Button(self.top, text="update", command=self.newupdate)
            self.upbtn.pack()
            self.delbtn = Button(self.top, text="Delete", command=self.delupdate)
            self.delbtn.pack()

# --------------UPDATE EXISTING DATA--------------

    def newupdate(self):
            self.pnam = self.pm2.get()
            self.pp = self.ll2.get()
            self.pd = self.ll3.get()
            self.pc = self.enl.get()
            conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
            cr = conn.cursor()
            q = 'update products set PName="{}",PPrice="{}",PDescription="{}",CatergoryName="{}" where PID="{}"'.format(self.pnam, self.pp, self.pd,self.pc,self.em1.get() )
            print(q)
            cr.execute(q)
            print(q)
            conn.commit()
            self.result = cr.fetchall()
            messagebox.showinfo("","sucessfull added")

            q = 'select * from products'
            cr.execute(q)
            self.result = cr.fetchall()

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in self.result:
                self.trv1.insert("", END, value=i)
# -------DELETE ALL SELECTED DATA----------------

    def delupdate(self):
            self.eml = self.em1.get()
            conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
            cr = conn.cursor()
            q = 'delete from products where PID="{}"'.format(self.eml)

            cr.execute(q)
            print(q)
            conn.commit()
            # cr = conn.cursor()
            q = 'select * from products'
            cr.execute(q)
            self.result = cr.fetchall()

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in self.result:
                self.trv1.insert("", END, value=i)
