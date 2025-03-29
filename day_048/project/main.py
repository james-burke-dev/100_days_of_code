from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

COOKIE_URL = "http://orteil.dashnet.org/experiments/cookie/"

COOKIE_X_PATH= '//*[@id="cookie"]'

STORE_X_PATH = '//*[@id="store"]'

SCORE_X_PATH = '//*[@id="money"]'

driver = webdriver.Firefox()
driver.get(COOKIE_URL)

cookie_btn = driver.find_element(By.XPATH, COOKIE_X_PATH)

store = driver.find_element(By.XPATH, STORE_X_PATH)

score = driver.find_element(By.XPATH, SCORE_X_PATH)

store_elems = driver.find_elements(By.CSS_SELECTOR, "#store div b")
costs_dict = {}

def check_store():
    store_elems = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    for elem in store_elems:
        try:
            item_name = elem.text.split("-")[0].strip()
            item_cost = int(elem.text.split("-")[1].replace(",","").strip())
        except IndexError:
            pass
        else:
            costs_dict[item_name] = item_cost
    return costs_dict

idx = 0
while True:
    cookie_btn.click()
    current_score = int(score.text)
    if(idx % 5 == 0):
        costs_dict = check_store()
    
    for item in costs_dict.items():
        if current_score > item[1]:
            print(f"buy{item[0]}")
            driver.find_element(by=By.ID, value=f"buy{item[0]}").click()
    idx += 1


#driver.find_element(By.CLASS_NAME, "button").click()
#driver.find_element(By.CLASS_NAME, "search").send_keys("Find me", Keys.ENTER)
#river.find_element(By.CLASS_NAME, "form").send_keys("Hello")

driver.quit()
