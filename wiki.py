import random
from urllib.request import urlopen
from urllib.error import HTTPError

import re

import datetime
from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())
def getLinks(url):
    links = []
    try:
        html = urlopen("http://en.wikipedia.org" +url)
    except HTTPError as e:
        return "HTTP ERROR"

    try:
        obj = BeautifulSoup(html, "html.parser")
        for link in  obj.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")):
            if 'href' in link.attrs:
                links.append(link.attrs['href'])
    except AttributeError as e:
        return "ATTRIBUTE ERROR"

    return links


links = getLinks("/wiki/Kenya")
if links == "HTTP ERROR":
    print("Url could not be opened")
elif links == "ATTRIBUTE ERROR":
    print("Attribute could not be found")
else:
    # for link in links:
    #     print("Main Link: "+  link)
    #     for item in getLinks(link):
    #         print(item)
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)]
        print(newArticle)
        links = getLinks(newArticle)