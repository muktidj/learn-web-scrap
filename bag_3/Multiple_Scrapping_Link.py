from bs4 import BeautifulSoup
import requests

#####################################################
# Extracting links from pagination bar
#####################################################

# How To Get The HTML

ROOT = 'https://subslikescript.com'  # this is the homepage of the website
WEBSITE = f'{ROOT}/movies_letter-W'  # concatenating the homepage with the movies "letter-X" section. You can choose any section (e.g., letter-A, letter-B, ...)
RESULT = requests.get(WEBSITE)
CONTENT = RESULT.text
SOUP = BeautifulSoup(CONTENT, 'lxml')


PAGINATION =SOUP.find('ul', class_='pagination')
PAGES = PAGINATION.find_all('li', class_='page-item') #type: ignore
LAST_PAGE = PAGES[-2].text # this is the number of pages that the website has inside the movies "letter X" section

folder_path = '/Users/user/Learn/python/webscraping/udemy/bag_3/result_scrapping_pagination/'



for PAGE in range(1, int(LAST_PAGE)+1)[:2]:
    RESULT = requests.get(f'{WEBSITE}?page={PAGE}')  # structure --> https://subslikescript.com/movies_letter-X?page=2
    CONTENT = RESULT.text
    SOUP = BeautifulSoup(CONTENT, 'lxml')

    # Locate the box that contains a list of movies
    BOX = SOUP.find('article', class_='main-article')

    # Store each link in "links" list (href doesn't consider root aka "homepage", so we have to concatenate it later)
    links = []
    for link in BOX.find_all('a', href=True):  # find_all returns a list # type: ignore
        links.append(link['href'])

    #################################################
    # Extracting the movie transcript
    #################################################



    for link in links:
        try:  # "try the code below. if something goes wrong, go to the "except" block"
            RESULT = requests.get(f'{ROOT}/{link}')  # structure --> https://subslikescript.com/movie/X-Men_2-290334
            CONTENT = RESULT.text
            SOUP = BeautifulSoup(CONTENT, 'lxml')

            # Locate the box that contains title and transcript
            BOX =SOUP.find('article', class_='main-article')
            # Locate title and transcript
            TITLE = BOX.find('h1').get_text() #type: ignore
            TRANSCRIPT = BOX.find('div', class_='full-script').get_text(strip=True, separator=' ') #type: ignore

            # Exporting data in a text file with the "title" name
            with open(f'{folder_path}/{TITLE}.txt', 'w') as file:
                file.write(TRANSCRIPT)
        except:
            print('------ Link not working -------')
            print(link)
