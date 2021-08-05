from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *
from datetime import datetime

import viewBills

val = ()
total = float


class demo:

    def callbackFunc(self,event):
        conn = Connect(host="127.0.0.1", user="root", password="", database="multistore")
        cr = conn.cursor()
        q = 'select PName from products where CatergoryName="{}"'.format(self.com.get())
        cr.execute(q)
        y=[]
        self.result = cr.fetchall()
        for i in self.result:
            self.new = y.append(i[0])
        self.com1.config(values=y)



    def pricepro(self,event):

        global val
        conn = Connect(host="127.0.0.1", user="root", password="", database="multistore")
        cr = conn.cursor()
        q = 'select * from products where PName="{}"'.format(self.com1.get())
        print(q)
        cr.execute(q)
        self.result = cr.fetchone()
        val = self.result
        self.proid = self.result[0]
        self.tot = self.result[2]
        self.ne.config(state='normal')
        self.ne.delete(0, 'end')
        self.ne.insert(0,self.tot)
        self.ne.config(state='readonly')



    def additem(self):


        self.a = self.spinval.get()
        print(self.a)

        if self.a == 1:

            pass

        else:

            self.tot = self.tot * int(self.a)

        global val
        new =[]
        new= list(val)
        new.append(self.a)
        new.append(self.tot)
        count = len(self.trv1.get_children())
        self.spinval.delete(0,'end')
        self.spinval.insert(0,str(1))
        self.trv1.insert('', index=count+1, values=new)
        self.total()



    def __init__(self,lgv):


            self.root = Tk()
            self.lgv = lgv
            self.val = StringVar()
            self.root.title("Store Home")
            self.root.state('zoomed')

            self.bg = PhotoImage(file="imageResources/258_1080x720.png")
            self.canvas1=Canvas(self.root)
            self.canvas1.pack(fill="both", expand=True)

            self.canvas1.create_image(0,0,image=self.bg,anchor='nw')
            conn=Connect(host="127.0.0.1",user="root",password="",database="multistore")
            cr=conn.cursor()


            q='select StoreName from storeview where StoreID="{}"'.format(lgv) #select store name by store id imported from login page
            cr.execute(q)
            self.result = cr.fetchone()
            self.x=[]


            for i in self.result:
                self.x.append(i)


            self.canvas1.create_text(700,50,text=f"Welcome {self.x[0]}", font= ("Gabriola","50","italic",'bold'))
            self.canvas1.create_text(350,170,text="Select Catergory",font=("arial","15","bold"))

            q = 'select CategoryName from category'
            cr.execute(q)
            self.result = cr.fetchall()
            x = []
            for i in self.result:
                x.append(i[0])
            self.current = x[0]
            self.com = Combobox(self.root,values=x,state='readonly')

            self.com.place(x=450,y=162)

            self.com.bind("<<ComboboxSelected>>", self.callbackFunc)
            self.canvas1.create_text(750, 170, text="Select Product", font=("arial", "15", "bold"))
            self.com1 = Combobox(self.root, values=(), state="readonly")
            self.com1.bind("<<ComboboxSelected>>", self.pricepro)
            self.com1.place(x=850, y=162)

            self.butt = Button(self.root, text="ADD To CART", command=self.additem).place(x=780, y=217)

            self.canvas1.create_text(337, 230, text="Product Price", font=("arial", "15", "bold"))
            self.ne = Entry(self.canvas1, width=25)
            self.ne.place(x=450, y=220)
            self.canvas1.create_text(660, 230, text="Quantity", font=("arial", "15", "bold"))
            self.spinval = Spinbox(self.canvas1, from_=1, to=25,width="5")
            self.spinval.place(x=710,y=220)

            self.ne.insert(0, self.val.get())
            self.ne.config(state="readonly")

            self.waraper = Frame(self.root)
            self.waraper.place(x=0,y=350)

            self.menu_2 = Menu(self.root)
            self.root.config(menu=self.menu_2)
            self.admin = Menu(self.menu_2, tearoff=0)
            self.menu_2.add_cascade(label="View", menu=self.admin)
            self.admin.add_command(label="View Bills", command=lambda: viewBills.view(lgv))
            self.admin.add_command(label="Logout", command= self.logout)


            self.trv1 = Treeview(self.root ,columns=(1, 2, 3, 4, 5, 6,7), show="headings", height="5")
            self.trv1.column('#0',width=0,stretch = NO)
            self.trv1.column('1',width=80,stretch = NO)
            self.trv1.column('6',width=80,stretch = NO)
            self.trv1.place(x=100,y=270)
            self.trv1.heading(1, text="Product ID")
            self.trv1.heading(2, text="Product Name")
            self.trv1.heading(3, text="Product Price")
            self.trv1.heading(4, text="Product Description")
            self.trv1.heading(5, text="category Name")
            self.trv1.heading(6, text="Quantity")
            self.trv1.heading(7, text="Total")
            self.trv1.config(height=15)
            self.trv1.bind('<Double-1>',self.deleteItem)

            self.butn = Button(self.canvas1, text="Save Bill", width="20", command= self.savebill).pack(side="bottom", padx=5,pady=40)
            self.canvas1.create_text(950, 230, text=f"Total", font=("arial", "15", "bold"))
            self.ent1 = Entry(self.canvas1)
            self.ent1.place(x=980, y=220)

            self.root.mainloop()

    def logout(self):
        self.root.destroy()

#-----------------------------Delete Iteam From Tree View-----------------------

    def deleteItem(self, event):
        self.que = askquestion('','Do you want to delete this item ??')
        print(self.que)
        if self.que == 'yes':

            self.s = self.trv1.selection()[0]
            print(self.trv1.focus())
            print(self.s)
            self.trv1.delete(self.s)
        self.total()

#--------------------------------Total Function-----------------------------------

    def total(self):


            global total
            self.all = self.trv1.get_children()
            total = 0
            for i in self.all:
                self.item = self.trv1.item(i)['values']
                total += self.item[6]


            self.ent1.config(state='normal')
            self.ent1.delete(0,'end')
            self.ent1.insert(0,total)
            self.ent1.config(state='readonly')

#--------------------------------Save Bill--------------------------------

    def savebill(self):


        now = datetime.now()
        self.date1   = now.strftime("%mm/%d/%y")
        conn = connect(host="127.0.0.1",user="root",password="",database="multistore")
        cr = conn.cursor()
        q= 'Insert into bill values ("{}","{}","{}","{}")'.format( "null",self.date1,self.lgv,total)
        print(q)
        cr.execute(q)
        self.result = cr.fetchall()
        conn.commit()
        id = cr.lastrowid
        self.all = self.trv1.get_children()
        for i in self.all:
            self.item = self.trv1.item(i)['values']
            q='insert into billdetails values ("{}","{}","{}","{}","{}")'.format('null',id,self.item[0],self.item[5],self.item[6])
            cr.execute(q)
            self.result=cr.fetchall()
            conn.commit()
            self.trv1.delete(i)
        showinfo('Bill', 'Bill Save Successfully')


# obj = demo()