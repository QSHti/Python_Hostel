#database

import sqlite3

def get_connection():
    con = sqlite3.connect('Hostel_db.db')
    return con
def close_connection(con):
    if con:
        con.close()

def create_table():

 con = get_connection()
 cur = con.cursor()
 cur.execute('''create table if not exists Booking_Details (
             Name text primary key,   
             Country text,
             Gender text,
             Passport int,
             FromDate int,
             ToDate int,
             Room_Type text)''')
 close_connection(con)

get_connection()
create_table()
