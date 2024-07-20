def get_top_n_cities_by_temperature(weather_stats, n):
    return sorted(weather_stats, key=lambda x: x[1])[:n]

