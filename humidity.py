def get_top_n_cities_by_humidity(weather_stats, n):
    return sorted(weather_stats, key=lambda x: x[2], reverse=True)[:n]

