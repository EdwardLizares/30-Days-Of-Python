import requests
import json
from bs4 import BeautifulSoup

def boston_scrape():
    url = 'http://www.bu.edu/president/boston-university-facts-stats/'
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.title)
    #print(soup.title.get_text)
    #print(soup.body)

    links = [link.get('href') for link in soup.find_all("a")]
    with open("22_Day_Web_scraping/Exercises/links.json", "w", encoding='utf-8') as f:
        json.dump(links, f, indent=4) # indent splits off what would be a long single string
    return links

def uci_scrape():
    pass # skip, ive done this with ucimlrepo before

def wikipedia_scrape():
    url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
    }
    response = requests.get(url, headers=headers, timeout=20)
    soup = BeautifulSoup(response.content, 'html.parser')
    # navigation 
    print(response.status_code)
    president_table = soup.find("table", id="mwgQ")
    presidents = president_table.find_all("span", class_="fn")
    president_names = [p.find("a").get_text() for p in presidents]
    with open("22_Day_Web_scraping/Exercises/presidents.json", "w", encoding='utf-8') as f:
        json.dump(president_names, f, indent=4) # indent splits off what would be a long single string
    return president_names

if __name__ == "__main__":
    #print("1:", boston_scrape())
    print("3:", wikipedia_scrape())