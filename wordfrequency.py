from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
from collections import Counter
import string

#Initial
#Testpush

punctuation = str.maketrans('','', string.punctuation)

head = []
headtoken = []
stemmed = []
lineconv = []
cleanedwords = []

with open('C:/data/noteevents/noteevents_a.csv', 'r') as sourcefile:
    df = pd.read_csv(sourcefile, header=0)

k = 0

for line in df['text']:
    k += 1
    lineconv.append(word_tokenize(line))
    if k > 1:
        break

for words in lineconv:
    cleanedwords.append([s.translate(punctuation) for s in words])

cleanedwords = [word for sublist in cleanedwords for word in sublist]
cleanedwords = [word for word in cleanedwords if word != '']


print(cleanedwords)
ps = PorterStemmer()

for word in cleanedwords:
        stemmed.append(ps.stem(word))

stemmedcount = Counter(stemmed)

print(dict(stemmedcount))


