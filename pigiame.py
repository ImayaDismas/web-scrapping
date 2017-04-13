from bs4 import  BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError


def getDescription(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return "HTTP ERROR"

    try:
        obj = BeautifulSoup(html, "html.parser")
        name = obj.findAll("h1",{"class":"brkword lheight28"})
        for i in name:
            pname = i
        location = obj.findAll("strong", {"class":"c2b small"})
        for loc in location:
            ploaction = loc
        price = obj.findAll("strong", {"class":"xxxx-large margintop7 block not-arranged"})
        for piz in price:
            pprice = piz
        poster = obj.findAll("span", {"class":"block color-5 brkword xx-large"})
        for post in poster:
            pposter = post

    except AttributeError as e:
        return "ATTRIBUTE ERROR"
    description = str(pname) +"\n" + str(ploaction) + "\n" + str(pprice) + "\n" + str(pposter)
    return description

description = getDescription("https://www.olx.co.ke/ad/simply-the-best-hp-probook-4540s-corei5-4gb-1tb-2-8cpu-webcam-wifi-dvd-ID15QO8n.html")
if description == "HTTP ERROR":
    print("Could not open the url")
elif description == "ATTRIBUTE ERROR":
    print("Could not get the attribube specified")
else:
    print(description)