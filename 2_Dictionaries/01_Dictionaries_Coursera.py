""" Return the most frequent word in a file and the number of occurrences.
"""

def most_frequent_word():
    name = input('Enter the file name: ')
    handle = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    bigcount = None
    bigword = None
    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

    print(bigword, bigcount)


"""Exercise: Write a program to read through a mail log, and return how many messages
have come from each email address.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

Add code to the above program to figure out who has the most messages in the file.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
"""

def no_of_emails():
    name = input('Enter the file name: ')
    handle = open(name)

    counts = dict()
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            counts[words[1]] = counts.get(words[1], 0) + 1

    print(counts)
    print(max(counts, key = counts.get), max(counts.values()))
    handle.close()

no_of_emails()



