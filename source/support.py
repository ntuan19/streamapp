import streamlit as st
from db import add_data,view_unique_value,get_value,view_data,edit_value,delete_value
import pandas as pd
def add():
    st.subheader("Add Items")
        #Layout:
    col1,col2 = st.beta_columns(2)
    with col1:
        value1 = st.text_area("Col 1")
    with col2:
        value2 = st.selectbox("Status",["Verified","Pending","False"])
        input_time = st.date_input("Time")
    if st.button("Submit"):
        add_data(value1,value2,input_time)
        st.success("Successfully Sent Data:{}".format(value1))

def update():
        st.subheader("Update Data")
        col3,col4 = st.beta_columns(2)
        with st.beta_expander("View specific results"):
               df = pd.DataFrame(view_unique_value())
               st.write(df)
        with col3:
             value_needs_change = st.text_area("Value to change")
        with col4:
             change_to = st.text_area("The desired value")
        if st.button("Submit"):
             k = get_value(value_needs_change)
             for i in range(len(k)):
                 changing_status=k[i][1]
                 changing_date = k[i][2]
                 m = edit_value(value_needs_change,changing_status,changing_date,change_to)
             st.subheader("Changed data")
             result1 = view_data()
             df = pd.DataFrame(result1)
             st.write(df)

def visualize():
        st.subheader("Visualize Data")
        result = view_data()
        with st.beta_expander("Give me all the juice"):
               df = pd.DataFrame(result,columns = ['Value','Status','Date'])
               st.write(df)
        with st.beta_expander('Provide the values'):
               value_df = df['Value'].to_frame()
               st.dataframe(value_df)
        with st.beta_expander('Provide the dates'):
               value_df = df['Date'].to_frame()
               st.dataframe(value_df)

def delete():
        st.subheader("Delete Data")
        col5,col6 = st.beta_columns(2)
        with st.beta_expander("View specific results"):
            df = pd.DataFrame(view_unique_value())
            st.write(df)
        with col5:
            value_to_delete = st.text_area("Value needs deleting")
        if st.button("Submit"):
             k = get_value(value_to_delete)
             for i in range(len(k)):
                 delete_value(value_to_delete)
             st.subheader("Changed data")
             result1 = view_data()
             df = pd.DataFrame(result1)
             st.write(df)