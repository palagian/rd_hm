# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
# Реалізувати за допомогою модуля requests з використанням мультипотоковості і мультипроцесорності.

import threading
import requests
import multiprocessing

cities = [
    {"city": "Kyiv", "latitude": 50.45, "longitude": 30.52},
    {"city": "Vilnius", "latitude": 54.69, "longitude": 25.28},
    {"city": "New York", "latitude": 40.71, "longitude": -74.01},
    {"city": "Venice", "latitude": 45.44, "longitude": 12.33},
    {"city": "Lisbon", "latitude": 38.72, "longitude": -9.13}
]

def get_weather(city):
    """ function for getting temperature """
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
        timeout = 15
    )
    data = resp.json()
    # checking if there is data for the needed city
    if "hourly" in data and "temperature_2m" in data["hourly"] and len(data["hourly"]["temperature_2m"]) > 0:
        temperature = data['hourly']['temperature_2m'][0]
        print(f"Temperature in {city['city']}: {temperature}°C")
    else:
        print(f"Could not get weather data for {city['city']}.")


# creating threads for each city
def thread_only():
    threads = []
    for city in cities:
        thread = threading.Thread(target=get_weather, args=(city,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# creating processes for each city
def multi_process():
    processes = []

    for city in cities:
        process = multiprocessing.Process(target=get_weather, args=(city, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    # multi_process()
    thread_only()





