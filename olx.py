from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getProducts(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return "HTTP Error"

    try:
        obj = BeautifulSoup(html, "html.parser")
        products = obj.findAll("meta", {"property":"og:title"})
    except AttributeError as e:
        return "Attribute Error"

    return products


products = getProducts("https://www.olx.co.ke/")
if products == "HTTP Error":
    print("Server could not be reached")

elif products == "Attribute Error":
    print("Attribute could not be found")

else:
    for product in products:
        print(product["content"])