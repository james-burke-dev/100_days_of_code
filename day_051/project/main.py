
from speed_tweeter import InternetSpeedTwitterBot
import os 

ACCOUNT_EMAIL = os.environ.get("EMAIL_ADDRESS")
ACCOUNT_PASSWORD = os.environ.get("PASSWORD")

PROMISED_DOWN = 150
PROMISED_UP = 10

bot = InternetSpeedTwitterBot("https://x.com/leaptel")
bot.get_internet_speed()


if PROMISED_UP > bot.up or PROMISED_DOWN > bot.down:
    message = f"Hey Internet Provider, why is my internet speed {bot.down}down/{bot.up}up when I pay for 1000down/1000up?"
    bot.tweet_at_provider(ACCOUNT_EMAIL=ACCOUNT_EMAIL, ACCOUNT_PASSWORD=ACCOUNT_PASSWORD, PROMISED_UP=PROMISED_UP, PROMISED_DOWN=PROMISED_DOWN)

bot.close()
