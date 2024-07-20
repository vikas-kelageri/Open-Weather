import requests
import csv
import pandas as pd

API_KEY = "YOUR_API_KEY"
CITY_FILE = "city.csv"
CITY_STATS_FILE = "city_stats.csv"
N = 3

def get_city_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data:
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon
    return None, None

