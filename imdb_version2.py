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


# %% getting movie name , its year and its rating
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
        movieNametd = tr.find('td',{'class':'titleColumn'})
        ratingtd = tr.find('td',{'class':'ratingColumn imdbRating'})
        #data = [td.a.string, td.span.string ,rating.strong.string]
        #f.write(data)
        f.write(movieNametd.a.string.replace(',',' ')+','+movieNametd.span.string+','+ratingtd.strong.string)
        f.write('\n')

# %% Scraping time , Genre, and releasing date from IMDB
import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/title/tt0111161/'
agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
headers = {"Accept-Language": "en-US,en;q=0.5", 'User-Agent': agent}
res2 =requests.get(url,headers=headers)
html = res2.text
soup2 = BeautifulSoup(html,'html.parser')
info = soup2.find('div',{'class':'sc-52d569c6-0 kNzJA-D'})
info1 = info.find('ul')#,{'role':'presemtation'})
info2 = info1.findAll('li',{'role':'presentation'})
#print(info)
#print(res2.status_code)
#for tag in info2:
#    print(tag)
list1 = []
for tag in info2:
    list1.append(tag.string)
print(list1)

#<div class="sc-52d569c6-0 kNzJA-D"><h1 textlength="24" data-testid="hero__pageTitle" class="sc-afe43def-0 esVJhx"><span class="sc-afe43def-1 fDTGTb">The Shawshank Redemption</span></h1><ul class="ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt" role="presentation"><li role="presentation" class="ipc-inline-list__item"><a class="ipc-link ipc-link--baseAlt ipc-link--inherit-color" role="button" tabindex="0" aria-disabled="false" href="/title/tt0111161/releaseinfo?ref_=tt_ov_rdat">1994</a></li><li role="presentation" class="ipc-inline-list__item"><a class="ipc-link ipc-link--baseAlt ipc-link--inherit-color" role="button" tabindex="0" aria-disabled="false" href="/title/tt0111161/parentalguide/certificates?ref_=tt_ov_pg">R</a></li><li role="presentation" class="ipc-inline-list__item">2h 22m</li></ul></div>
# url = 'https://www.imdb.com/chart/top/'
# headers = {"Accept-Language": "en-US,en;q=0.5"}
# res =requests.get(url,headers=headers)
# html = res.text
# soup = BeautifulSoup(html,'html.parser')
# tbody = soup.find('tbody', {'class':'lister-list'})
# trows = tbody.findAll('tr')
# for tr in trows:
#     td = tr.find('td',{'class':'titleColumn'})
#     #print(td.a.string, td.span.string )
#     movieId = td.a['href']
#     movieurl = f'https://www.imdb.com/{movieId}'
#     print(movieurl)
   

# %%
