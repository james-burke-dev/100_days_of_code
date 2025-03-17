import requests
import smtplib

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM", 
    "outputsize": "compact",
    "apikey": API_KEY
}

def get_stock_data(sym):
    params["symbol"] = sym
    try:
        response = requests.get(url=API_URL, params=params)
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

def send_email():
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)

        message = f"Subject: It will rain today \n\nBring an umbrella! \n\nFrom Your Weatherman"

        connection.sendmail(from_addr=email_address, to_addrs=email_address,
                           msg=message)
        connection.close()

stock_data = get_stock_data("IBM")
stock_data_list = [value for (key, value) in stock_data.items()]

yesterdays_stock_close = float(stock_data_list[0]["4. close"])
day_before_yesterday_stock_close = float(stock_data_list[1]["4. close"])

perc_diff = find_perc_difference(yesterdays_stock_close, day_before_yesterday_stock_close)

if perc_diff > 5:
    print("Get News ")

print(day_before_yesterday_stock_close, " ", yesterdays_stock_close)
