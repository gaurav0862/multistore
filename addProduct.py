from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *


class addpro:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("ADD PRODUCT")
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.var_4 = StringVar()
        # self.top.geometry('500x500')
        self.top.state("zoomed")
        self.top.label_5 = Label(self.top, text="ADD PRODUCT", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,
                                                                                                                 pady=20)
        self.label_1 = Label(self.top, text="Product Name :: ").place(x=400, y=100)
        self.en1 = Entry(self.top, textvariable=self.var_1).place(x=500, y=100)
        self.label_2 = Label(self.top, text="Product Price :: ").place(x=700, y=100)
        self.en2 = Entry(self.top, textvariable=self.var_2).place(x=800, y=100)
        self.label_3 = Label(self.top, text="Product description :: ").place(x=400, y=200)
        self.en3 = Text(self.top, height=5, width=47)
        self.en3.place(x=550, y=200)
        self.label_4 = Label(self.top, text="Category Name :: ").place(x=400, y=350)
        conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
        cr = conn.cursor()
        q = 'select CategoryName from Category'
        cr.execute(q)
        conn.commit()
        self.result = cr.fetchall()
        x = []
        for i in self.result:
            x.append(i[0])
        self.enl = Combobox(self.top, values=x, state="readonly")
        self.enl.place(x=500, y=350)

        self.Button1 = Button(self.top, text='ADD', command=self.newpro)
        self.Button1.place(x=700, y=400)
        self.cat = self.enl.get()


    def newpro(self):
        self.pnam = self.var_1.get()
        self.pprc = self.var_2.get()
        self.pdes = self.en3.get(1.0, END)
        self.cat = self.enl.get()
        conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
        cr = conn.cursor()
        if self.pnam=="" or self.pprc=="" or self.pdes=="" or  self.cat=="":
            showinfo("ADD PRODUCT","Provide valid inputs")
        else:

            try:
                self.price=int(self.pprc)
                q = 'insert into products values ("{}","{}","{}","{}","{}")'.format("null", self.pnam, self.pprc,
                                                                                    self.pdes,
                                                                                    self.cat)
                cr.execute(q)
                conn.commit()
                self.result = cr.fetchall()
                self.top.destroy()
                showinfo('Add PRODUCT',"Product Added Sucessfully")

            except:
                showinfo("","Invalid Price ")


