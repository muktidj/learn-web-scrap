from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.adamchoi.co.uk/overs/detailed")



 # Find the element using Selenium 4's find_element method
element = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']") #type: ignore

# Perform actions on the found element (e.g., click, get text, etc.)
element.click()  # Example: Click the element

matches = driver.find_elements(By.TAG_NAME, "tr")
data = 50
for match in matches[:data]:
     print(match.text)


sleep(10000)

driver.quit()





