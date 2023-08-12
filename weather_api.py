# import libraries
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    import requests
import json
import sys


# function to get weather data
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the weather data.")
        print(e)
        return
    except json.JSONDecodeError as e:
        print("An error occurred while parsing the weather data.")
        print(e)
        return

    if weather_data.get("cod") == "404":
        print(f"City '{city_name}' not found. Please check the spelling and try again.")
        return

    # printing the information
    print(f"Weather forecast for {weather_data['name']}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind speed: {weather_data['wind']['speed']} m/s")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the name of a city as an argument.")
        sys.exit(1)
    api_key = "your-api-key"
    city_name = " ".join(sys.argv[1:])
    get_weather(city_name, api_key)
