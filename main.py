from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"https://www.amazon.in/realme-Wireless-Earbuds-Spatial-Charging/dp/B0CH1HLLBV/ref=sr_1_6?crid=19FO8G8JCG9"
           f"GN&dib=eyJ2IjoiMSJ9.PwcF3zCz9ocNnJVYYP3v0qpPaaGjTn5iiK1kaRFXnxW8m0yc6J5WhxW09t3ihVrw246HQX8jxgCjVLWVYJFc"
           f"BH7WboX8ZV8V2K9bg4HGQP4Uw-Td7GsDifFuDbzdw3Pa5dWcZ7WaoEgzBSX8HMisDFXwX0zehhPaW4LsCkRE7IyLZC0RproI_WG8yi4N"
           f"ryOcQpLOEUPBhO98VrjZq9uBc1x7LA6FT-pzHCWzbR_ev80.x_NUeUzjtRjvQO1XWSGWFmsOF7jMX782mgmVyXmZDgk&dib_tag=se&k"
           f"eywords=earbuds+realme&nsdOptOutParam=true&qid=1725971679&sprefix=earbuds+realm%2Caps%2C230&sr=8-6")

price_rupees = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
print(f"the price is {price_rupees}")

driver.quit()