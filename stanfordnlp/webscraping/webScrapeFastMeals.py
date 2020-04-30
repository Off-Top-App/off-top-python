import requests
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import re

output= open('wiki-fast-meals-scrape.txt', 'w', encoding='utf8')
global count

food_url = 'http://fastfood.theringer.com/'

request= urllib.request.Request(food_url)
opener= urllib.request.build_opener()
page_content= opener.open(request).read()

soup= BeautifulSoup(page_content, 'lxml')
count= 0

section= soup.findAll('span')
for x in section:
    print(x.text + '\n')
    output.write(x.text + '\n')
    count+=1

print('Count: ', count)
output.close()
