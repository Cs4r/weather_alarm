from twx.botapi import TelegramBot


class BotDelegate:
    def __init__(self, bot_token):
        self.bot = TelegramBot(bot_token)

    def send_msg_to_user(self, user_id, message):
        self.bot.send_message(user_id, message).wait()