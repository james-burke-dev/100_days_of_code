from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def click_btn_x_path(self, path):
        time.sleep(2)
        button = self.driver.find_element(by=By.XPATH, value=path)
        if button:
            button.click()

    def login(self, username, password):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(username)
        password.send_keys(password)

        time.sleep(5)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        # If login not now is prompted - close it 
        self.click_btn_x_path(path="//div[contains(text(), 'Not now')]")

        time.sleep(5)
        # If notification is prompted - close it 
        self.click_btn_x_path(path="//button[contains(text(), 'Not Now')]")

    def find_followers(self):
        time.sleep(5)
        # Will bring up the followers of an account
        self.driver.get(f"https://www.instagram.com/chef/followers")

        time.sleep(8.2)
        # The xpath of the modal will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
