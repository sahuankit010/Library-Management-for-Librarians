"""
Author : Ankit Sahu
Date : Nov 20, 2022
"""

import mysql.connector
from mysql.connector import errorcode
from datetime import date, timedelta
from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.ttk import Treeview

from main import *
cnx = mysql.connector.connect(**{'user': 'root', 'password': '', 'host': 'localhost', 'db': 'library_db'})


class BorrowingPerson:
    def __init__(self, master):
        self.parent = master

        self.titleLabel = Label(self.parent, text="Enter Details")
        self.titleLabel.grid(row=0, column=0, padx=20, pady=20)
        self.fnameLabel = Label(self.parent, text="First Name").grid(row=1, column=0, padx=10, pady=5)
        self.fnameTB = Entry(self.parent)
        self.fnameTB.grid(row=2, column=0, padx=10, pady=5)
        self.lnameLabel = Label(self.parent, text="Last Name").grid(row=3, column=0, padx=10, pady=5)
        self.lnameTB = Entry(self.parent)
        self.lnameTB.grid(row=4, column=0, padx=10, pady=5)
        self.ssnLabel = Label(self.parent, text="SSN").grid(row=5, column=0, padx=10, pady=5)
        self.ssnTB = Entry(self.parent)
        self.ssnTB.grid(row=6, column=0, padx=10, pady=5)
        self.addressLabel = Label(self.parent, text="Street Address").grid(row=7, column=0, padx=10, pady=5)
        self.addressTB = Entry(self.parent)
        self.addressTB.grid(row=8, column=0, padx=10, pady=5)
        self.cityLabel = Label(self.parent, text="City").grid(row=9, column=0, padx=10, pady=5)
        self.cityTB = Entry(self.parent)
        self.cityTB.grid(row=10, column=0, padx=10, pady=5)
        self.stateLabel = Label(self.parent, text="State").grid(row=11, column=0, padx=10, pady=5)
        self.stateTB = Entry(self.parent)
        self.stateTB.grid(row=12, column=0, padx=10, pady=5)
        self.numberLabel = Label(self.parent, text="Phone Number").grid(row=13, column=0, padx=10, pady=5)
        self.numberTB = Entry(self.parent)
        self.numberTB.grid(row=14, column=0, padx=10, pady=5)
        self.addBtn = Button(self.parent, text="Add", command=self.add_borrower, fg='red', bg='yellow')
        self.addBtn.grid(row=15, column=0, padx=10, pady=5)

    def add_borrower(self):
        Ssn = self.ssnTB.get()
        cursor = cnx.cursor()
        cursor.execute("SELECT MAX(Card_Id) from BORROWER")
        new_card_no = int(cursor.fetchall()[0][0]) + 1
        new_card_no = str(new_card_no)
        cursor.execute("SELECT EXISTS(SELECT Ssn FROM BORROWER WHERE BORROWER.Ssn = '" + str(Ssn) + "')")
        result = cursor.fetchall()
        if result == [(0,)]:
            address = ', '.join([self.addressTB.get(), self.cityTB.get(), self.stateTB.get()])
            cursor.execute("Insert into BORROWER (Card_Id, Ssn, Fname, Lname, Address, Phone) Values ('" + new_card_no + "', '" + Ssn + "', '" + str(self.fnameTB.get()) + "', '" + str(self.lnameTB.get()) + "', '" + str(address) + "', '" + str(self.numberTB.get()) + "')")
            cnx.commit()
            self.parent.destroy()
        else:
            messagebox.showinfo("Error", "Borrower Already Exists!")