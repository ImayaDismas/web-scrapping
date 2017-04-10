from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib3.exceptions import HTTPError

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
#return null, break, or do some other "Plan B"
else:
    #program continues. Note: If you return or break in the
    #exception catch, you do not need to use the "else" statement
    if html is None:
        print("URL is not found")
    else:
        #program continues
        bsObj = BeautifulSoup(html.read(), "lxml")
        # print(bsObj.find("nonExistent").someTag)
        # print(bsObj.html.body.h1)

        try:
            badContent = bsObj.find("nonExisting")
        except AttributeError as e:
            print("Tag was not found")
        else:
            if badContent == None:
                print ("Tag was not found")
            else:
                print(badContent)
