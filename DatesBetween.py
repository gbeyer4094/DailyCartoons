import tkinter as tk

from tkcalendar import DateEntry
from datetime import date, timedelta
from tkinter import *
from tkinter import messagebox


def showdatedifference():
    delta = toCal.get_date() - fromCal.get_date()
    messagebox.showinfo("Date Difference", str(delta).split(' ')[0])


root = tk.Tk()
fromDate = date.today() + timedelta(days=-1)
selectedFromDate = fromDate
var1 = StringVar()
fromLabel = Label(root, textvariable=var1)
var1.set("From Date: ")
fromLabel.pack()
fromCal = DateEntry(root, width=12, year=fromDate.year, month=fromDate.month, day=fromDate.day,
                    background='dark-blue', foreground='white', borderwidth=2)
fromCal.pack(padx=10, pady=10)

toDate = date.today()
selectedToDate = toDate
var2 = StringVar()
toLabel = Label(root, textvariable=var2)
var2.set("To Date: ")
toLabel.pack()
toCal = DateEntry(root, width=12, year=toDate.year, month=toDate.month, day=toDate.day,
                  background='dark-blue', foreground='white', borderwidth=2)
toCal.pack(padx=10, pady=10)

select = Button(root, text="display Date Difference", command=showdatedifference)
select.pack(padx=10, pady=10)

root.mainloop()
