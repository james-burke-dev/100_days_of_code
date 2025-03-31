from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os

ACCOUNT_EMAIL = os.environ.get("EMAIL_ADDRESS")
ACCOUNT_PASSWORD = os.environ.get("PASSWORD")


def click_btn_css(element):
    time.sleep(2)
    button = driver.find_element(by=By.CSS_SELECTOR, value=element)
    button.click()

def click_btn_x_path(path):
    time.sleep(2)
    button = driver.find_element(by=By.XPATH, value=path)
    button.click()

def sign_in():
    email = driver.find_element(By.XPATH, value='//*[@id="email"]')
    password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
    email.send_keys(ACCOUNT_EMAIL)
    password.send_keys(ACCOUNT_PASSWORD)
    password.send_keys(Keys.ENTER)

driver = webdriver.Firefox()
driver.get("http://www.tinder.com")

click_btn_x_path('//*[text()="Log in"]')

click_btn_x_path('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')

time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sign_in()

driver.switch_to.window(base_window)

time.sleep(5)
click_btn_x_path('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
click_btn_x_path('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
click_btn_x_path('//*[@id="content"]/div/div[2]/div/div/div[1]/button')

# Loop through 100 profiles 
for n in range(100):

    time.sleep(3)

    try:
        #Click the like button 
        click_btn_x_path('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

    #Close Matched pop-up in
    except ElementClickInterceptedException:
        try:
            click_btn_css(".itsAMatch a")
        # Wait for like button to appear and retry 
        except NoSuchElementException:
            time.sleep(2)

driver.quit()