"""
Author : Ankit Sahu
Date : Nov 20 2022
"""

import mysql.connector
from mysql.connector import errorcode
from datetime import date, timedelta
from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.ttk import Treeview
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

from MainGui import *
from PayFines import *
from BorrowingPerson import *
from CheckIn import *

global cnx
cnx = mysql.connector.connect(**{'user': 'root', 'password': '', 'host': 'localhost', 'db': 'library_db'})
cursor = None
todays_date = date.today()

if __name__ == '__main__':
    root = ThemedTk(theme="radiance")
    tool = MainGui(root)
    root.mainloop()