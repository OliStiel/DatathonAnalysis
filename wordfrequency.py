from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
from collections import Counter, OrderedDict
import string
import seaborn as sns
from stop_words import get_stop_words


def numberCheck(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def countAndOrder(wordlist,countlist,headNum):
    df = pd.DataFrame({"words": wordlist, "count": countlist})
    grouped = df.sort_values('count', ascending=False).head(headNum)

    return grouped

punctuation = str.maketrans('','', string.punctuation)

head = []
headtoken = []
stemmed = []
lineconv = []
cleanedwords = []
stop_words = get_stop_words('en')

with open('C:/data/noteevents/noteevents_b.csv', 'r') as sourcefile:
    df = pd.read_csv(sourcefile, header=0)

with open('C:/data/f_pats.csv', 'r') as demogsfile:
    female = demogsfile.readlines()

docs = df.loc[(df['subject_id'].isin(female)) & (df['category'] == 'Nursing/other')]["text"]

doccount = docs.shape[0]

for line in docs:
    count =+ 1
    lineconv.append(word_tokenize(line))
    if count > 5000:
        break


for words in lineconv:
    cleanedwords.append([s.translate(punctuation) for s in words])

cleanedwords = [word for sublist in cleanedwords for word in sublist]
cleanedwords = [word for word in cleanedwords if word != '' and numberCheck(word) == False and word not in stop_words and len(word)>1]

ps = PorterStemmer()

for word in cleanedwords:
        stemmed.append(ps.stem(word))

stemmedcount = dict(Counter(stemmed))
orderedcount = OrderedDict(sorted(stemmedcount.items()))

wordlist = list(orderedcount.keys())
countlist = list(orderedcount.values())

grouped10 = countAndOrder(wordlist, countlist, 100)

# sns.barplot("words", "count", data=grouped10)
# sns.plt.plot()
# sns.plt.show()

for i,m in grouped10.values:
    print(i/doccount,m,i)
