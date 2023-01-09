"""
Take the following string: str = 'X-DSPAM-Confidence:0.8475' Extract the portion of the
string after the colon character and convert the extracted string into a floating point number.
"""

def convert_to_float(str):
    atpos = str.find(':')
    print(float(str[atpos+1:]))

"""
Write a program to read through a file and print the contents of the file (line by line) all in upper case.

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

"""
Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you reach the end of the file, print out the average spam confidence.
"""

def get_file_name():

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

"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def not_string(str):
    if str.startswith('not '):
        return str
    else:
        return 'not ' + str

"""
Given a non-empty string and an int n, return a new string where the char at index n
has been removed. The value of n will be a valid index of a char in the original string
(i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""

def missing_char(str, n):
    return str[:n] + str[n+1:]

"""
Given a string, return a new string where the first and last chars have been exchanged.

exchange_first_last('code') → 'eodc'
exchange_first_last('a') → 'a'
exchange_first_last('ab') → 'ba'
"""

def exchange_first_last(str):
    if len(str) <= 1:
        return str        
    if len(str) == 2:
        return str[len(str)-1] + str[0]
    else:
        return str[len(str)-1] + str[1:len(str)-1] + str[0]

"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is
less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""

def front3(str):
    if len(str) > 3:
        str = str[:3]
    return str * 3

"""
Given a string and a non-negative int n, return a larger string that is n copies
of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
"""

def string_times(str, n):
    new_str = ''
    for i in range(n):
        new_str = new_str + str
    return new_str

"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""

def front_times(str, n):
    front = ''
    new_str = ''
    if len(str) < 3:
        front = str
    else:
        front = str[:3]
    for i in range(n):
        new_str = new_str + front
    return new_str

"""
Given a string, return a new string made of every other char starting with the first.

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
    new_str = ''
    for i in range(len(str)):
        if i % 2 == 0:
            new_str = new_str + str[i]
    return new_str
    
"""
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""

def double_char(str):
    new_str = ''
    for letter in str:
        new_str += letter + letter
    return new_str

"""
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""

def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] == 'h' and str[i + 1] == 'i':
            count += 1
    return count

"""
Return True if the string "cat" and "dog" appear the same number of times.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

def cat_dog(str):
    cat = 0
    dog = 0
    for i in range(len(str) - 2):
        if str[i] == 'c' and str[i + 1] == 'a' and str[i + 2] == 't':
            cat += 1
        if str[i] == 'd' and str[i + 1] == 'o' and str[i + 2] == 'g':
            dog += 1
    return cat == dog

"""
Given two strings, return True if either of the strings appears at very end of the other string,
ignoring upper/lower case differences.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → Tru
"""

def end_other(a, b):
    lower_a = a.lower()
    lower_b = b.lower()

    if lower_a == lower_b:
        return True

    if len(a) == len(b) and not lower_a == lower_b:
        return False

    if len(a) < len(b):
        lower_b = lower_b[len(b) - len(a):]
    else:
        lower_a = lower_a[len(a) - len(b):]
    
    return lower_a == lower_b