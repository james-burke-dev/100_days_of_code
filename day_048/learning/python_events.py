from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

event_time_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_link_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events_times = [time.text for time in event_time_elements]
events_links = [link.text for link in event_link_elements]
events_dict = {}

for idx, link in enumerate(events_links):
    try:
        events_dict[idx] = {"time": events_times[idx], 
                            "name": events_links[idx]}
    except IndexError:
        print(f"Indec Error for {idx}")

print(events_dict)

driver.quit()
