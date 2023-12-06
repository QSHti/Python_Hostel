# make booking class
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox as mb
import datetime
import csv
import sqlite3
import main
import Hostel_Database


class Booking:

    #Gui
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x500')
        self.root.title("New Booking")
        self.root.configure(background='white')
        
        #Container
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        #Booking window text
        self.booking_label = Label(self.mainframe, text = "Customer Booking", width = 50 ,font = ("times", 20,"bold"), fg = 'black', anchor = 'n')
        self.booking_label.place(x = -100, y = 50)

        #Customer details
        #Name label/entry
        self.name_label = Label(self.mainframe, text = "Full Name", width = 20, font = ("times", 12, "bold"), anchor= "w", bg = 'white')
        self.name_label.place(x = 70, y = 130)
        self.name_var = StringVar()
        self.name_entry = Entry(self.mainframe, width = 30, bd = 2, textvar = self.name_var)
        self.name_entry.place(x = 240, y = 130)
        
        #Country label/entry
        self.country_label = Label(self.mainframe, text = "Country", width = 20, font = ("times", 12, "bold"), anchor = "w", bg = 'white')
        self.country_label.place(x = 70, y = 160)
        self.country_entry = Entry(self.mainframe, width=30, bd = 2)
        self.country_entry.place(x = 240, y = 160)

        #Gender label/button
        self.gender_label = Label(self.mainframe, text="Gender", width=20, font=("times",12,"bold"),anchor="w",bg='white')
        self.gender_label.place(x=70,y=230)
        self.gender = IntVar()
        self.gender_radiobutton1 = Radiobutton(self.mainframe, text="Male", variable=self.gender, value= "Male", font=("times",12),bg='white')
        self.gender_radiobutton1.pack(pady=5)
        self.gender_radiobutton1.place(x=235,y=230)
        self.gender_radiobutton2 = Radiobutton(self.mainframe, text="Female", variable=self.gender, value="Female", font=("times",12),bg='white')
        self.gender_radiobutton2.pack(pady=5)
        self.gender_radiobutton2.place(x=315,y=230)

        #Passport Entry/label
        self.passport_label = Label(self.mainframe, text="Valid Passport (7 digits)",width=20,font=("times",12,"bold"),anchor="w",bg='white')
        self.passport_label.place(x=70,y=260)
        self.passport_digits_var = IntVar()
        self.passport_entry = Entry(self.mainframe,width=30,bd=2, text = self.passport_digits_var)
        self.passport_entry.place(x=240,y=260)
       
        #Calendar
        #From date
        self.from_date_label = Label(self.mainframe, text = "From", width = 20, font = ("times", 12, "bold"), anchor = "w", bg = 'white')
        self.from_date_label.place(x = 70, y = 290)
        self.from_date_entry = DateEntry(self.mainframe, width = 27, background = 'brown', foreground = 'white', date_pattern = 'dd/mm/Y', borderwidth = 3)
        self.from_date_entry.place(x = 240, y = 290)

        #Due date
        self.to_date_label = Label(self.mainframe, text = "To", width = 20, font = ("times", 12, "bold"), anchor= "w" , bg = 'white')
        self.to_date_label.place(x = 70,y = 320)
        self.to_date_entry = DateEntry(self.mainframe, width = 27, background= 'brown', foreground = 'white', date_pattern = 'dd/mm/Y', borderwidth = 3)
        self.to_date_entry.place(x = 240, y = 320)
        
        global choice_variable
        choice_variable = StringVar()
        #Room type option
        def accomodation_opt():

            def gender_value():
                value = self.gender.get()
                if value == 'Female':
                    return 'Female'
                else:
                    return 'Male'

            gender = gender_value()
            if gender == 'Male':
                #Dropdown menu "male"
                choice_variable.set("Male")
                option = ("Male Dorm", "Single Room", "Double Room")
                option_menu = OptionMenu(self.mainframe, choice_variable, *option)
                option_menu.config(font=("times", 16), bd=3, bg="white")
                option_menu.place(x=240, y=380, width=190)
            else:
                #Dropdown menu "female"
                choice_variable.set("Female")
                option = ("Female Dorm", "Single Room", "Double Room")
                option_menu = OptionMenu(self.mainframe, choice_variable, *option)
                option_menu.config(font=("times", 11), bd=3, bg="white")
                option_menu.place(x=240, y=380, width=190)

        #Save info to DB
        def get_customer_details():

            global details
            name = self.name_entry.get()
            country = self.country_entry.get()
            def gender_value():
                value = self.gender.get()

                if (self.gender == 'Male'):
                     value = 'Male'
                else: 
                     value = 'Female'
                return value
            gender = gender_value()
            passport = self.passport_entry.get()
            from_date = self.from_date_entry.get()
            to_date = self.to_date_entry.get()
            room = choice_variable.get()

            Hostel_Database.create_table()
            con = sqlite3.connect('Hostel_db.db')
            cur = con.cursor()
            cur.execute('INSERT INTO Booking_Details (Name, Country, Gender, Passport, FromDate, ToDate, Room_Type)' 'VALUES (?,?,?,?,?,?,?)', (name, country, gender, passport, from_date, to_date, room))
            con.commit()
            cur.execute('SELECT * FROM Booking_Details')
            print(cur.fetchall())

        #Save to txt/csv
        def save():
            gender = self.gender.get()
            room = choice_variable.get()
            db = self.from_date_entry.get_date()
            d = db.strftime('%d/%m/%Y')
            db1 = self.to_date_entry.get_date()
            td = db1.strftime('%d/%m/%Y')
            now = datetime.datetime.now()
            if (self.gender == 'Male'):
                gender = 'male'
            else:
                gender = 'female'

            #Save in txt
            s = '\n'+ now.strftime("%d-%m-%Y %H:%M") + " " + '\t ' + " "+ "Name: " + self.name_entry.get() + " " + '\t ' + "County: " + self.country_entry.get() + " " + '\t ' + "Passport: " + self.passport_entry.get() + " " + '\t ' + "From: " + d + " " + '\t ' + "Due: " + td + " " + '\t ' + " " + "Gender: " + gender + ' \t ' + " " +"Type of room: "+ room
            f = open(('regdetails.txt'), 'a')
            f.write(s)
            f.close()
            try:

                #Save in csv
                with open('Regfile.txt', 'a') as fs:
                    w = csv.writer(fs)
                    w.writerow(["Booked on: "+ now.strftime("%d-%m-%Y %H:%M"), " by: " + self.name_entry.get(),
                                " country: " + self.country_entry.get()," passport: " + self.passport_entry.get()," booked from: " + d," booked until: " + td,
                                " gender: " + gender," room booked: " + room])
                    fs.close()
            except:
                print("Close the data file")

        #Room button
        self.room_options_button = Button(self.mainframe, text = 'Check available room options', command = accomodation_opt, width=22, bg = 'white', font = ("times",12,"bold"))
        self.room_options_button.place(x = 240, y = 350)
        
        #Booking finish button
        self.submit_form_button = Button(self.mainframe, text = "Booking complete", bg = 'white', command = get_customer_details, font = ("times", 12, "bold"))
        self.submit_form_button.place(x = 100, y = 350)

        #Save button to txt/csv
        self.save_button = Button(self.mainframe, text="Save to txt/csv", command=save, font=("times", 12, "bold"), bg='white')
        self.save_button.place(x=180, y=400)
            
        
#Booking page function
def booking_page():
    root = Tk()
    desktop = Booking(root)
    root.mainloop()
