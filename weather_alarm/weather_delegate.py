import pyowm
import datetime


class WeatherDelegate:
    def __init__(self, api_key):
        self.__owm = pyowm.OWM(api_key)

    def tomorrow_forecast_at(self, city, hour=0, minute=0):
        forecast = self.__owm.three_hours_forecast(city)
        tomorrow = pyowm.timeutils.tomorrow(hour, minute)
        weather = forecast.get_weather_at(tomorrow)
        precipitation = forecast.will_be_rainy_at(tomorrow) or forecast.will_be_stormy_at(
            tomorrow) or forecast.will_be_foggy_at(
            tomorrow) or forecast.will_be_snowy_at(tomorrow)

        return self.__format_weather_forecast(city, tomorrow, weather.get_detailed_status(), precipitation)

    def current_observed_weather(self, city):
        def check_precipitation(d):
            return False if len(d) == 0 else d['3h'] > 0

        weather = self.__owm.weather_at_place(city).get_weather()
        precipitation = check_precipitation(weather.get_rain()) or check_precipitation(weather.get_snow())

        return self.__format_weather_forecast(city, datetime.datetime.now(), weather.get_detailed_status(), precipitation)

    @staticmethod
    def __format_weather_forecast(city, date, status, precipitation):
        message = "Weather forecast for %s on %s at %s:\n\n" % (
            city, date.strftime("%B, %d"), date.strftime("%H:%M"))
        message += "\tStatus: %s\n" % status
        message += "\tShould you take an umbrella?: %s" % ("Yes" if precipitation else "No")
        return message
