import streamlit as st
import pandas as pd
from support import add, update,visualize,delete
from db import *
import csv
import os 

def main():
    st.title("Visualization App")
    menu = ["Add","Delete","Update","Visualize"]
    options = st.sidebar.selectbox("Menu",menu)
    create_table()
    if options =="Add":
          add()
    elif options == "Delete":
          delete()
    elif options == "Update":
          update()       
    elif options == "Visualize":
          visualize()
    #Exporting data into CSV file
    print('Exporting data into CSV file.....')
    cursor = con.cursor()
    cursor.execute("SELECT * from valuestable")
    with open("value_data.csv","w") as csv_file:
        csv_writer = csv.writer(csv_file,delimiter="\t")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    dirpath = os.getcwd() + "/value_data.csv"
    print("Data Exported into {}".format(dirpath))
 

if __name__== '__main__':
    main()