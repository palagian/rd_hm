# 2. Використовуючи API для погоди https://open-meteo.com/en/docs, написати програму, яка буде приймати від користувача назву міста і
# виводити поточні показники погоди в консоль.
# Для визначення координат міста можна використати https://open-meteo.com/en/docs/geocoding-api

import requests

def get_weather(city_name):
    # Getting city coordinates from geocoding
    geocoding_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=10&language=en&format=json'
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()

    if len(geocoding_data) > 0 and 'results' in geocoding_data:
        results = geocoding_data['results']
        for result in results:
            if result['name'] == city_name:
                latitude = result['latitude']
                longitude = result['longitude']

    else:
        print(f'City {city_name} not found.')
        return

    # Get weather data by coordinates
    weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Displaying current weather indicators
    current_temperature = weather_data['hourly']['temperature_2m'][0]

    print(f'Temperature in the city {city_name}: {current_temperature}°C')

# Requesting a city name from a user
city_name = input('Enter the city name: ').capitalize()

# Getting the temperature
get_weather(city_name)





