# %%
import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/chart/top/'
headers = {"Accept-Language": "en-US,en;q=0.5"}
res =requests.get(url,headers=headers)
html = res.text
soup = BeautifulSoup(html,'html.parser')
for tag in soup.findAll('img'):
    print(tag['alt'])

# %%
import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/chart/top/'
headers = {"Accept-Language": "en-US,en;q=0.5"}
res =requests.get(url,headers=headers)
html = res.text
soup = BeautifulSoup(html,'html.parser')
for tag in soup.findAll('span',{'class':'secondaryInfo'}):
    print(tag.string.replace('(','').replace(')',''))

