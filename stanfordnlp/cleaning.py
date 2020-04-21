import os
import sys
import re

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
