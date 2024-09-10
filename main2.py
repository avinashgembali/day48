from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
dictionary = {}
for i in range(len(events)):
    dictionary[i] = {
        "time": dates[i].text,
        "event": events[i].text
    }

print(dictionary)
driver.quit()