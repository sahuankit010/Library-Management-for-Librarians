"""
Author : Ankit Sahu
Date : Nov 20, 2022
"""

import mysql.connector
from mysql.connector import errorcode
from datetime import date, timedelta
from datetime import date
from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.ttk import Treeview

from main import *
cnx = mysql.connector.connect(**{'user': 'root', 'password': '', 'host': 'localhost', 'db': 'library_db'})

class CheckIn:
    def __init__(self, master):
        self.parent = master

        self.bookForCheckInID = None
        self.search_string = None
        self.data = None

        self.searchLabel = Label(self.parent, text="Search here: Borrower ID, Borrower Name or ISBN")
        self.searchLabel.grid(row=0, column=0, padx=20, pady=20)
        self.searchTextBox = Entry(self.parent)
        self.searchTextBox.grid(row=1, column=0)
        self.searchBtn = Button(self.parent, text="Search", command=self.search_book_loans, fg='red', bg='yellow')
        self.searchBtn.grid(row=2, column=0)
        self.table = Treeview(self.parent, columns=["Loan ID", "ISBN", "Borrower ID", "Title"])
        self.table.grid(row=3, column=0)
        self.table.heading('#0', text="Loan ID")
        self.table.heading('#1', text="ISBN")
        self.table.heading('#2', text="Borrower ID")
        self.table.heading('#3', text="Book Title")
        self.table.bind('<ButtonRelease-1>', self.select_book_for_checkin)
        self.checkInBtn = Button(self.parent, text="Check In", command=self.check_in, fg='red', bg='yellow')
        self.checkInBtn.grid(row=4, column=0)

    def search_book_loans(self):
        self.search_string = self.searchTextBox.get()
        cursor = cnx.cursor()
        cursor.execute("select BOOK_LOANS.LoanID, BOOK_LOANS.ISBN, BOOK_LOANS.Card_ID, BOOK.title, BOOK_LOANS.Date_In from BOOK_LOANS "
                       "join BORROWER on BOOK_LOANS.Card_ID = BORROWER.Card_Id "
                       "join BOOK on BOOK_LOANS.ISBN = BOOK.ISBN "
                       "where BOOK_LOANS.ISBN like concat('%', '" + self.search_string + "', '%') or "
                        "BORROWER.Fname like concat('%', '" + self.search_string + "', '%') or "
                        "BORROWER.Lname like concat('%', '" + self.search_string + "', '%') or "
                        "BOOK_LOANS.Card_ID like concat('%', '" + self.search_string + "', '%')")

        self.data = cursor.fetchall()
        self.view_data()

    def view_data(self):
        """
        View data on Treeview method.
        """
        self.table.delete(*self.table.get_children())
        for elem in self.data:
            if elem[4] is None:
                self.table.insert('', 'end', text=str(elem[0]), values=(elem[1], elem[2], elem[3]))

    def select_book_for_checkin(self, a):
        curItem = self.table.focus()
        self.bookForCheckInID = self.table.item(curItem)['text']

    def check_in(self):
        if self.bookForCheckInID is None:
            messagebox.showinfo("Attention!", "Select Book to Check In First!")
            return None
        cursor = cnx.cursor()
        cursor.execute("SELECT BOOK_LOANS.Date_In FROM BOOK_LOANS WHERE BOOK_LOANS.LoanID = '" + str(self.bookForCheckInID) + "'")
        result = cursor.fetchall()
        if result[0][0] is None:
            cursor.execute("UPDATE BOOK_LOANS SET BOOK_LOANS.Date_In = '" + str(date.today()) + "' WHERE BOOK_LOANS.LoanID = '"
                           + str(self.bookForCheckInID) + "'")
            cnx.commit()
            messagebox.showinfo("Done", "Book Checked In Successfully!")
            self.parent.destroy()
        else:
            return None

