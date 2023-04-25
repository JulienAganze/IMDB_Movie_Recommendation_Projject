# %%
# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.imdb.com/chart/top/'
# headers = {"Accept-Language": "en-US,en;q=0.5"}
# res =requests.get(url,headers=headers)
# html = res.text
# soup = BeautifulSoup(html,'html.parser')
# tbody = soup.find('tbody', {'class':'lister-list'})
# trows = tbody.findAll('tr')
# for tr in trows:
#     td = tr.find('td',{'class':'titleColumn'})
#     print(td.a.string, td.span.string )
  

# #print(soup.findAll('body', {'class':'lister-list'}))

# # %%
# for tag in tbody:
#     print(tag)


# %%
import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/chart/top/'
headers = {"Accept-Language": "en-US,en;q=0.5"}
res =requests.get(url,headers=headers)
html = res.text
soup = BeautifulSoup(html,'html.parser')
tbody = soup.find('tbody', {'class':'lister-list'})
trows = tbody.findAll('tr')
with open('moviesinfo.csv','w') as f:
    for tr in trows:
        td = tr.find('td',{'class':'titleColumn'})
        rating = tr.find('td',{'class':'ratingColumn imdbRating'})
        #data = [td.a.string, td.span.string ,rating.strong.string]
        #f.write(data)
        f.write(td.a.string.replace(',',' ')+','+td.span.string+','+rating.strong.string)
        f.write('\n')

  


