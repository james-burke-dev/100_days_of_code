import smtplib
import requests
import datetime as dt

GMAIL_SMTP_SERVER = "smtp.gmail.com"
EMAIL_ADDRESS = "test@test.com"
PASSWORD = "not_a_real_PASSWORD"

SPACE_STATION_URL = "http://api.open-notify.org/iss-now.json"
SUNRISE_URL = "https://api.sunrise-sunset.org/json"

SYD_LAT = "33.8688"
SYD_LNG = "151.2093"

SYD_POS = (float(SYD_LAT), float(SYD_LNG))

sun_params = {
    "lat": SYD_LAT, 
    "lng": SYD_LNG, 
    "formatted": 0,
    "tzid": "Australia/Sydney"
}

def send_email():
    with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=PASSWORD)


        message = f"Subject: Space Station Alert \n\nLook up! \n\nThe ISS is above you \n\nNASA"

        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS,
                           msg=message)
        connection.close()
        print(message)

def check_location():
    response = requests.get(url=SPACE_STATION_URL)
    response.raise_for_status()

    iss_pos = (float(response.json()["iss_position"]["longitude"]), (response.json()["iss_position"]["latitude"]))

    if (SYD_POS[0] - 5 < iss_pos[0] < SYD_POS[0]):
        if (SYD_POS[1] - 5 < iss_pos[1] < SYD_POS[1] + 5):
            return True
    print(f"ISS Not Overhead - current position: {iss_pos[0], iss_pos[1]}")
    return False

def is_night():
    now = dt.datetime.now()

    response = requests.get(url=SUNRISE_URL, params=sun_params)

    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    if sunset < now.hour:
        return True
    else:
        print(f"Current hour - {now.hour}")
        print(f"Sunset - {sunset}")
        print(f"Sunrise - {sunrise}")
        return False

if is_night() and check_location():
    send_email()
