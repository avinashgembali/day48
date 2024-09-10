from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
name = driver.find_element(By.NAME, value="fName")
name.send_keys("avi")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("g")
email = driver.find_element(By.NAME, value="email")
email.send_keys("a@gmail.com")
button = driver.find_element(By.CLASS_NAME, value="btn-block")
button.click()

