import csv
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class view:


    def __init__(self,lgv):
        self.top = Toplevel()
        # self.top.title("View Bills").pack(side= 'top')
        Label(self.top,text="View Bills", font= ("Gabriola","25","italic",'bold')).pack(pady=15)
        self.top.waraper = LabelFrame(self.top,text ="Bill view" )
        self.top.waraper.pack(fill="both", expand="yes", padx=50)
        self.trv = Treeview(self.top.waraper, columns=(1, 2, 3, 4), show="headings", height="5")
        self.trv.pack(padx=10, pady=20)
        self.trv.heading(1, text="Bill ID")
        self.trv.heading(2, text="Bill Date")
        self.trv.heading(3, text="store id")
        self.trv.heading(4, text="Total Amount")
        self.trv.bind("<Double-1>", self.showdetails)
        Button(self.top,text='Convert to Excel',command=self.save_csv).pack(pady=15)

        conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
        cr = conn.cursor()
        q = 'select * from bill where billby="{}"'.format(lgv)
        cr.execute(q)
        self.result = cr.fetchall()


        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)

    def save_csv(self):
        with open("new.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',', dialect='excel')

            for row_id in self.trv.get_children():
                row = self.trv.item(row_id)['values']
                print('save row:', row)
                csvwriter.writerow(row)
                showinfo('csv', "CSV File Genrated")

    def showdetails(self,event):
        self.top = Toplevel()
        self.top.title("View Admin")
        Label(self.top,text="Bill Details",font= ("Gabriola","25","italic",'bold')).pack(pady=15)
        self.top.waraper = LabelFrame(self.top, text="Bill Details")
        self.top.waraper.pack(fill="both", expand="yes", padx=50)
        self.trv1 = Treeview(self.top.waraper, columns=(1, 2, 3, 4), show="headings", height="5")
        self.trv1.pack(padx=10, pady=20)
        self.trv1.heading(1, text="Bill ID")
        self.trv1.heading(2, text="Product ID")
        self.trv1.heading(3,text="Product Name")
        self.trv1.heading(3, text="Quantity")
        self.trv1.heading(4, text="Price")
        conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
        cr = conn.cursor()
        self.temp_data = self.trv.item(self.trv.focus())['values']

        self.new = self.temp_data[0]


        q = 'select bill_ID,product_ID,quantity,price from billDetails where bill_ID="{}"'.format(self.new)
        cr.execute(q)
        self.result1 = cr.fetchall()



        for i in self.trv1.get_children():
            self.trv1.delete(i)

        for i in self.result1:
            self.trv1.insert("", END, value=i)
