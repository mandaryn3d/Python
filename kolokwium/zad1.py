
import sys
import re

url_regex = re.compile(r'^'+
        r'(http|https)://www.[\w]*.[\w]*/'
        )

def wypiszPlik(pathRead, pathWrite):
    count = 0
    plikR = open(pathRead)
    plikW = open(pathWrite, "w")
    for line in plikR:
        for word in line.split(' '):
            result = url_regex.match(word.replace("\n",""))
            if result:
                count+=1
                print str(count) + '. ' + word
                plikW.write(str(count) + '. ' + word)
    plikW.close()
    plikR.close()
    
sciezkaDoWczytania = sys.argv[1]
sciezkaDoZapisania = sys.argv[2]
wypiszPlik(sciezkaDoWczytania, sciezkaDoZapisania)
