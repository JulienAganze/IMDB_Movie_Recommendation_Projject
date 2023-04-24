# %%
import requests
res =requests.get('https://www.imdb.com/chart/top/')
print(res.text)
