import os
import sys
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import unicodedata

#nltk.download()
#python -m nltk.downloader all
#Default location - C:\Users\smika\AppData\Roaming\nltk_data

output= open('deep-clean-output18.txt', 'w', encoding="utf8")
global count

def cleanData():
    with open(sys.argv[1], 'r', encoding="utf8") as input:
        data= input.read()
        count= 0
        for line in data.lower().split():
            tokens= word_tokenize(line)
            if(line.isalpha()):
                print(*tokens)
                output.write(str(*tokens) +'\tB-FOOD\n')
                count+=1

    print('\nWord Count: ', count)
    input.close()
    output.close()

cleanData()
