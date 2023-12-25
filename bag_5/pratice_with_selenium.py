from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.adamchoi.co.uk/overs/detailed")



sleep(100)

driver.quit()





