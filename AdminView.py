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
        self.label_1 = Label(self.top, text="Email :: ").pack(side=TOP,pady=10)
        self.em = Entry(self.top)
        self.em.insert(0, self.temp_data[0])
        self.em.pack(side=TOP,pady=10)
        self.label_2 = Label(self.top, text="password :: ").pack(side=TOP,pady=10)
        self.pm = Entry(self.top)
        self.pm.insert(0, self.temp_data[1])
        self.pm.pack(side=TOP,pady=10)
        self.label_3= Label(self.top, text="Last Login :: ").pack(side=TOP,pady=10)
        self.ll = Entry(self.top)
        self.ll.insert(0, self.temp_data[2])
        self.ll.pack(side=TOP,pady=10)
        self.label_4 = Label(self.top, text="Role :: ").pack(side=TOP,pady=10)
        # self.rr = Entry(self.top)
        # self.rr.insert(0, self.temp_data[3])
        # self.rr.pack(side=TOP,pady=10)
        self.enp_1=("Admin", "SuperAdmin")
        self.current= self.enp_1.index(str(self.temp_data[3]))
        self.enl = Combobox(self.top, values=self.enp_1, state="readonly")
        self.enl.pack(side=TOP,pady=10)
        self.enl.insert(0,self.temp_data[3])
        self.enl.config(state='readonly')


        self.upbtn = Button(self.top, text="update", command=self.newupdate)
        self.upbtn.pack()
        self.delbtn = Button(self.top, text="Delete", command=self.delupdate)
        self.delbtn.pack()


    #--------------UPDATE EXISTING DATA--------------

    def newupdate(self):
            self.pqw = self.pm.get()
            self.eml = self.em.get()
            self.rol = self.enl.get()
            conn = Connect(host='127.0.0.1', user='root', password='', database='admin_login')
            cr = conn.cursor()
            q = 'update admin set password="{}",type_1="{}" where email="{}"'.format(self.pqw,self.rol, self.eml,)

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
        self.eml = self.em.get()
        conn = Connect(host='127.0.0.1', user='root', password='', database='admin_login')
        cr = conn.cursor()
        q = 'delete from admin where email="{}"'.format(self.eml)

        cr.execute(q)
        print(q)
        conn.commit()
        self.result = cr.fetchall()

        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv_1.insert("", END, value=i)
        self.top.destroy()



    #---------------SHOW EXISTING DATA---------------------

    def show_data(self):
        conn = Connect(host='127.0.0.1', user='root', password='', database='admin_login')
        cr = conn.cursor()
        q = 'select * from admin'
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
        self.top.geometry('500x500')
        self.label_1 = Label(self.top, text="EMAIL ID :: ").pack(side=TOP,pady = 10)
        self.en = Entry(self.top, textvariable=self.var_1).pack(side=TOP,pady = 10)
        self.lable_2 = Label(self.top, text="Password").pack(side=TOP,pady = 10)
        self.enp = Entry(self.top, textvariable=self.var_2).pack(side=TOP,pady = 10)
        self.lable_2 = Label(self.top, text="Add Role").pack(side=TOP,pady = 10)
        self.enp = Combobox(self.top, values= ("Admin","SuperAdmin"),state="readonly")
        self.enp.pack(side=TOP, pady = 10)
        self.upnew = Button(self.top, text='Update', command= self.upnew).pack(side=TOP,pady = 10)

    def upnew(self):
        self.eql = self.var_1.get()
        self.pml = self.var_2.get()
        self.pml_1 = self.enp.get()
        conn = Connect(host='127.0.0.1', user='root', password='', database='admin_login')
        cr = conn.cursor()
        q = 'insert into admin values ("{}","{}",null,"{}")'.format(self.eql,self.pml,self.pml_1)
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


        self.waraper = LabelFrame(self.root)
        self.waraper.pack(fill="both",expand="yes",padx=50,pady=50)
        self.trv  = Treeview(self.waraper,columns=(1,2,3,4),show="headings",height="5")
        self.trv.pack(padx=10,pady=50)
        self.trv.heading(1,text="Email ID")
        self.trv.heading(2,text="Password")
        self.trv.heading(3,text="Last Login")
        self.trv.heading(4,text="Type")
        self.trv.bind("<Double-1>",self.show_details)
        conn = Connect(host='127.0.0.1', user='root', password='', database='admin_login')
        cr = conn.cursor()
        q = 'select * from admin'
        cr.execute(q)
        self.result = cr.fetchall()

        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)


        self.btn = Button(self.waraper,text="Show",command = self.show_data)
        self.btn.pack(side=BOTTOM,padx=10)
        self.btn_1 = Button(self.waraper,text="Add New",command = self.newadd)
        self.btn_1.pack(side=BOTTOM,padx=10)

        self.root.mainloop()
obh =admin()

