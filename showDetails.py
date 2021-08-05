from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from datetime import datetime
from tkcalendar import *
from pymysql import *

class fetch:

    def __init__(self,new2,new4):
        conn = connect(host='127.0.0.1',user='root',password='',database='multistore')
        cr = conn.cursor()

        q = 'select * from bill where dateOfBill between "{}" and "{}"'.format(new2,new4)
        print(q)
        cr.execute(q)
        result5 = cr.fetchall()
        return result5








