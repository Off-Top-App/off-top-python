import os
import sys

output= open('output-sports.txt', 'w', encoding="utf8")

def generateFormat():
    with open(sys.argv[1], encoding="utf8") as input:
        data= input.read()
        for line in data.split():
            print(line + "\tSPORT\n")
            output.write(line+'\n')
    output.close()
    input.close()

generateFormat()
