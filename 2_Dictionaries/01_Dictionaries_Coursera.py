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


""" Write a program to read through a mail log, and return how many messages have
come from each email address.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'ray@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'david.horwitz@uct.ac.za': 4, 'stephen.marquard@uct.ac.za': 2}

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


""" Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and only
count the letters a-z. Your program should not count spaces, digits, punctuation,
or anything other than the letters a-z.
"""

def letter_frequency():
    name = input("Enter the file: ")
    handle = open(name)

    counts = dict()
    text = handle.read().lower()
    for letter in text:
        if letter >= 'a' <= 'z':
            counts[letter] = counts.get(letter, 0) + 1
    
    sorted_counts = sorted( [ (v,k) for k,v in counts.items() ], reverse=True)
    for k,v in sorted_counts:
        print(k,v)

    handle.close()

letter_frequency()

