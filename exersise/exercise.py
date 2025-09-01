import streamlit as st
import plotly.express as px
import pandas as pd

st.header('In Search for Happiness')
x_axis = st.selectbox('Select data for the X-Axis', ('GDP', 'Happiness'))
y_axis = st.selectbox('Select data for the Y-Axis', ('GDP', 'Generosity', 'Happiness'))

df = pd.read_csv('../data/happy.csv')

st.subheader(f'{x_axis} and {y_axis}')
fig = px.scatter(x=df[x_axis.lower()], y=df[y_axis.lower()])
st.plotly_chart(fig)

x = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]  # Perfect straight line (y = 2*x)
})


st.plotly_chart(px.scatter(x=x['x'], y=x['y']))