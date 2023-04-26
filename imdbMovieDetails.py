# %%
import requests
from bs4 import BeautifulSoup

movieName = input('Enter Movie Name: ')
movieName = movieName.lower()

# Hitting at the imdb top 250 movies
url = 'https://www.imdb.com/chart/top/'
headers = {"Accept-Language": "en-US,en;q=0.5"}
res =requests.get(url,headers=headers)
html = res.text

soup = BeautifulSoup(html,'html.parser')
tbody = soup.find('tbody', {'class':'lister-list'})
trows = tbody.findAll('tr')
for tr in trows:
    td = tr.find('td',{'class':'titleColumn'})
    imdbMovieName = td.a.string.strip().lower()
    #print(imdbMovieName)
    if  imdbMovieName== movieName:
        movieId = td.a['href']
        movieurl = f'https://www.imdb.com/{movieId}'
      
        # Hitting at the movie url
        url_movie = movieurl
        agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        headers = {"Accept-Language": "en-US,en;q=0.5", 'User-Agent': agent}
        res2 =requests.get(url_movie,headers=headers)
        html = res2.text
        soup2 = BeautifulSoup(html,'html.parser')
        summary = soup2.find('div',{'class':'ipc-metadata-list-item__content-container'})
        
        dirId = summary.a['href']
        dirurl = f'https://www.imdb.com/{dirId}'
        print('Director Name: ',summary.a.string)
        #print(dirurl)

        # Hitting at the director url to recommenr four ovies from that director
        url_dir = dirurl
        res3 = requests.get(url_dir,headers=headers)
        html = res3.text
        soup3 = BeautifulSoup(html,'html.parser')
        Knownfor = soup3.find('div',{'class':'ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid'})
        #MovieDivs = Knownfor.findAll('div',{'class':'ipc-poster ipc-poster--base ipc-poster--dynamic-width ipc-primary-image-list-card__poster ipc-sub-grid-item ipc-sub-grid-item--span-2'})
        for div in Knownfor:
            moviediv= div.find('div',{'class':'ipc-primary-image-list-card__content-top'})
            print(moviediv.a.string)

        break  
        














#<div class="ipc-primary-image-list-card__content-top"><a class="ipc-primary-image-list-card__title" role="button" tabindex="0" aria-disabled="false" href="/title/tt0111161/?ref_=nm_knf_t_1">The Shawshank Redemption</a></div>


# url_movie = 'https://www.imdb.com/title/tt0111161/'
# agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# headers = {"Accept-Language": "en-US,en;q=0.5", 'User-Agent': agent}
# res2 =requests.get(url_movie,headers=headers)
# html = res2.text
# soup2 = BeautifulSoup(html,'html.parser')
# summary = soup2.find('div',{'class':'ipc-metadata-list-item__content-container'})
# print(summary.a.string)
# dirId = summary.a['href']
# dirurl = f'https://www.imdb.com/{dirId}'
# print(dirurl)















