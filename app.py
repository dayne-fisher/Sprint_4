import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

st.header("Market of Vehicles in the US")
st.write("Filter the data below to see the by each manufacturer")

df = pd.read_csv('vehicles_us.csv')
df = df.drop(df.columns[0], axis=1)

manufacturer_choice = df['manufacturer_name'].unique()

st.selectbox('Select a Manufacturer')

