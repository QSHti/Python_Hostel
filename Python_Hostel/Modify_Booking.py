from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.simpledialog import askstring

import sqlite3
import Hostel_Database
import main
import Booking


class ModifyBooking:
     def __init__(self, root):
        self.root = root
        self.root.geometry('720x620')
        self.root.title("Modify Booking")
        self.root.configure(background='green')

        #Container
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        #Search label/entry
        self.search_label = Label(self.mainframe, text="Enter your name to search booking:", width=27,font=("times", 12, "bold"), anchor="w", bg='white')
        self.search_label.place(x=10, y=230)
        self.search_entry = Entry(self.mainframe, width=30, bd=2)
        self.search_entry.place(x=255, y=233)

        self.edit_name_var = StringVar()
        self.edit_name_label = Label(self.mainframe, text="Name")
        self.edit_name_label.place(x=20, y=315)
        self.edit_name_entry = Entry(self.mainframe, text=self.edit_name_var)
        self.edit_name_entry.place(x=150, y=315)

        self.edit_country_var = StringVar()
        self.edit_country_label = Label(self.mainframe, text="Country")
        self.edit_country_label.place(x=20, y=345)
        self.edit_country_entry = Entry(self.mainframe, text=self.edit_country_var)
        self.edit_country_entry.place(x=150, y=345)

        self.edit_gender_var = StringVar()
        self.edit_gender_label = Label(self.mainframe, text="Gender")
        self.edit_gender_label.place(x=20, y=375)
        self.edit_gender_entry = Entry(self.mainframe, text=self.edit_gender_var)
        self.edit_gender_entry.place(x=150, y=375)

        self.edit_passport_var = IntVar()
        self.edit_passport_label = Label(self.mainframe, text="Passport number")
        self.edit_passport_label.place(x=20, y=405)
        self.edit_passport_entry = Entry(self.mainframe, text=self.edit_passport_var)
        self.edit_passport_entry.place(x=150, y=405)

        #Scrollbar (under construction)
        self.scroll_bar = ttk.Scrollbar(self.mainframe)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        self.tree = ttk.Treeview(self.mainframe, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8"),selectmode="extended", height=10, yscrollcommand=self.scroll_bar.set)
        self.tree['show'] = 'headings'
        self.scroll_bar.config(command=self.tree.yview)
        self.tree.heading("#1", text="Guest name")
        self.tree.heading("#2", text="Country")
        self.tree.heading("#3", text="Gender")
        self.tree.heading("#4", text="Passport")
        self.tree.heading("#5", text="FromDate")
        self.tree.heading("#6", text="ToDate")
        self.tree.heading("#7", text="Room")

        #Column
        #Table
        self.tree.column("#1", width=100)
        self.tree.column("#2", width=100)
        self.tree.column("#3", width=100)
        self.tree.column("#4", width=100)
        self.tree.column("#5", width=100)
        self.tree.column("#6", width=100)
        self.tree.column("#7", width=100)
        self.tree.pack()

        global iid
        iid = self.tree.focus()

        #Display all data function
        def display_all():
            self.tree.delete(*self.tree.get_children())
            con = sqlite3.connect('Hostel_db.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM Booking_Details')
            con.commit()
            details = cur.fetchall()
            for row in details:
                self.tree.insert('', 'end', values=row)
            con.close()

        display_all()

        #Search Function
        def search_entry():
            self.tree.delete(*self.tree.get_children())
            con = sqlite3.connect('Hostel_db.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM Booking_Details WHERE Name LIKE ?", ('%' + str(self.search_entry.get()) + '%',))
            details = cur.fetchall()
            for row in details:
                self.tree.insert("", 'end', values=row)
            con.close()

        #Info in space
        def select_entry(event):
            global iid
            iid = self.tree.focus()
            values = self.tree.item(iid, 'values')
            self.edit_name_entry.insert(0, values[0])
            self.edit_country_entry.insert(0, values[1])
            self.edit_gender_entry.insert(0, values[2])
            self.edit_passport_entry.insert(0, values[3])

        #Update
        def update_entry():
            iid = self.tree.focus()
            name = self.edit_name_var.get()
            country = self.edit_country_var.get()
            gender = self.edit_gender_var.get()
            passport = self.edit_passport_var.get()
            self.tree.item(iid, text='', values=(name, country, gender, passport))
            con = sqlite3.connect('Hostel_db.db')
            cur = con.cursor()
            cur.execute("UPDATE Booking_Details SET Name = ?, Country = ?, Gender = ?, Passport = ? WHERE Room_Type = ?", (name, country, gender, passport, self.tree.item(iid, 'text')))
            mb.showinfo("Notification", "Update has been successful!")
            con.commit()
            con.close()

        search_entries = StringVar()

        #display all button
        self.search_button = Button(self.mainframe, text="Display all", command=display_all, font=("times", 12), bg='white')
        self.search_button.place(x=10, y=265)

        #search button
        self.search_button = Button(self.mainframe, text="Search", command=search_entry, font=("times", 12), bg='white')
        self.search_button.place(x=444, y=226)

        #update button
        self.update_button = Button(self.mainframe, text="Update", command=update_entry, font=("times", 12), bg='white')
        self.update_button.place(x=250, y=520)

        #delete button
        self.delete_booking = Button(self.mainframe, text="Delete Booking", font=("times", 14), bg='white')
        self.delete_booking.place(x=50, y=520)

        self.tree.bind("Booking Details", select_entry)
        self.tree.bind('<ButtonRelease-1>', select_entry)


#Modify booking page function
def modify_booking_page():
    root = Tk()
    desktop = ModifyBooking(root)
    root.mainloop()

