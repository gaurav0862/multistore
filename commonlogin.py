from tkinter import *
import adminlogin
import StoreLogin

class login:

    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry('300x300')
        self.bg = PhotoImage(file="imageResources/new3.png")
        self.canvas1 = Canvas(self.root, width=500, height=300)
        self.canvas1.place(x=0, y=0)

        self.root.resizable(0, 0)

        self.canvas1.create_image(0, 0, image=self.bg, anchor="nw")
        self.canvas1.create_text(150,50,text="LOGIN",font=('Ink Free', 50, "bold",))

        self.btn = Button(self.root, text="ADMIN LOGIN", command= self.adminlogin)
        self.btn.place(x=50, y=150)


        self.btn = Button(self.root, text="STORE LOGIN", command= self.storelogin)
        self.btn.place(x=170, y=150)

        self.root.mainloop()


    def adminlogin(self):


        self.root.destroy()
        adminlogin.adlogin()




    def storelogin(self):

        self.root.destroy()
        StoreLogin.stologin()




login()