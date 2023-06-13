from typing import Tuple
import requests


API_KEY = "7598a17dae98564b0adfa271f40a66e7"
API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(city: str) -> Tuple[str]:
    """
    Get weather data from OpenWeatherMap API.
    Returns a tuple containing the current temperature and 
    weather description.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    r = requests.get(API_URL, params=params)
    data = r.json()
    return data['main']['temp'], data['weather'][0]['description']


