from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://www.adamchoi.co.uk/overs/detailed")



 # Find the element using Selenium 4's find_element method
element = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']") #type: ignore

# Perform actions on the found element (e.g., click, get text, etc.)
element.click()  # Example: Click the element


dropdwon_element = Select(driver.find_element(by='id', value='country'))

dropdwon_element.select_by_visible_text('Italy')
sleep(3)



matches = driver.find_elements(By.TAG_NAME, "tr")


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
df.to_csv("football_italy_data_csv.csv", index=False)


print(df)


driver.quit()





