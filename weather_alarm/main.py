#!/usr/bin/env python3
import pyowm
from twx.botapi import TelegramBot
import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from weather_alarm.constants import *


def send_tomorrow_forecast(hour, time):
    notify_bot(tomorrow_forecast_at(hour, time))


def send_current_observed_weather():
    notify_bot(current_observed_weather())


def notify_bot(message):
    bot = TelegramBot(BOT_API_TOKEN)
    bot.update_bot_info().wait()
    bot.send_message(TELEGRAM_USER_ID, message).wait()


def tomorrow_forecast_at(hour=0, minute=0):
    owm = pyowm.OWM(OWM_API_KEY)
    forecast = owm.three_hours_forecast(CITY)
    tomorrow = pyowm.timeutils.tomorrow(hour, minute)
    weather = forecast.get_weather_at(tomorrow)
    precipitation = forecast.will_be_rainy_at(tomorrow) or forecast.will_be_stormy_at(
        tomorrow) or forecast.will_be_foggy_at(
        tomorrow) or forecast.will_be_snowy_at(tomorrow)

    return format_weather_forecast(CITY, tomorrow, weather.get_detailed_status(), precipitation)


def current_observed_weather():
    def check_precipitation(d):
        return False if len(d) == 0 else d['3h'] > 0

    owm = pyowm.OWM(OWM_API_KEY)
    weather = owm.weather_at_place(CITY).get_weather()
    precipitation = check_precipitation(weather.get_rain()) or check_precipitation(weather.get_snow())

    return format_weather_forecast(CITY, datetime.datetime.now(), weather.get_detailed_status(), precipitation)


def format_weather_forecast(city, date, status, precipitation):
    message = "Weather forecast for %s on %s at %s:\n\n" % (
        city, date.strftime("%B, %d"), date.strftime("%H:%M"))
    message += "\tStatus: %s\n" % status
    message += "\tShould you take an umbrella?: %s" % ("Yes" if precipitation else "No")
    return message


now = datetime.datetime.now()
nightly_alarm_time = datetime.datetime(now.year, now.month, now.day, *NIGHTLY_ALARM_TIME)
daily_alarm_time = datetime.datetime(now.year, now.month, now.day, *DAILY_ALARM_TIME)

scheduler = BlockingScheduler()

scheduler.add_job(func=send_tomorrow_forecast, args=FORECAST_TIME, trigger='interval', next_run_time=nightly_alarm_time,
                  misfire_grace_time=30, days=1)

scheduler.add_job(func=send_current_observed_weather, trigger='interval', next_run_time=daily_alarm_time,
                  misfire_grace_time=30, days=1)

print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass