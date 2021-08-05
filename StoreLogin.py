import time
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
import datetime
import storeHome
import forgot


class login:


    def login1(self):

        con = connect(host="127.0.0.1",user='root',password='',database='multistore')
        cr = con.cursor()

        self.lgv = self.var_1.get()
        self.lgv_1 = self.var_2.get()
        q = 'select * from storeview where StoreID="{}" and Password="{}" '.format(self.lgv,self.lgv_1)
        cr.execute(q)
        self.result=cr.fetchone()
        print(self.result)
        if self.result == None:
            showinfo('Login',"WRONG CRIDENTIALS")
        else:

            showinfo('Login',"Login Sucessfull")
            print("Login Sucessfull")
            self.root.destroy()

            storeHome.demo(self.lgv)






    def __init__(self):

        self.root = Tk()
        self.root.geometry('500x500')
        self.bg =PhotoImage(file ="imageResources/3.png")
        self.canvas1 = Canvas(self.root,width=500,height=500)
        self.canvas1.place(x=0,y=0)
        self.root.resizable(0,0)

        self.canvas1.create_image(0,0,image= self.bg,anchor ="nw")


        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.canvas1.create_text(250,50, text="Login",font=('Ink Free',50,"bold"))
        self.canvas1.create_text(215,135,text = "STORE ID : ")

        self.eme = Entry(self.root,textvariable=self.var_1)
        self.eme.place(x=250,y=125)
        self.canvas1.create_text(205,180 , text="PASSWORD : ")
        self.eme_1 = Entry(self.root,textvariable=self.var_2,show='*')
        self.eme_1.place(x=250,y=170)
        self.btn = Button(self.root,text="LOGIN", command=self.login1)
        self.btn.place(x=225,y=225)
        self.canvas1.create_text(245,275, text="Forgot password", font=('Helveticabold', 7))

        # self.new = Label(self.root, text="this is a test")
        # self.new.pack(side='bottom')
        # self.new.bind("<Button-1>", '')

        self.root.mainloop()


obj=login()