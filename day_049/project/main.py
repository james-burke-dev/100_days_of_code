from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os

ACCOUNT_EMAIL = os.environ.get("EMAIL_ADDRESS")
ACCOUNT_PASSWORD = os.environ.get("PASSWORD")
PHONE = os.environ.get("PONE_NUM")


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

def click_btn_css(element):
    time.sleep(2)
    button = driver.find_element(by=By.CSS_SELECTOR, value=element)
    button.click()

def click_btn_link_text(text):
    time.sleep(2)
    sign_in_button = driver.find_element(by=By.LINK_TEXT, value=text)
    sign_in_button.click()

def sign_in():
    time.sleep(5)
    email_field = driver.find_element(by=By.ID, value="username")
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field = driver.find_element(by=By.ID, value="password")
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Reject cookies
click_btn_css('button[action-type="DENY"]')

# Go to Sign-in 
click_btn_link_text("Sign in")

# Sign in
sign_in()

# CAPTCHA - Solve Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        click_btn_css(".jobs-s-apply button")

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
