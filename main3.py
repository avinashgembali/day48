from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
# articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text
# articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # clicks on that article count
# articles.click()

# finding element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search_symbol = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
search_symbol.click()

search = driver.find_element(By.NAME, value="search")
# sending input
search.send_keys("Allu Arjun")

search.send_keys(Keys.ENTER)


