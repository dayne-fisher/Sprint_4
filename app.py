
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

min_days_listed, max_days_listed = int(df['days_listed'].min()), int(df['days_listed'].max())

days_listed_range = st.slider("Select Number of Days Listed", value=(min_days_listed, max_days_listed), min_value=min_days_listed, max_value=max_days_listed)
days_listed_range[0]
days_listed_range[1]

actual_range = list(range(days_listed_range[0], days_listed_range[1]+1))


df_filtered = df[ (df.model == selected_manu) & df.model_year.isin(list(actual_range))]


st.header("Days Posted Analysis")
st.write(""" Let's analyze what variable influences days posted the most between Condition or Model Year""")

list_for_hist = ['condition', 'model_year']
selected_var = st.selectbox('Filter for Days Posted Difference', list_for_hist)


fig1 = px.histogram(df, x="days_listed", color= selected_var)
fig1.update_layout(title = "<b> Split of Days Posted by {}</b>".format(selected_var))
st.plotly_chart(fig1)

st.write(""" After viewing the data, we can tell that the condition influences the number of days listed. """)

def age_category(x):
    if x<5: return '<5'
    elif  x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
df['age'] = 2024 - df['model_year']
df['age_category'] = df['age'].apply(age_category)

list_for_scatter = ["paint_color", "is_4wd", "type"]

choice_for_scatter = st.selectbox('Days Listed depending on', list_for_scatter)

fig2 = px.scatter(df, x='days_listed', y= choice_for_scatter, color = "age_category", hover_data= ["model_year"])
fig2.update_layout(title = "<b> Days Listed vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)

st.write("""After viewing the data, we can tell that that the odometer number influences the number of days listed. """)


st.write (""" Overall, even though other factors come into play about how long a vehicle is listed, the condition has the greastest impact of the amount of days listed for vehicles in the US.  """)