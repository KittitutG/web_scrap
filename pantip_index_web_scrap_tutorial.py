from bs4 import BeautifulSoup
import requests
import pandas




'''
Beautifulsoup has a big limitation
they can only extract data from static
which mean. any web that return data from JS. 
BS4 can not extract them
'''

URL = 'https://pantip.com/topic/42777418'


webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "html.parser")

links = soup.find_all("h2",{"class":"display-post-title"})


content = links[0].text
print(content)