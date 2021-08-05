from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from pymysql import *

class admin:

    #-----------------SHOW ALL DETAILS--------------------

    def show_details(self,event):
        self.temp_data= self.trv.item(self.trv.focus())['values']
        self.top = Toplevel()
        self.top.geometry('500x500')
        self.label_1 = Label(self.top, text="Store ID :: ").pack(side=TOP,pady=10)
        self.em = Entry(self.top)
        self.em.insert(0, self.temp_data[0])
        self.em.config(state='readonly')
        self.em.pack(side=TOP,pady=10)
        self.label_2 = Label(self.top, text="Store Name :: ").pack(side=TOP,pady=10)
        self.pm = Entry(self.top)
        self.pm.insert(0, self.temp_data[1])
        self.pm.pack(side=TOP,pady=10)
        self.label_3= Label(self.top, text="Store location :: ").pack(side=TOP,pady=10)
        self.ll = Entry(self.top)
        self.ll.insert(0, self.temp_data[2])
        self.ll.pack(side=TOP,pady=10)
        self.label_4 = Label(self.top, text="password :: ").pack(side=TOP,pady=10)
        self.lll = Entry(self.top)
        self.lll.insert(0, self.temp_data[3])
        self.lll.pack(side=TOP, pady=10)

    #--------------update and delete button----------
        self.upbtn = Button(self.top, text="update", command=self.newupdate)
        self.upbtn.pack()
        self.delbtn = Button(self.top, text="Delete", command=self.delupdate)
        self.delbtn.pack()


    #--------------UPDATE EXISTING DATA--------------

    def newupdate(self):
            self.snm = self.pm.get()
            self.sid = self.em.get()
            self.loc = self.ll.get()
            self.ps = self.lll.get()
            conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
            cr = conn.cursor()
            q = 'update storeview set Password="{}",Location="{}",StoreName="{}" where StoreID="{}"'.format(self.ps,self.loc,self.snm, self.sid,)

            cr.execute(q)
            print(q)
            conn.commit()
            self.result = cr.fetchall()
            self.result = cr.fetchall()

            for i in self.trv.get_children():
                self.trv.delete(i)

            for i in self.result:
                self.trv.insert("", END, value=i)
            self.top.destroy()

    #-------DELETE ALL SELECTED DATA----------------

    def delupdate(self):
        self.sid = self.em.get()
        conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
        cr = conn.cursor()
        q = 'delete from admin where StoreID="{}"'.format(self.sid)

        cr.execute(q)
        print(q)
        conn.commit()
        self.result = cr.fetchall()

        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)
        self.top.destroy()



    #---------------SHOW EXISTING DATA---------------------

    def show_data(self):
        conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
        cr = conn.cursor()
        q = 'select * from storeview'
        cr.execute(q)
        self.result = cr.fetchall()


        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)

    #---------------------ADD NEW DATA------------------------------

    def newadd(self):

        self.top = Toplevel()
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.var_3 = StringVar()
        self.var_4 = StringVar()
        self.top.geometry('500x500')
        self.label_1 = Label(self.top, text="Store ID :: ").pack(side=TOP,pady = 10)
        self.en = Entry(self.top, textvariable=self.var_1).pack(side=TOP,pady = 10)
        self.lable_2 = Label(self.top, text="Store Name").pack(side=TOP,pady = 10)
        self.enp = Entry(self.top, textvariable=self.var_2).pack(side=TOP,pady = 10)
        self.lable_3 = Label(self.top, text="Store Location").pack(side=TOP,pady = 10)
        self.stl = Entry(self.top, textvariable=self.var_3).pack(side=TOP, pady=10)
        self.lable_4 = Label(self.top, text="Store Password").pack(side=TOP,pady = 10)
        self.sps = Entry(self.top, textvariable=self.var_4).pack(side=TOP, pady=10)
        # self.enp = Combobox(self.top, values= ("Admin","SuperAdmin"),state="readonly")
        self.upnew = Button(self.top, text='Update', command= self.upnew).pack(side=TOP,pady = 10)

    def upnew(self):
        self.eql = self.var_1.get()
        self.pml = self.var_2.get()
        self.pml_1 = self.var_3.get()
        self.pml_2 = self.var_4.get()
        conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
        cr = conn.cursor()
        q = 'insert into storeview values ("{}","{}","{}","{}")'.format(self.eql,self.pml,self.pml_1,self.pml_2)
        cr.execute(q)
        print(q)
        conn.commit()
        self.result = cr.fetchall()

        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)
        self.top.destroy()

    def __init__(self):

        self.root = Tk()
        self.root.state('zoomed')


        self.waraper = LabelFrame(self.root,text= "Store details")
        self.waraper.pack(fill="both",expand="yes",padx=50,pady=50)
        self.trv  = Treeview(self.waraper,columns=(1,2,3,4),show="headings",height="5")
        self.trv.pack(padx=10,pady=50)
        self.trv.heading(1,text="Store ID")
        self.trv.heading(2,text="Store Name")
        self.trv.heading(3,text="Store Location")
        self.trv.heading(4,text="Password")
        self.trv.bind("<Double-1>",self.show_details)
        conn = Connect(host='127.0.0.1', user='root', password='', database='multistore')
        cr = conn.cursor()
        q = 'select * from storeview'
        cr.execute(q)
        self.result = cr.fetchall()

        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)


        self.btn = Button(self.waraper,text="Show",command = self.show_data)
        self.btn.place(x=550,y=250)
        self.btn_1 = Button(self.waraper,text="Add New",command = self.newadd)
        self.btn_1.place(x=650,y=250)
            # pack(side=BOTTOM,padx=10)

        self.root.mainloop()
# obh =admin()