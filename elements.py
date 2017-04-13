from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def findCharacters(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        obj = BeautifulSoup(html, "html.parser")
        characters = obj.findAll("span", {"class":"green"})
    except AttributeError as e:
        return None

    return characters



characters = findCharacters("http://www.pythonscraping.com/pages/warandpeace.html")
if characters == None:
    print("The page is not found or not well formatted")
else:
    for name in characters:
        print(name.get_text())