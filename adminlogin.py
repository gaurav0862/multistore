import time
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
import datetime
import AdminHome


class login:

    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry('500x500')
        self.bg = PhotoImage(file="imageResources/3.png")
        self.canvas1 = Canvas(self.root, width=500, height=500)
        self.canvas1.place(x=0, y=0)
        self.root.resizable(0, 0)

        self.canvas1.create_image(0, 0, image=self.bg, anchor="nw")

        self.var_1 = StringVar()
        self.var_2 = StringVar()
        # self.lab  = Label(text = "LOGIN", font=('Ink Free',24,"bold")).place(x=200,y=50)
        self.canvas1.create_text(250, 50, text="Login", font=('Ink Free', 50, "bold",))
        # self.lab_1 = Label(text="ENTER EMAIL ID : ").place(x=125,y=125,)
        self.canvas1.create_text(200, 135, text="ENTER EMAIL ID : ")

        self.eme = Entry(self.root, textvariable=self.var_1)
        self.eme.place(x=250, y=125)
        # self.lab_2 = Label(text="ENTER PASSWORD : ").place(x=125,y=170)
        self.canvas1.create_text(192, 180, text="ENTER PASSWORD : ")
        self.eme_1 = Entry(self.root, textvariable=self.var_2, show='*')
        self.eme_1.place(x=250, y=170)
        self.btn = Button(self.root, text="LOGIN", command=self.login1)
        self.btn.place(x=225, y=225)

        self.root.mainloop()


    def login1(self):
        con = connect(host="127.0.0.1", user='root', password='', database='multistore')
        cr = con.cursor()

        self.lgv = self.var_1.get()
        self.lgv_1 = self.var_2.get()

        if self.lgv =="" and self.lgv_1 =="":
            showinfo("Login","Please provide id password")

        else:
            q = 'select * from admin where email="{}" and password="{}" '.format(self.lgv, self.lgv_1)
            cr.execute(q)
            self.result = cr.fetchone()
            print(self.result)
            if self.result == None:
                showinfo('Login', "Invalid Input")
            else:
                print(datetime.datetime.now())
                self.time_1 = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                print(self.time_1)
                q = 'update admin set last_login="{}" where email="{}"'.format(self.time_1, self.lgv)
                self.result = cr.execute(q)
                con.commit()
                showinfo('Login', "Login Sucessfull")
                print("Login Sucessfull")
                self.root.destroy()
                AdminHome.demo()



obj = login()
