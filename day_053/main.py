import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

def get_page_html(URL):
    '''Accepts a webpage URL
    Returns a BeautifulSoup object'''
    try:
        response = requests.get(url=URL, headers={"Accept-Language":"en-US"})
    except:
        print("Could not get product HTML")
    else:
        product_webpage = response.text
        soup = BeautifulSoup(product_webpage, 'html.parser')
        return soup

soup = get_page_html(ZILLOW_URL)

# Find all HTML elements containing rent prices
price_elems = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices = []
for elem in price_elems:
    prices.append(re.sub('[$,/a-z]+', '', elem.getText().split("+")[0]))

# Find all HTML elements containing hrefs for Properties
anchor_elems = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
links = []
for elem in anchor_elems:
    links.append(elem.get("href"))

# Find all HTML elements containing adress info for Properties
address_elems = soup.find_all("address")
addresses = []
for elem in address_elems:
    address = elem.getText().strip()
    address = address.replace("\n", "")
    addresses.append(address)

# Create a dataframe from all three lists 
data_df = pd.DataFrame({
    'url': links,
    'address': addresses,
    'rent': prices
})

try:
    data_df.to_csv('zillow_data.csv', sep='\t', encoding='utf-8', index=False, header=True)
except FileNotFoundError:
    print("file not found - please create zillow_data.csv and rerun this script")
