"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def not_string(str):
    if str.startswith('not'):
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

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

def front_back(str):

    if len(str) <= 1:
        return str
        
    if len(str) == 2:
        return str[len(str) - 1] + str[0]
    else:
        return str[len(str) - 1] + str[1:len(str) - 1] + str[0]


"""
Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there.
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""

def front3(str):
    if len(str) < 3:
        return str + str + str
    else:
        return str[:3] + str[:3] + str[:3]


"""
Given a string and a non-negative int n, return a larger string that is n copies
of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

def string_times(str, n):
    new_str = ''
    for i in range(n):
        new_str = new_str + str
    return new_str


"""
Given a string and a non-negative int n, we'll say that the front of the string
is the first 3 chars, or whatever is there if the string is less than length 3.
Return n copies of the front;

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
Given a string, return a string where for every char in the original,
there are two chars.

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
Given two strings, return True if either of the strings appears at
very end of the other string, ignoring upper/lower case differences.

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
