import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

st.header("Ads of Vehicles in the US")
st.write("Filter the data below to see the by each manufacturer")

df = pd.read_csv('vehicles_us.csv')
df = df.drop(df.columns[0], axis=1)

model_choice = df['model'].unique()

selected_manu = st.selectbox('Select a Model', model_choice)

min_price, max_price = int(df['price'].min()), int(df['price'].max())

price_range = st.slider("Select Price", value=(min_price, max_price), min_value=min_price, max_value=max_price)
price_range[0]
price_range[1]

range(price_range[0], price_range[1])


df_filtered = df[ df.manufacturer_name == selected_manu]





df_filtered

