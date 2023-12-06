# main class
import tkinter
from tkinter import *
from tkinter import ttk
import Booking
import Modify_Booking


class HostelBooking:

    #Gui
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x500')
        self.root.title("EcoHostel")
        self.root.configure(bg = 'white')

        
        #Container
        self.mainframe = ttk.Frame(self.root, padding = "3 3 12 12")
        self.mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)
        
        #Welcome page banner
        self.label = Label(self.mainframe, text = "EcoHostel Booking", width = 50 ,font = ("times", 20,"bold"), fg = 'black', anchor = 'n')
        self.label.place(x = -100, y = 50)
   
        #Welcome page Button (Make booking)
        self.registration_button = Button(self.mainframe, text = "Make Your Booking", command = Booking.booking_page, font = ("times", 14), bg='white', anchor = 'center')
        self.registration_button.place(x = 200, y = 200)

        #Welcome page Button (Modify)
        self.modify_booking = Button(self.mainframe, text = "Modify Booking", command = Modify_Booking.modify_booking_page, font = ("times", 14), bg = 'white', anchor = 'center')
        self.modify_booking.place(x = 200, y = 250)

#Welcome page function
def welcome_page():
    root = Tk()
    desktop = HostelBooking(root)
    root.mainloop()

if __name__ == '__main__':
    welcome_page()
