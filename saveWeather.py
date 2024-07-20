def save_weather_stats(weather_stats, file_name):
    df = pd.DataFrame(weather_stats, columns=["City", "Temperature", "Humidity"])
    df.to_csv(file_name, index=False)

