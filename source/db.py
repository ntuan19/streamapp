import sqlite3
#create connection object that represents the database.
#data would be stored in mydatabase.db
con = sqlite3.connect('mydatabase.db',check_same_thread=False)
#Creating a cursor object using the cursor() method
c = con.cursor()
import csv

#Database
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS valuestable(value TEXT,value_status TEXT,date DATE )')
def add_data(value,value_status,date):
    c.execute('INSERT INTO valuestable(value,value_status,date) VALUES(?,?,?)',(value,value_status,date))
    con.commit()
def view_data():
    c.execute('SELECT * FROM valuestable')
    data = c.fetchall()
    return data
def view_unique_value():
    c.execute('SELECT DISTINCT value from valuestable ')
    data = c.fetchall()
    return data
def get_value(value):
    c.execute('SELECT * FROM valuestable WHERE Value="{}"'.format(value))
    data = c.fetchall()
    return data

def edit_value(changing_value,changing_status,changing_date,change_to):
     c.execute("UPDATE valuestable SET value =?,value_status=?,date=? WHERE value=? ",(change_to,changing_status,changing_date,changing_value))
     con.commit()
     data = c.fetchall()
     return data
def delete_value(deleting_value):
    c.execute('DELETE FROM valuestable WHERE value="{}"'.format(deleting_value))
    con.commit()
