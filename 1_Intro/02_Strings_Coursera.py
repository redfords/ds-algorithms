""" Take the following string: str = 'X-DSPAM-Confidence:0.8475'
Extract the portion of the string after the colon character and
convert the extracted string into a floating point number.
"""

def convert_to_float(str):
    atpos = str.find(':')
    print(float(str[atpos+1:]))

""" Write a program to read through a file and print the contents
of the file (line by line) all in upper case.

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH:

RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
"""

def uppercase():
    fname = input('Enter a file name: ')
    try:
            fhand = open(fname)
    except:
            print('File cannot be opened', fname)
            quit()
    for lx in fhand:
            ly = lx.rstrip()
            print(ly.upper())

""" Write a program to prompt for a file name, and then read through the
file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you reach the end of the file, print out the average spam confidence.
"""

def print_spam_avg():
    sum = 0.0
    count = 0
    for line in fhand:
        new_line = line.rstrip()
        if new_line.startswith('X-DSPAM-Confidence:'):
            count += 1
            sum += float(new_line[new_line.find(' ')+1:])
    print('Average spam confidence', sum / count)

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

print_spam_avg()
fhand.close()
