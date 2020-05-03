import requests
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import re

output= open('wiki-fast-food-scrape.txt', 'w', encoding='utf8')
global count

food_url = 'https://en.wikipedia.org/wiki/List_of_fast_food_restaurant_chains'

request= urllib.request.Request(food_url)
opener= urllib.request.build_opener()
page_content= opener.open(request).read()

soup= BeautifulSoup(page_content, 'lxml')
count= 0

section= soup.findAll('div', {'class':'div-col columns column-width'})
for div in section:
    for ul in div.findAll('ul'):
        for li in ul.findAll('li'):
            print(li.text + '\n')
            output.write(li.text + '\n')
            count+=1

print('Count: ', count)
output.close()
