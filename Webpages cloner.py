import os
from bs4 import BeautifulSoup, SoupStrainer
import requests
import sand as sd

links = sd.links

path = 'D:\\Resize\\Martial Peak\\'

def getdata(url):
    r = requests.get(url)
    return r.text
i = 1
total = len(links)
for link in links:
    url = link

  
    htmldata = getdata(link)
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    for data in soup.find_all("h1"):
        l = data.get_text()
        k = l[:-1]
        filename = k + ".html"
        try:
            with open(os.path.join(path, filename), 'w', encoding="utf-8") as fp:
                fp.write(str(soup))
                fp.close()
            print(str(i) + " out of " + str(total) + " Name: " + str(l))
            i+=1
        except:
            print("error with")
#     for da in soup.find_all("p"):
#         l = da.get_text()
#         file = open('./ein.txt', 'a', encoding="utf-8")
#         file.write(l)
#         file.write("\n")
#         file.close()
#         print(str(i) + " out of " + str(total))
#         i+=1


# filename = ' '
# with open(os.path.join(path, filename), 'w') as fp:
#     pass