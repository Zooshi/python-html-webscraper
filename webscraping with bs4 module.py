from urllib.request import urlopen
from bs4 import BeautifulSoup

url = r"http://www-public.webscraper.io/test-sites/e-commerce/allinone/phones/touch"

req = urlopen(url).read()
soup = BeautifulSoup(req,'html.parser')
caption = soup.find('div', {'class':'caption'})
length = len(soup.find_all('h4', {'class':'pull-right price'}))
for i in range(length):
    price = soup.find_all('h4', {'class':'pull-right price'})[i].text
    title = soup.find_all('a', {'class':'title'})[i].text
    description = soup.find_all('p', {'class':'description'})[i].text
    print(price+" "+title+" "+description)

