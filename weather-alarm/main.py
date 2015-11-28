#!/usr/bin/env python3
import json
import pyowm

with open('../config.json') as data_file:
    config = json.load(data_file)

API_KEY = config['owm_api_key']
CITY = config['owm_city']

owm = pyowm.OWM(API_KEY)
forecast = owm.daily_forecast(CITY)

tomorrow = pyowm.timeutils.tomorrow(8,00)

print(forecast.will_be_sunny_at(tomorrow))

observation = owm.weather_at_place(CITY)
w = observation.get_weather()
print(w.get_rain())
print(w.get_status())
