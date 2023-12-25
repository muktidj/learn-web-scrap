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
date = []
home_team = []
score = []
away_team = []

for match in matches[:data]:
     date.append(match.find_element(By.XPATH, "./td[1]").text) #//tr/td[1] 
     home_team.append(match.find_element(By.XPATH, "./td[2]").text) #//tr/td[2] 
     # match.find_element(By.XPATH, "./td[3]") #//tr/td[3] 
     # match.find_element(By.XPATH, "./td[4]") #//tr/td[4]

print(date)
print(home_team)

sleep(10000)

driver.quit()





