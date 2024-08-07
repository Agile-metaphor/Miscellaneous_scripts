# from bs4 import BeautifulSoup, SoupStrainer
# import requests
# import sand as sd

# links = sd.links
# url = "https://www.divinedaolibrary.com/martial-peak/"

# page = requests.get(url)    
# data = page.text
# soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
#     print(link.get('href'))

#links = []

#print(links)
# def getdata(url):
#     r = requests.get(url)
#     return r.text
# total = len(links)
# for link in links:
#     url = link

  
#     htmldata = getdata(link)
#     soup = BeautifulSoup(htmldata, 'html.parser')
#     data = ''
#     for data in soup.find_all("h1"):
#         l = data.get_text()
#         file = open('./ein.txt', 'a', encoding="utf-8")
#         file.write(l)
#         file.write("\n" + "\n"+ "\n"+ "\n"+ "\n"+ "\n"+ "\n")
#         file.close()
#         #print(str(i) + " out of " + str(total))
#         #i+=1
#     for da in soup.find_all("p"):
#         l = da.get_text()
#         file = open('./ein.txt', 'a', encoding="utf-8")
#         file.write(l)
#         file.write("\n")
#         file.close()
#         print(str(i) + " out of " + str(total))
#         i+=1


i = 1
k=1
l=111
import requests
from bs4 import BeautifulSoup
while(k <= l):
    # specify the URL of the webpage to scrape
    url = "https://www.volarenovels.com/novel/cultivation-chat-group/ccg-chapter-" + str(k) + "/"
    filename = "Cultivation-Group-chat-" + str(k) + ".html"
    # # make a GET request to the webpage and store the response
    # response = requests.get(url)

    # # create a BeautifulSoup object to parse the HTML content
    # soup = BeautifulSoup(response.content, 'html.parser')

    # # find the div with class="entry-content" and get all the <p> tags within it
    # entry_content_div = soup.find('div', class_='entry-content')
    # p_tags = entry_content_div.find_all('p')

    # # create a file to save the extracted text
    # with open(filename, 'w', encoding="utf-8") as file:
    #     # iterate over the <p> tags and write their text content to the file
    #     for p in p_tags:
    #         file.write(p.text + '\n')

    # print(f'The extracted text has been saved to {filename}.')

    # make a GET request to the webpage and store the response
    response = requests.get(url)

    # create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # create an HTML file to save the cloned webpage
    # filename = 'cloned_page.html'
    with open(filename, 'w', encoding='utf-8') as file:
        # write the HTML content to the file
        file.write(str(soup))

    print(f'The webpage at {url} has been cloned to {filename}.')
    k+=1

