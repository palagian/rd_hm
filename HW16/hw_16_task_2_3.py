# 2. Знайти середню температуру по прогнозу для кожного міста і вивести в якому місті зараз найспекотніше.
# 3. Вивести різницю по часу виконання програми використовуючи потоки і процеси.

import threading
import requests
import multiprocessing
import time

cities = [
    {"city": "Kyiv", "latitude": 50.45, "longitude": 30.52},
    {"city": "Vilnius", "latitude": 54.69, "longitude": 25.28},
    {"city": "New York", "latitude": 40.71, "longitude": -74.01},
    {"city": "Venice", "latitude": 45.44, "longitude": 12.33},
    {"city": "Lisbon", "latitude": 38.72, "longitude": -9.13}
]


def get_avg_temp(city):
    """ function for calculating average temperature """
    latitude = city["latitude"]
    longitude = city["longitude"]
    resp = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
        },
        # increasing timeout for avoiding "requests.exceptions.ReadTimeout" error from server
        timeout = 60
    )
    data = resp.json()
    if "hourly" in data and "temperature_2m" in data["hourly"] and len(data["hourly"]["temperature_2m"]) > 0:
        temperature_list = data['hourly']['temperature_2m']
        avg_temperature = sum(temperature_list) / len(temperature_list)
        return avg_temperature
    else:
        print(f"Could not get weather data for {city['city']}.")
        return None


def timer(func):
    """ function for calculating time of function execution"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to execute")
        return result
    return wrapper

@timer
# creating threads for each city
def thread_only():
    threads = []
    for city in cities:
        thread = threading.Thread(target=get_avg_temp, args=(city, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

@timer
# creating processes for each city
def multi_process():
    processes = []
    for city in cities:
        process = multiprocessing.Process(target=get_avg_temp, args=(city, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    multi_process()
    thread_only()


    # collecting average temperatures of cities
    avg_temperatures = []
    for city in cities:
        avg_temp = get_avg_temp(city)
        if avg_temp:
            avg_temperatures.append(avg_temp)

    # outputting the average temperature for each city
    print("\nAverage temperatures for all cities:")
    for i, city in enumerate(cities):
        print(f"{i+1}. {city['city']}: {avg_temperatures[i]:.2f}°C")

    # finding the hottest city
    hottest_city = cities[avg_temperatures.index(max(avg_temperatures))]["city"]
    print(f"\nThe hottest city: {hottest_city}")
