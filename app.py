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

actual_range = list(range(price_range[0], price_range[1]+1))


df_filtered = df[ (df.manufacturer_name == selected_manu) & df.model_year.isin(list(actual_range))]


st.header("Days Posted Analysis")
st.write(""" Let's analyze what variable influences price the most between Condition, Model Year and Odometer""")

list_for_hist = ['condition', 'model_year', 'odometer']
selected_var = st.selctbox('Filter for Days Posted Difference', list_for_hist)


fig1 = px.histogram(df, x="days_listed", color= selected_var)
fig1.update_layout(title = "<b> Split of Days Posted by {}</b>".format(selected_var))
st.plotly_chart(fig1)


def age_category(x):
    if x<5: return '<5'
    elif  x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
df['age'] = 2024 - df['model_year']
df['age_category'] = df['age'].apply(age_category)

list_for_scatter = ["odometer", "paint_color", "is_4wd", "type"]

choice_for_scatter = st.selectbox('Days Listed depending on', list_for_scatter)

fig2 = px.scatter(df, x='days_listed', y= choice_for_scatter, color = "age_category", hover_data= ["model_year"])
fig2.update_layout(title = "<b> Days Listed vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)

