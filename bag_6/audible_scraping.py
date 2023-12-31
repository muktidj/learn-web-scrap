from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://www.audible.com/search")


BOX_ELEMENT = driver.find_element(By.CLASS_NAME, "adbl-impression-container")
LI_ELEMENT = BOX_ELEMENT.find_elements(By.XPATH, ".//li[contains(@class, 'productListItem')]")


data = 5
book_title = []
book_author = []
book_length = []


for product in LI_ELEMENT[:data]:
     book_title.append(product.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]").text) # type: ignore
     book_author.append(product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]").text) # type: ignore
     book_length.append(product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text) # type: ignore
     


df = pd.DataFrame({"Book Title": book_title, "Book Author": book_author, "Duration": book_length})
df.to_csv("book_csv.csv", index=False)
     


print(df)

sleep(1000)
driver.quit()