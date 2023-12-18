from bs4 import BeautifulSoup
import requests


TARGET_URL = "https://subslikescript.com/movie/SOS_Titanic-79836"
HEADERS = {
     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
RESPONSE = requests.get(TARGET_URL)
CONTENT = RESPONSE.text

SOUP = BeautifulSoup(CONTENT, "lxml")


# Bisa menggunakan cara seperti ini untuk html bersarang 
box = SOUP.find("article", class_ ="main-article")

title = box.find("h1").get_text() #type: ignore

transcript = box.find("div", class_ = "full-script").get_text(strip=True, separator=' ') #type: ignore
print(title) # type: ignore
print("================")

print(transcript) # type: ignore

with open(f"{title}.txt", "w") as file:
     file.write(transcript)


