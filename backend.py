import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("API_KEY")


def get_data(place, forecast_days, kind):
    geo_url =  f"https://api.openweathermap.org/geo/1.0/direct?q={place}&limit={1}&appid={api_key}"

    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    if not geo_data:
        return f"No location found for '{place}'"

    lat = geo_data[0]['lat']
    long = geo_data[0]['lon']
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    return data



if __name__ == '__main__':
    print( get_data('manila', 4, 'temperature'))