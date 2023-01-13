# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#quickstart.py

# Imports
import streamlit as st
import pandas as pd

# Load data
# Parse UK style dates i.e. 31/12/2022
df=pd.read_csv("trainexpensesJan2023.csv",index_col='date',
                 parse_dates = True,
                 dayfirst=True,
                 usecols = ['date', 'vote', 'amount'])
# Create a title for your app
st.title("Personal Inter-City Transport Costs")

# A description
st.write("Here are the Costs by date:")



# SIDEBAR
# -----------------------------------------------------------
sidebar = st.sidebar
df_display = sidebar.checkbox("Display Raw Data", value=True)

#df_display = st.checkbox("Display Data", value=True)
# Display the dataframe
if df_display:
    st.write(df)
#st.write(df)