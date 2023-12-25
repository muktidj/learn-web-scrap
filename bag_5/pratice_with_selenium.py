from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://www.adamchoi.co.uk/overs/detailed")



 # Find the element using Selenium 4's find_element method
element = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']") #type: ignore

# Perform actions on the found element (e.g., click, get text, etc.)
element.click()  # Example: Click the element

matches = driver.find_elements(By.TAG_NAME, "tr")

# data = 50
date = []
home_team = []
score = []
away_team = []

for match in matches:
     match_date= match.find_element(By.XPATH, "./td[1]").text #//tr/td[1] 
     if "2023" in match_date:
          date.append(match_date)
          home_team.append(match.find_element(By.XPATH, "./td[2]").text) #//tr/td[2] 
          score.append(match.find_element(By.XPATH, "./td[3]").text) #//tr/td[3] 
          away_team.append(match.find_element(By.XPATH, "./td[4]").text) #//tr/td[4]
   

df = pd.DataFrame({"date": date, "home_team": home_team, "score": score, "away_team": away_team})
df.to_csv("football_data_csv", index=False)

print(df)
sleep(10000)

driver.quit()





