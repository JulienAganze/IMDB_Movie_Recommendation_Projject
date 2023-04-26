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

# %% Scraping duration time of the movie  from IMDB
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
headers = {"Accept-Language": "en-US,en;q=0.5"}
res =requests.get(url,headers=headers)
html = res.text
soup = BeautifulSoup(html,'html.parser')
tbody = soup.find('tbody', {'class':'lister-list'})
trows = tbody.findAll('tr')
for tr in trows:
    td = tr.find('td',{'class':'titleColumn'})
    #print(td.a.string, td.span.string )
    movieId = td.a['href']
    movieurl = f'https://www.imdb.com/{movieId}'
    url_to_ignore = 'https://www.imdb.com/title/tt0056058/'
   # print(movieurl)
    try:
        # movie name
        print(td.a.string)

        # moive duration
        url_movie = movieurl
        agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        headers = {"Accept-Language": "en-US,en;q=0.5", 'User-Agent': agent}
        res2 =requests.get(url_movie,headers=headers)
        html = res2.text
        soup2 = BeautifulSoup(html,'html.parser',multi_valued_attributes=None)
        duration_info = soup2.find('div',{'class':'sc-52d569c6-0 kNzJA-D'})
        duration_info1 = duration_info.find('ul')
        li = duration_info1.findAll('li')
        print(li[2].string)
        
        ##------Genre---------
        genre_info = soup2.find('div',{'class':'sc-385ac629-10 SacCW'})
        genre_info1 = genre_info.find('section')#,{'role':'presemtation'})
        genre_info2 = genre_info1.find('div',{'class':'ipc-chip-list--baseAlt ipc-chip-list'})
        genre_info3 = genre_info2.findAll('div',{'class':'ipc-chip-list__scroller'})
        for tag in genre_info3:
            print(tag.a.span.string)

        ## -------Release year and place--------
        release_info_url = movieurl+'releaseinfo/'
        agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        headers = {"Accept-Language": "en-US,en;q=0.5", 'User-Agent': agent}
        res_rel =requests.get(release_info_url,headers=headers)
        html_rel = res_rel.text
        soup4 = BeautifulSoup(html_rel,'html.parser')
        release_info = soup4.find('div',{'data-testid':'sub-section-releases'})
        release_info1 = release_info.find('div')
        release_info2 = release_info.find('ul')
        for tag in release_info1:
            print(tag.li.span.string, '('+release_info2.li.a.string+')')
        #print('('+release_info2.li.a.string+')')

        
        #print(td.span.string )
        print('\n')
    except:
        pass
# %% try getting the genre
import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/title/tt0111161/'
agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
headers = {"Accept-Language": "en-US,en;q=0.5", 'User-Agent': agent}
res2 =requests.get(url,headers=headers)
html = res2.text
soup3 = BeautifulSoup(html,'html.parser')
info = soup3.find('div',{'class':'sc-385ac629-10 SacCW'})
info1 = info.find('section')#,{'role':'presemtation'})
info2 = info1.find('div',{'class':'ipc-chip-list--baseAlt ipc-chip-list'})
info3 = info2.findAll('div',{'class':'ipc-chip-list__scroller'})
for tag in info3:
    print(tag.a.span.string)


# %% Getting the release date and place
import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/title/tt0111161/releaseinfo/'
agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
headers = {"Accept-Language": "en-US,en;q=0.5", 'User-Agent': agent}
res2 =requests.get(url,headers=headers)
html = res2.text
soup4 = BeautifulSoup(html,'html.parser')
info = soup4.find('div',{'data-testid':'sub-section-releases'})
info1 = info.find('div')
info2 = info.find('ul')
for tag in info1:
    print(tag.li.span.string, '('+info2.li.a.string+')')
print('('+info2.li.a.string+')')


