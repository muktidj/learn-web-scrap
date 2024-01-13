from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd

options = Options()
options.window_size = (1280, 800) # type: ignore
# options.headless = True # type: ignore
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
# driver.get("https://www.audible.com/search")

driver.get("https://www.audible.com/adblbestsellers?ref_pageloadid=ZJVpTik6SSSNpgaZ&ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=d42ea6af-6ce9-44e1-bbd5-7e2e15acab17&pf_rd_r=ACXD7SWWG2W10QGGZ7SW&pageLoadId=I11bL9EZNDXY3fUN&creativeId=7ba42fdf-1145-4990-b754-d2de428ba482")

# Pagination Handle
pagination = driver.find_element(By.XPATH, "//ul[contains(@class, 'pagingElements')]")
pages = pagination.find_elements(By.XPATH, ".//li[contains(@class, 'bc-list-item')]")
last_page = int(pages[-2].text)


current_page = 1


book_title = []
book_author = []
book_length = []

while current_page <= last_page:
     sleep(2)
     BOX_ELEMENT = driver.find_element(By.CLASS_NAME, "adbl-impression-container")  # type: ignore
     LI_ELEMENT = BOX_ELEMENT.find_elements(By.XPATH, ".//li[contains(@class, 'productListItem')]")  # type: ignore
     
     for product in LI_ELEMENT:
          book_title.append(product.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]").text) # type: ignore
          book_author.append(product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]").text) # type: ignore
          book_length.append(product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text) # type: ignore

     current_page +=1

     try:
          next_page = driver.find_element(By.XPATH, "//span[contains(@class, 'nextButton')]")
          next_page.click()
     except:
          pass
     


df = pd.DataFrame({"Book Title": book_title, "Book Author": book_author, "Duration": book_length})
df.to_csv("book_best-seller_csv.csv", index=False)
     


print(df)

driver.quit()