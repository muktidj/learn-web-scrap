from bs4 import BeautifulSoup
import requests

ROOT = "https://subslikescript.com"
TARGET_URL = f"{ROOT}/movies"
HEADERS = {
     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
RESPONSE = requests.get(TARGET_URL)
CONTENT = RESPONSE.text

SOUP = BeautifulSoup(CONTENT, "lxml")


# Bisa menggunakan cara seperti ini untuk html bersarang 
box = SOUP.find("article", class_ ="main-article")

links = []
for link in box.find_all("a", href=True):  # type: ignore
     links.append(link["href"]) 

print(links)

for link in links:
     TARGET_URL = f"{ROOT}/{link}"
     RESPONSE = requests.get(TARGET_URL)
     CONTENT = RESPONSE.text
     SOUP = BeautifulSoup(CONTENT, "lxml")
     BOX = SOUP.find("article", class_ ="main-article")
     TITLE = BOX.find("h1").get_text() #type: ignore
     TRANSCRIPT = BOX.find("div", class_ = "full-script").get_text(strip=True, separator=' ') #type: ignore
     with open(f"{TITLE}.txt", "w") as file:
          file.write(TRANSCRIPT)



