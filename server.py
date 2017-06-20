import mincemeat
import glob
import csv
import argparse

# LOAD FILES PATH
text_files = glob.glob('./texts/*')

# PARAMETERS
parser = argparse.ArgumentParser()
parser.add_argument('--authors',
                    nargs='+',
                    help='name of authors like "Grzegorz Rozenberg" "Philip S. Yu"',
                    default=[]
                    )


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

# Write a CSV
w = csv.writer(open("authors_most_frequently_words.csv", "w"))

for author, countered_words in results.items():
    w.writerow([author, countered_words])

# Print selected authors

args = parser.parse_args()

if args.authors:
    for author in args.authors:
        print("\nAuthor: %s" % author)
        print("==== Frequently Words")
        for word, frequency in results[author].most_common():
            print("======== %s - %d times" % (word, frequency))
