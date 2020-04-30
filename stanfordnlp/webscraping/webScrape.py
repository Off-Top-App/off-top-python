import requests
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import re

output= open('food-scrape.txt', 'w', encoding='utf8')
global count

food_url = 'http://eatingatoz.com/food-list'

request= urllib.request.Request(food_url)
opener= urllib.request.build_opener()
page_content= opener.open(request).read()

soup= BeautifulSoup(page_content, 'lxml')
count= 0

section= soup.findAll('div', {'class': 'entry'})
for x in section:
    for ul in x.findAll('ul'):
        for li in ul.findAll('li'):
            print(li.text.replace(' ', '\n'))
            output.write(li.text.lower().replace(' ', '\n') + '\n')
            count+=1
            #print(li.text.split(' ', 1)[0])
print('Count: ', count)
output.close()
