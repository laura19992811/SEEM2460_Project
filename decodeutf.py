import codecs
import unicodedata
f = open("output.txt","r")
#with codecs.open('output.txt', encoding='utf-8') as f:
for line in f:
    print(line.encode("utf-8").decode("utf-8"))
