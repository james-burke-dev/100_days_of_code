from selenium import webdriver
from selenium.webdriver.common.by import By
#firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_experimental_option("detach", True)

driver = webdriver.Firefox()
driver.get("https://www.amazon.com.au/PASYOU-Adjustable-Weight-Bench-Foldable/dp/B07S7NRZL4")

price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"Price: ${price_whole}.{price_fraction}")

driver.quit()
