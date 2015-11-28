#!/usr/bin/env python3
import json


def get_time_as_list(t):
    return [int(i) for i in t.split(":")]

with open('../config.json') as data_file:
    config = json.load(data_file)

OWM_API_KEY = config['owm_api_key']
CITY = config['city']
BOT_API_TOKEN = config['bot_api_token']
TELEGRAM_USER_ID = config['telegram_user_id']
FORECAST_TIME = get_time_as_list(config["forecast_time"])
NIGHTLY_ALARM_TIME = get_time_as_list(config["nightly_alarm_time"])
DAILY_ALARM_TIME = get_time_as_list(config["daily_alarm_time"])
