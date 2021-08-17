import csv
from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from tkcalendar import *
from datetime import datetime
import addAdmin
import viewAdmin
import addCatagory
import viewCategory
import viewProducts
import addProduct
import store_view
import showDetails
from pymysql import *


total1 = float

class demo:

        def caln(self,event):
            self.cal = Calendar(self.canvas1, selectmode='day')
            self.cal.place(x=400, y=210)

        def caln2(self,event):
            self.cal2 = Calendar(self.canvas1, selectmode='day')
            self.cal2.place(x=755, y=210)



        def grad_date(self):
                self.da = self.cal.get_date()
                new1 = datetime.strptime(self.da, '%m/%d/%y')
                self.new5 = datetime.strftime(new1, '%m/%d/%y')
                self.ent1.config(state='normal')
                self.ent1.delete(0, 'end')
                self.ent1.insert(0, self.new5)
                self.ent1.config(state='readonly')
                self.cal.destroy()


        def grad_date1(self):
                self.na = self.cal2.get_date()
                new3 = datetime.strptime(self.da, '%m/%d/%y')
                self.new4 = datetime.strftime(new3, '%m/%d/%y')
                self.ent2.config(state='normal')
                self.ent2.delete(0, 'end')
                self.ent2.insert(0, self.new4)
                self.ent2.config(state='readonly')
                self.cal2.destroy()

        def fetch(self):


            if self.ent1.get()=="" and self.ent2.get()=="":

                conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
                cr = conn.cursor()

                q = 'select * from bill '
                print(q)
                cr.execute(q)
                self.result6 = cr.fetchall()

                for i in self.tree.get_children():
                    self.tree.delete(i)

                for i in self.result6:
                    self.tree.insert("", END, value=i)

                self.total1()

            else:

                conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
                cr = conn.cursor()

                q = 'select * from bill where dateOfBill between "{}" and "{}"'.format(self.new5, self.new4)
                print(q)
                cr.execute(q)
                self.result5 = cr.fetchall()

                for i in self.tree.get_children():
                    self.tree.delete(i)

                for i in self.result5:
                    self.tree.insert("", END, value=i)

                self.total1()

        def showdetails1(self,event):
            self.top = Toplevel()
            self.top.title("View Admin")
            self.top.waraper = LabelFrame(self.top, text="Bill Details")
            self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
            self.trv1 = Treeview(self.top.waraper, columns=(1, 2, 3, 4), show="headings", height="5")
            self.trv1.pack(padx=10, pady=50)
            self.trv1.heading(1, text="Bill ID")
            self.trv1.heading(2, text="Product ID")
            self.trv1.heading(3, text="Quantity")
            self.trv1.heading(4, text="Price")
            conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
            cr = conn.cursor()
            self.temp_data = self.tree.item(self.tree.focus())['values']

            self.new = self.temp_data[0]

            q = 'select bill_ID,product_ID,quantity,price from billDetails where bill_ID="{}"'.format(self.new)
            print(q)
            cr.execute(q)
            self.result1 = cr.fetchall()

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in self.result1:
                self.trv1.insert("", END, value=i)

            # self.total1()

        def showstoreinfo(self):

            new = self.com.get()
            if new == "":
                showerror('search',"Field could not be empty")

            elif self.ent1.get()=="" and self.ent2.get()=="":
                conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
                cr = conn.cursor()
                q = f'select * from bill where billBy ="{new}"'
                cr.execute(q)
                self.bills= cr.fetchall()

                print(self.bills)
                if self.bills==():
                    showinfo('search',"No data found")

                else:
                    for i in self.tree.get_children():
                        self.tree.delete(i)

                    for i in self.bills:
                        self.tree.insert("", END, value=i)

                    self.com.config(state='normal')
                    self.com.delete(0, 'end')
                    self.com.insert(0, "")
                    self.com.config(state='readonly')
                    self.total1()


            else:
                conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
                cr = conn.cursor()

                q = 'select * from bill where dateOfBill between "{}" and "{}"  and  billBy = "{}" '.format(self.new5, self.new4,new)
                print(q)
                cr.execute(q)
                self.result58 = cr.fetchall()

                if self.result58==():
                    showinfo('search',"No data found")

                else:

                    for i in self.tree.get_children():
                        self.tree.delete(i)

                    for i in self.result58:
                        self.tree.insert("", END, value=i)

                    self.com.config(state='normal')
                    self.com.delete(0, 'end')
                    self.com.insert(0, "")
                    self.com.config(state='readonly')
                    self.total1()

        def total1(self):

            global total1
            self.all = self.tree.get_children()
            total1 = 0
            for i in self.all:
                self.item = self.tree.item(i)['values']
                total1 += int(self.item[3])

            self.ent7.config(state='normal')
            self.ent7.delete(0, 'end')
            self.ent7.insert(0, total1)
            self.ent7.config(state='readonly')

        def __init__(self):


            self.root = Tk()
            self.root.title("Home Page")
            # self.root.state('zoomed')
            self.root.geometry('1366x680')
            self.root.resizable(0,0)
            self.bg = PhotoImage(file="imageResources/258_1080x720.png")
            self.canvas1=Canvas(self.root)
            self.canvas1.pack(fill="both", expand=True)

            self.canvas1.create_image(0,0,image=self.bg,anchor='nw')

            self.canvas1.create_text(700,50,text="Welcome", font= ("Gabriola","50","italic",'bold'))
            self.canvas1.create_text(700,135,text="View Store Data", font= ("Gabriola","25",'bold'))
            self.canvas1.create_text(370,200,text = 'Start Date',font= ("arial","15","bold",'bold'))
            self.ent1 = Entry(self.root,state='readonly')
            self.ent1.bind("<Double-1>", self.caln)
            self.ent1.place(x=450, y=190)
            Button(self.canvas1, text="Get Date",command=self.grad_date).place(x=600, y=186)

            self.canvas1.create_text((800,200),text="End Date",font= ("arial","15","bold",'bold'))
            self.ent2 = Entry(self.root,state='readonly')
            self.ent2.bind("<Double-1>", self.caln2)
            self.ent2.place(x=875, y=190)
            Button(self.canvas1, text="Get Date", command=self.grad_date1).place(x=1025, y=186)
            Button(self.canvas1,text="Fetch Details", command = self.fetch).place(x=780,y=338)
            self.canvas1.create_text(910, 350, text=f"Total", font=("arial", "15", "bold"))
            self.ent7 = Entry(self.canvas1)
            self.ent7.place(x=950, y=339)
            self.canvas1.create_text(400,350,text='Search by Store ID : ',font= ("arial","15","bold",'bold'))
            conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
            cr = conn.cursor()
            q = 'select StoreID from storeview'
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchall()
            x = []
            for i in self.result:
                x.append(i[0])
            self.com = Combobox(self.canvas1,values=x,state='readonly',width=30)
            self.com.place(x=510,y=340)
            self.but = Button(self.canvas1,text='Search',command = self.showstoreinfo).place(x=725,y=338)

            self.menu_1 = Menu(self.root)
            self.root.config(menu=self.menu_1)

            self.admin = Menu(self.menu_1,tearoff=0)
            self.menu_1.add_cascade(label="Admin",menu = self.admin)
            self.admin.add_command(label ="Add User",command=lambda :addAdmin.admin_view())
            self.admin.add_command(label ="View Admin",command= lambda :viewAdmin.viewadd()  )
            self.admin.add_command(label ="Logout",command= self.logout )

            self.catmenu = Menu(self.menu_1,tearoff=0)
            self.menu_1.add_cascade(label="Category",menu=self.catmenu)
            self.catmenu.add_command(label="Add Category",command= lambda :addCatagory.addcat())
            self.catmenu.add_command(label="View Category",command= lambda :viewCategory.viewcat())


            self.promenu= Menu(self.menu_1,tearoff=0)
            self.menu_1.add_cascade(label="Products",menu=self.promenu)
            self.promenu.add_command(label="View Products", command= lambda :viewProducts.viewpro())
            self.promenu.add_command(label="Add Product",command= lambda :addProduct.addpro())
            self.storeview = Menu(self.menu_1, tearoff=0)
            self.menu_1.add_cascade(label="Stores", menu=self.storeview)
            self.storeview.add_command(label="View stores", command=lambda: store_view.admin())
            self.frame = Frame(self.canvas1)
            self.frame.place(x=300,y=400)
            self.tree = Treeview(self.frame,columns=(1,2,3,4),show='headings',height="10")
            self.tree.heading(1,text='Bill No.')
            self.tree.heading(2,text='Bill Date')
            self.tree.heading(3,text='Store ID')
            self.tree.heading(4,text='Bill Value')
            self.tree.bind("<Double-1>", self.showdetails1)
            Button(self.canvas1,text='Convert to excel', command = self.save_csv ).pack(side='bottom',pady=15)
            self.tree.pack()



            self.root.mainloop()

        def save_csv(self):
            with open("new.csv", "w", newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',', dialect='excel')

                for row_id in self.tree.get_children():
                    row = self.tree.item(row_id)['values']
                    print('save row:', row)
                    csvwriter.writerow(row)
                    showinfo('csv',"CSV File Genrated")

        def logout(self):

            self.root.destroy()

# obj = demo()