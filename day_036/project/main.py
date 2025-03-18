import requests
import smtplib
import os

SYMBOL = "IBM"
COMPANY_NAME = "IBM"

API_KEY = os.environ.get("STOCK_API_KEY")

API_URL = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_URL = 'https://newsapi.org/v2/everything'

SMTP_SERVER = os.environ.get("SMTP_SVR_ADD")
email_address = os.environ.get("EMAIL_ADD")
password = os.environ.get("EMAIL_PASSWORD")

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM", 
    "outputsize": "compact",
    "apikey": API_KEY
}

news_api_params = {
    'q': '',
    'from': '2025-03-17',
    'sortBy': 'popularity',
    'language': 'en',
    'apiKey': NEWS_API_KEY
}

def get_stock_data(sym):
    stock_api_params["symbol"] = sym
    try:
        response = requests.get(url=API_URL, params=stock_api_params)
        response.raise_for_status
    except:
        print("Exception when querying stock API")
        exit()
    else:      
        data = response.json()["Time Series (Daily)"]
        return data

def find_perc_difference(num1, num2):
    diff = abs(num1 - num2)
    perc_diff = (diff / num1) * 100
    return perc_diff

def get_news(sym):
    news_api_params["q"] = sym
    try:
        response = requests.get(url=NEWS_API_URL, params=news_api_params)
        response.raise_for_status
    except:
        print("Exception when querying news API")
        exit()
    else:      
        data = response.json()
        articles = data["articles"]

        first_three_articles = articles[0:3]

        article_content = [f"Headline: {article["title"]}. \n Brief: {article["description"]}" for article in first_three_articles]

        send_email(article_content)

def send_email(message):
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)
        connection.sendmail(from_addr=email_address, to_addrs=email_address,
                           msg=message)
        connection.close()

stock_data = get_stock_data(SYMBOL)
stock_data_list = [value for (key, value) in stock_data.items()]

yesterdays_stock_close = float(stock_data_list[0]["4. close"])
day_before_yesterday_stock_close = float(stock_data_list[1]["4. close"])

perc_diff = find_perc_difference(yesterdays_stock_close, day_before_yesterday_stock_close)

if perc_diff > 5:
    get_news(COMPANY_NAME)
else:
    print("Stock has not changed by 5%")
