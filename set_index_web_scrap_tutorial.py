from bs4 import BeautifulSoup
import requests
import pandas


URL = 'https://www.ddproperty.com/property/project/chamonix-sriracha-laem-chabang-%E0%B8%8A%E0%B8%B2%E0%B9%82%E0%B8%A1%E0%B8%99%E0%B8%B4%E0%B8%81%E0%B8%8B%E0%B9%8C-%E0%B8%A8%E0%B8%A3%E0%B8%B5%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%B2-%E0%B9%81%E0%B8%AB%E0%B8%A5%E0%B8%A1%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%87-%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5-%E0%B8%82%E0%B8%B2%E0%B8%A2-11050100#810'
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'

HEADERS = ({'User-Agent':UserAgent,
            'Accept-Language':'en-Us, en;q=0.5'})

webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "html.parser")

links = soup.find_all("h2",{"class":"amount"})

print(links)


# relative_url = links[0].get('href')
# print(relative_url)
# new_link = 'https://www.amazon.com' + relative_url
# print(new_link)

# new_webpage = requests.get(new_link, headers= HEADERS)

# new_soup = BeautifulSoup(new_webpage.content, "html.parser")
# print(new_soup)