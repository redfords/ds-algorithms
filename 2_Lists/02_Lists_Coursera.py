"""
Shakespeare used over 20,000 words in his works. But how would you
determine that? Download a copy of the file www.py4e.com/code3/romeo.txt.
List all unique words, sorted in alphabetical order, that are stored in
the file containing a subset of Shakespeare’s work.
"""

def count_unique_words():
    unique_words = list()
    words = list()

    for line in fhand:
        words = line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    unique_words.sort()
    print(unique_words)

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

count_unique_words()
fhand.close()