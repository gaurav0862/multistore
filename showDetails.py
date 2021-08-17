from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from datetime import datetime
from tkcalendar import *
from pymysql import *

class fetch:

    def __init__(self,new2,new4):
        conn=Connect(host='13.232.35.56', user='shivam', password='shivam@123', database='shivam')
        cr = conn.cursor()

        q = 'select * from bill where dateOfBill between "{}" and "{}"'.format(new2,new4)
        print(q)
        cr.execute(q)
        result5 = cr.fetchall()
        return result5








