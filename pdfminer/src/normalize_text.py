
#from cStringIO import StringIO
import io
import os
import sys
import re
import string
import math
import multiprocessing
import collections
from nltk import pos_tag
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

def convertMultiple(txtDir, cleanedTxtDir):
    if txtDir == "": txtDir = os.getcwd() + "\\" #if no pdfDir passed in
    MASTER_LIST = collections.Counter() #houses all lemmas and  combined counts from all pdfs/txts

    for txt in os.listdir(txtDir): #iterate through txts in txt directory
        fileExtension = txt.split(".")[-1]
        if fileExtension == "txt":
            txtFilename = txtDir + txt
            text = clean(txtFilename) #get LIST of text content of pdf

            MASTER_LIST += collections.Counter(text) #wtf is wrong with you, its clearly passed as a counter object!
            txt = os.path.splitext(txt)[0] #remove .txt extension
            txt = os.path.splitext(txt)[0] #remove .pdf extension, this is stupid...
            cleanedFilename = cleanedTxtDir + txt + "_cleaned_pass1.txt"

            with open(cleanedFilename, 'w') as f:
                for item in text:
                    f.write("%s\n" % item)
    print(MASTER_LIST)

    #at this point remove counts of 2 or less (assumes you have a large data set)

    masterTxtFilename = cleanedTxtDir + "_to_DB.txt"
    with open(masterTxtFilename, 'w') as f:
        for k, v in MASTER_LIST.items():
            f.write("{} {}\n".format(k, v))

def clean(fname):

    with open(fname) as infile:
        data = infile.read()
    if len(data) == 0: #indicates an empty file
        return ''
    data = data.lower() #convert to lowercase
    data = re.sub('[^a-zA-Z0-9]', ' ', data) #remove punctuation (and weird chars!)
    data = re.sub(r'\d+', ' ', data) #remove numbers?
    data = ' '.join(word for word in data.split() if len(word) > 2)  # remove 2 letter 'words' or smaller
    data = ' '.join([word for word in data.split() if word not in stopWords]) #remove stop words

    #lemmatize:
    dataTokenized = sorted(word_tokenize(data))  # tokenize data
    dataLemma = []
    lemmatizer = WordNetLemmatizer()
    for word, tag in pos_tag(dataTokenized):
        wntag = tag[0].lower()
        wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
        lemma = lemmatizer.lemmatize(word, wntag) if wntag else word
        dataLemma.append(lemma)

    #stemming:
    ps = PorterStemmer()
    dataStemmed = []
    for word in dataLemma:
        dataStemmed.append(ps.stem(word))

    #count and create dictionary of cur file to be returned
    curDict = collections.Counter(dataStemmed)
    return curDict

stopWords = stopwords.words('english')
txtDir = "C:/Users/nico/Desktop/Off-Top/off-top-python/pdfminer/txt/"
cleanedTxtDir ="C:/Users/nico/Desktop/Off-Top/off-top-python/pdfminer/clean/"

convertMultiple(txtDir, cleanedTxtDir)

