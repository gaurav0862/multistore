from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class addcat:

    def __init__(self):
        self.top = Toplevel()
        self.top.title("ADD ADMIN")
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.top.geometry('500x500')
        self.top.label_3 = Label(self.top, text="ADD CATEGORY", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,
                                                                                                              pady=20)
        self.label_1 = Label(self.top, text="Category Name :: ").pack(side=TOP, pady=10)
        self.en = Entry(self.top, textvariable=self.var_1).pack(side=TOP, pady=10)
        self.lable_2 = Label(self.top, text="Category Description").pack(side=TOP, pady=10)
        self.enp = Text(self.top, width=50, height=10)
        self.enp.pack(side=TOP)
        self.Button1 = Button(self.top, text='ADD', command=self.unewcat)
        self.Button1.pack(side=TOP, pady=10)


    def unewcat(self):
        self.cnam = self.var_1.get()
        self.catdes = self.enp.get(1.0, END)
        conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
        cr = conn.cursor()
        if self.cnam=="" and self.catdes=="":
            showinfo("ADD CATEGORY",'Please input correct details')
        else:
            q = 'insert into category values ("{}","{}")'.format(self.cnam, self.catdes)
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchall()
            self.top.destroy()