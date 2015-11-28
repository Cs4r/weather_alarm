from twx.botapi import TelegramBot


class NotificationSender:
    def __init__(self, bot_token, user_id):
        self.bot = TelegramBot(bot_token)
        self.user_id = user_id

    def send_message(self, message):
        self.bot.send_message(self.user_id, message).wait()