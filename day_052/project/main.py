
from insta_follower import InstaFollower
import os 

ACCOUNT_EMAIL = os.environ.get("EMAIL_ADDRESS")
ACCOUNT_PASSWORD = os.environ.get("PASSWORD")

bot = InstaFollower()
bot.login(username=ACCOUNT_EMAIL, password=ACCOUNT_PASSWORD)
bot.find_followers()
bot.follow()