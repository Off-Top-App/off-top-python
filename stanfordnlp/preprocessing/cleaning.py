import os
import sys
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

output= open('clean-output.txt', 'w', encoding="utf8")
global count

def cleanData():
    with open(sys.argv[1], 'r', encoding="utf8") as input:
        data= input.read()
        count= 0
        for line in data.split():
            if (line.lower().isnumeric() or re.findall('[^A-Za-z0-9]', line) or not line.lower().isalpha()):
                print('-')
            else:
                output.write(line.lower() + '\tSPORT\n')
                print(line.lower())
                count+=1

    print('\nWord Count: ', count)
    input.close()
    output.close()

cleanData()


def cleanDataWTokens():
    with open(sys.argv[1], 'r', encoding="utf8") as input:
        data= input.read()
        count= 0
        for line in data.lower().split():
            tokens= word_tokenize(line)
            if(line.isalpha()):
                print(*tokens)
                output.write(str(*tokens) +'\tB-SPORT\n')
                count+=1

    print('\nWord Count: ', count)
    input.close()
    output.close()

cleanDataWTokens()
