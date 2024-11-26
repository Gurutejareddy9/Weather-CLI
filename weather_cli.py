# weather_cli.py
import requests
from config import OPENWEATHERMAP_API_KEY, OPENWEATHERMAP_API_URL

def get_weather(city, api_key, base_url):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use metric for Celsius, or 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    if weather_data['cod'] == '404':
        print(f"City '{city}' not found.")
        return
    main = weather_data['main']
    wind = weather_data['wind']
    weather = weather_data['weather'][0]
    print(f"Weather in {city}:")
    print(f"  - **Description:** {weather['description']}")
    print(f"  - **Temperature:** {main['temp']}°C")
    print(f"  - **Feels Like:** {main['feels_like']}°C")
    print(f"  - **Humidity:** {main['humidity']}%")
    print(f"  - **Wind Speed:** {wind['speed']} m/s")

def main():
    print("Weather CLI")
    print("------------")
    city = input("Enter the city name to check its weather: ")
    get_weather(city, OPENWEATHERMAP_API_KEY, OPENWEATHERMAP_API_URL)

if __name__ == "__main__":
    main()
