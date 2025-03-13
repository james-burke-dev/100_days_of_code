import smtplib
import datetime as dt
import random

GMAIL_SMTP_SERVER = "smtp.gmail.com"
email_address = "test@test.com"
password = "not_a_real_password"

try:
    with open("day_032/learning/quotes.txt", "r") as fn:
        quotes = fn.readlines()
except FileNotFoundError:
    print("Quotes file not found... ")
    print("Exiting")
    exit()
else:
    now = dt.datetime.now()

    if now.weekday() == 0:
        with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=email_address, password=password)
            connection.sendmail(from_addr=email_address, to_addrs="insert@email.com",
                                msg=f"Subject: Monday's Quote \n\n{random.choice(quotes)}")
            connection.close()
    else:
        exit()
