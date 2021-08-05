# Import Required Library
from tkinter import *
from tkcalendar import *
from pymysql import *
import datetime


conn = connect(host='127.0.0.1',user='root',password='',database='multistore')
cr = conn.cursor()

# q ='select dateOfBill from bill where"{}"'.format('28-07-2021')
# cr.execute(q)
# result = cr.fetchone()
# print(result)

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar

cal = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)

cal.pack(pady=20)


def grad_date():
    new = cal.get_date()
    new1 = datetime.datetime.strptime(new,'%m/%d/%y')
    new2 = datetime.datetime.strftime(new1,'%m/%d/%y')
    print(new2)

    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Excecute Tkinter
root.mainloop()
