def read_cities(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        cities = [row[0] for row in csv_reader]
    return cities

