import mincemeat
import glob
import csv

# LOAD FILES PATH
text_files = glob.glob('./texts/*')


def file_contents(filename):
    with open(filename) as fp:
        return fp.read()

source = dict(
    (filename, file_contents(filename))
     for filename in text_files
)


def mapfn(k, v):
    # print 'map' + k
    from stopwords import allStopWords
    import string

    for line in v.splitlines():
        info, authors, title = line.split(":::")
        if "::" in authors:
            # Transform multiple authors in ITEMS
            authors = authors.split("::")
        else:
            # Transform a Single Author to ONE ITEM IN LIST
            authors = [authors]
        for word in title.split():
            # First, remove punctuations.
            word = word.translate(None, string.punctuation)

            # Now, transform to lowercase.
            word = word.lower()

            # Word should not be listed in Stopwords file.
            if word not in allStopWords and word != '':
                for author in authors:
                    yield author, word


def reducefn(k, v):
    from collections import Counter
    # K = Author (it's a key)
    # V = Array of words (it's a values)

    # print 'reduce ' + k

    return Counter(v)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("authors_most_frequently_words.csv", "w"))

for author, countered_words in results.items():
    w.writerow([author, countered_words])