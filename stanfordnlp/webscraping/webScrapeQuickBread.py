import requests
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import re

output= open('wiki-quick-bread-scrape.txt', 'w', encoding='utf8')
global count

food_url = 'https://en.wikipedia.org/wiki/List_of_quick_breads'

request= urllib.request.Request(food_url)
opener= urllib.request.build_opener()
page_content= opener.open(request).read()

soup= BeautifulSoup(page_content, 'lxml')
count= 0

section= soup.findAll('div', {'class':'mw-parser-output'})
for x in section:
    for ul in x.findAll('ul'):
        for li in ul.findAll('li'):
            for a in li.findAll('a'):
                print(a.text + '\n')
                output.write(a.text + '\n')
                count+=1

print('Count: ', count)
output.close()
