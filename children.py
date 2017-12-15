from urllib.request import urlopen

from bs4 import BeautifulSoup


def getChildren(url):
    try:
        html = urlopen(url)
    except:
        return  None
    else:
        try:
            bsObj = BeautifulSoup(html.read(), "html.parser")
        except:
            return None
        else:
            return bsObj.find("table",{"id":"giftList"}).children


url = "http://www.pythonscraping.com/pages/page3.html"

children = getChildren(url)
for child in children:
    print(child)