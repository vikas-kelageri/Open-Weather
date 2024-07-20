### Pre-setup Steps:
1. Register at OpenWeatherMap: Go to [OpenWeatherMap](https://openweathermap.org/) and sign up.
2. Generate an API Key: After signing in, generate an API key.

### Automation Steps:

1. Create a file named `city.csv` and add a list of cities.
2. Get the longitudes and latitudes for the city using the Geocoding API.
3. Use the latitude and longitude information to get the weather report using the One Call API.
4. Save all the stats into a CSV file named `city_stats.csv`.
5. Add a Test Suite to get various weather statistics.

### Required Libraries:
First, install the necessary Python libraries:

```bash
pip install requests pandas
```

### Python Script:

```python
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

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if 'current' in data:
        temp = data['current']['temp']
        humidity = data['current']['humidity']
        return temp, humidity
    return None, None

def read_cities(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        cities = [row[0] for row in csv_reader]
    return cities

def save_weather_stats(weather_stats, file_name):
    df = pd.DataFrame(weather_stats, columns=["City", "Temperature", "Humidity"])
    df.to_csv(file_name, index=False)

def get_top_n_cities_by_temperature(weather_stats, n):
    return sorted(weather_stats, key=lambda x: x[1])[:n]

def get_top_n_cities_by_humidity(weather_stats, n):
    return sorted(weather_stats, key=lambda x: x[2], reverse=True)[:n]

def main():
    cities = read_cities(CITY_FILE)
    weather_stats = []

    for city in cities:
        lat, lon = get_city_coordinates(city)
        if lat is not None and lon is not None:
            temp, humidity = get_weather(lat, lon)
            if temp is not None and humidity is not None:
                weather_stats.append([city, temp, humidity])
    
    save_weather_stats(weather_stats, CITY_STATS_FILE)
    
    top_coldest_cities = get_top_n_cities_by_temperature(weather_stats, N)
    top_humid_cities = get_top_n_cities_by_humidity(weather_stats, N)
    
    print(f"Top {N} Coldest Cities:")
    for city in top_coldest_cities:
        print(f"{city[0]} - {city[1]}°C")

    print(f"\nTop {N} Cities with Highest Humidity:")
    for city in top_humid_cities:
        print(f"{city[0]} - {city[2]}%")

if __name__ == "__main__":
    main()
```

### Explanation:

1. `get_city_coordinates(city)`: Fetches the latitude and longitude of a city using the OpenWeatherMap Geocoding API.
2. `get_weather(lat, lon)`: Fetches the weather data for the given latitude and longitude using the OpenWeatherMap One Call API.
3. `read_cities(file_name)`: Reads the list of cities from a CSV file.
4. `save_weather_stats(weather_stats, file_name)`: Saves the weather statistics to a CSV file.
5. `get_top_n_cities_by_temperature(weather_stats, n)`: Returns the top `n` cities with the lowest temperature.
6. `get_top_n_cities_by_humidity(weather_stats, n)`: Returns the top `n` cities with the highest humidity.
7. `main()`: Main function to execute the steps.

Make sure to replace `"
"` with your actual OpenWeatherMap API key and ensure that your `city.csv` file contains the list of cities you want to analyze. This script will read the cities, fetch their weather data, save the stats to a CSV file, and then print the top `N` coldest and most humid cities.
