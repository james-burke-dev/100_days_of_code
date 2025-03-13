import smtplib
import datetime as dt
import pandas as pd
import random

GMAIL_SMTP_SERVER = "smtp.gmail.com"
email_address = "test@test.com"
password = "not_a_real_password"


def send_email(person):
    with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)

        try:
            letter_num = random.randint(1,3)
            with open(f"day_032/project/letter_templates/letter_{letter_num}.txt") as fn:
                message = fn.read()
                message = message.replace("[NAME]", f"{person["name"]}")

        except FileNotFoundError:
            print("Message template not found... ")
            print("Using default message... ")
            message = f"Subject: Happy Birthday! \n\nTo {person["name"]}, \n\nHappy Birthday! \n\nFrom My Name"

        connection.sendmail(from_addr=email_address, to_addrs=person["name"],
                           msg=message)
        connection.close()
        print(message)

def check_birthday(now, birthday):
    if (now.month == birthday.month) and (now.day == birthday.day):
        return True
    return False

try:
    birthday_df = pd.read_csv("day_032/project/birthday_data.csv")
    birthday_list = birthday_df.to_dict(orient="records")
except FileNotFoundError:
    print("Birthday.csv not found... ")
    print("Exiting")
    exit()
else:
    now = dt.datetime.now()

    for person in birthday_list:
        birthday = dt.datetime(year=person["year"], month=person["month"], day=person["day"])
        is_birthday = check_birthday(now, birthday)
        
        if is_birthday:
            print(f"Sending email to {person["name"]}")
            send_email(person)
        else:
            print(f"Not {person["name"]}'s birthday")
