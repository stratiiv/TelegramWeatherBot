from typing import Tuple
import requests


API_KEY = "7598a17dae98564b0adfa271f40a66e7"
API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(location: str | Tuple[float, float]) -> Tuple[str]:
    """
    Get weather data from OpenWeatherMap API.
    Args:
        location (str | Tuple[float, float]):
        The location can be either a city name (str) or
        a tuple containing latitude and longitude coordinates (float).
    Returns:
        Tuple[str]: A tuple containing the current temperature and
        weather description.
    """

    if isinstance(location, str):
        params = {
            "q": location,
            "appid": API_KEY,
            "units": "metric"
        }
    elif isinstance(location, tuple):
        params = {
            "lat": location[0],
            "lon": location[1],
            "appid": API_KEY,
            "units": "metric"
        }

    r = requests.get(API_URL, params=params)
    data = r.json()
    return data['main']['temp'], data['weather'][0]['description']
