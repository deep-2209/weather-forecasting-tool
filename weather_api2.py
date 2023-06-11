# write a code to fetch weather information from OpenWeatherAPI of a particular city, and print the following information in the console:
#     Temperature
#     Weather
#     Humidity
#     Wind speed
# Note: Please use the requests module

# Solution:
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    import requests
import json
import os

# API key
api_key = os.environ.get('WEATHER_API_KEY')
# city name
city_name = input("Enter city name : ")
# complete url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object convert
# json format data into python format data
x = response.json()
# print the following information
print("Temperature : " + str(x['main']['temp']))
print("Weather : " + str(x['weather'][0]['description']))
print("Humidity : " + str(x['main']['humidity']))
# json format data into