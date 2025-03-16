import requests
import smtplib
import os

LAT = os.environ.get("LAT")
LNG = os.environ.get("LNG")
WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")

SMTP_SERVER = os.environ.get("SMTP_SVR_ADD")
email_address = os.environ.get("EMAIL_ADD")
password = os.environ.get("EMAIL_PASSWORD")

params = {
    "appid": API_KEY,
    "lat": LAT,
    "lon": LNG,
    "cnt": 4
}

def get_weather():
    response = requests.get(url=WEATHER_URL, params=params)
    response.raise_for_status()

    weather = response.json()

    return weather

def check_for_percipitation(weather):
    for forecast in weather["list"]:
        if int(forecast["weather"][0]["id"]) < 700:
            return True
    return False

def send_email():
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)

        message = f"Subject: It will rain today \n\nBring an umbrella! \n\nFrom Your Weatherman"

        connection.sendmail(from_addr=email_address, to_addrs=email_address,
                           msg=message)
        connection.close()

weather = get_weather()

will_rain = check_for_percipitation(weather)

if will_rain:
    send_email()
