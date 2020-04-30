import requests
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import re

output= open('wiki-food-scrape.txt', 'w', encoding='utf8')
global count

food_url = 'https://en.wikipedia.org/wiki/List_of_culinary_fruits'

request= urllib.request.Request(food_url)
opener= urllib.request.build_opener()
page_content= opener.open(request).read()

soup= BeautifulSoup(page_content, 'lxml')
count= 0

section= soup.findAll('tbody')
for x in section:
    for tr in x.findAll('tr'):
        for td in tr.findAll('td'):
            for a in td.findAll('a'):
                print(a.text + '\n')
                output.write(a.text + '\n')
                count+=1
            for i in td.findAll('i'):
                print(i.text + '\n')
                output.write(i.text + '\n')
                count+=1

print('Count: ', count)
output.close()
