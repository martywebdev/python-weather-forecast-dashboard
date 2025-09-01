import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox('Select data to view',
                      ("Temperature", "Sky"))

st.subheader(f'{option} for the next {days} days in {place}')

def get_data(days):
    dates = ["2025-09-01", "2025-09-02", "2025-09-03"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]

    return dates, temperatures

date, temp = get_data(days)
figure = px.line(x=date, y=temp, labels={"x": "Date", 'y': "Temperature (c)"})
st.plotly_chart(figure)