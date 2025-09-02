import streamlit as st
import plotly.express as px
from plotly.tools import return_figure_from_figure_or_data

from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ', value='Manila')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox('Select data to view',
                      ("Temperature", "Sky"))


st.subheader(f'{option} for the next {days} days in {place}')


try:
    filtered_data = get_data(place, days, option)
    if option == 'Temperature':
        temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]

        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", 'y': "Temperature (c)"})
        st.plotly_chart(figure)

    if option == 'Sky':
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        images = { "Clear": "images/clear.png", "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png",}

        image_paths = [images[condition] for condition in sky_conditions]

        st.image(image_paths, width=115)
except (KeyError, FileNotFoundError, TypeError) as e:
    st.error(f"An error occurred: {e}")