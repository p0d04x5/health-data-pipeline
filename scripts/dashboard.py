import streamlit as st
import pandas as pd
import sqlite3

# Set Streamlit page title
st.set_page_config(page_title="Health Data Dashboard", layout="wide")

# Connect to the SQLite database
conn = sqlite3.connect("health.db")

# Load the data from the database
df = pd.read_sql_query("SELECT * FROM health_data", conn)

# Dashboard title
st.title("💪 Health Data Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Basic stats
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Age distribution
if "age" in df.columns:
    st.subheader("📈 Age Distribution")
    st.bar_chart(df["age"].value_counts().sort_index())

# Gender distribution
if "gender" in df.columns:
    st.subheader("👫 Gender Distribution")
    st.bar_chart(df["gender"].value_counts())

# Close DB connection
conn.close()
