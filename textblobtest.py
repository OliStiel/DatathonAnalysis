import textblob as tb
import pandas as pd
import nltk as nt


class NoteAcceptor:
    notecount = 0

    def __init__(self, note):
        self.note = note
        NoteAcceptor.notecount += 1

        blob = tb.TextBlob(note)
        for i in blob.sentences:
            print("SENTENCE:", i, "POLARITY: ", i.sentiment.polarity)

with open('C:/data/noteevents/noteevents_b.csv', 'r') as sourcefile:
    df = pd.read_csv(sourcefile, header=0, nrows=3, skiprows=0)

k = 0
for i in df['text']:
    NoteAcceptor(df['text'].values[k])
    k += 1

print(NoteAcceptor.notecount)



