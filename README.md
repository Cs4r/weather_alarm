# weather-alarm
This software warns me (using [Telegram](https://telegram.org/)) whether the weather is going to change abruptly so that I know if I have to take my umbrella before going to work

## Support
weather-alarm has been developed to run on Python 3.4

## Installation

First of all, is mandatory to install the following modules through pip (Or your favorite package management system for python, although I prefer pip due to its simplicity):

- [PyOWM] (https://github.com/csparpa/pyowm)
- [twx.botapi] (https://github.com/datamachine/twx.botapi)
- [APScheduler] (https://apscheduler.readthedocs.org/en/latest/index.html)

In order to accomplish such a task, just execute the following commands:

```pip install pyowm```

```pip install twx.botapi```

```pip install apscheduler```

Yippee! Now all the required external modules are installed :smiley:


## Configuration

Finally, fill the config.json file in with your data. It will look like this:

```
{
  "owm_api_key": "55x62cbf16xx2956ef191185fdee4000",
  "city": "Granada, ES",
  "bot_token": "155277833:BBGZP-WY5tXXXUjW5az5bFCNbEFR0N",
  "telegram_user_id": 1234567,
  "forecast_time": "8:30",
  "nightly_alarm_time": "23:00",
  "daily_alarm_time": "8:00"
}
```

## Run

Simply execute:

```python3 main.py```

