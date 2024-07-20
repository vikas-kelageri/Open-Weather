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

