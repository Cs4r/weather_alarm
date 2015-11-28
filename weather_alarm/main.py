#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from weather_alarm.constants import *
from weather_alarm.weather_delegate import WeatherDelegate
from weather_alarm.bot_delegate import BotDelegate


bot = BotDelegate(BOT_TOKEN)
weather = WeatherDelegate(OWM_API_KEY)


def send_tomorrow_forecast(hour, time):
    bot.send_msg_to_user(TELEGRAM_USER_ID, weather.tomorrow_forecast_at(CITY, hour, time))


def send_current_observed_weather():
    bot.send_msg_to_user(TELEGRAM_USER_ID, weather.current_observed_weather(CITY))

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