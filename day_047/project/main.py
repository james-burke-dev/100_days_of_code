import requests
from bs4 import BeautifulSoup
import os
import smtplib

PRODUCT_URL = "https://appbrewery.github.io/instant_pot/"
#PRODUCT_URL = "https://www.amazon.com.au/PASYOU-Adjustable-Weight-Bench-Foldable/dp/B07S7NRZL4"
TARGET_PRICE = 100 
GMAIL_SMTP_SERVER = "smtp.gmail.com"
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
PASSWORD = os.environ.get("EMAIL_PASSWORD")

def get_page_html():
    try:
        response = requests.get(url=PRODUCT_URL, headers={"Accept-Language":"en-US"})
    except:
        print("Could not get product HTML")
    else:
        product_webpage = response.text
        soup = BeautifulSoup(product_webpage, 'html.parser')
        return soup

def get_price(page_html):
    price_whole = page_html.find(class_="a-price-whole").getText()
    price_fraction = page_html.find(class_="a-price-fraction").getText()

    price = float(f"{price_whole}{price_fraction}")

    return price

def send_email():
    with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=PASSWORD)


        message = f"Amazon Price Alert \n\nYour product is below {TARGET_PRICE} \n\nClick the link: {PRODUCT_URL} \n"

        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS,
                           msg=message)
        connection.close()
        print(message)

page_html = get_page_html()

price = get_price(page_html)

if price < TARGET_PRICE:
    print(f"Price below {TARGET_PRICE}")
    print(f"Sending email to {EMAIL_ADDRESS}")
    send_email()
else:
    print(f"No luck today. Price: {price}")
    print(f"Price above {TARGET_PRICE}")
