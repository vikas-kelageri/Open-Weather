def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if 'current' in data:
        temp = data['current']['temp']
        humidity = data['current']['humidity']
        return temp, humidity
    return None, None

