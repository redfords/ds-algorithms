""" Given a string, return a new string where "not " has been added to the front.
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


""" Given a non-empty string and an int n, return a new string where the char at index n
has been removed. The value of n will be a valid index of a char in the original string
(i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn' """

def missing_char(str, n):
    return str[:n] + str[n+1:]


""" Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba' """

def front_back(str):

    if len(str) <= 1:
        return str
        
    if len(str) == 2:
        return str[len(str) - 1] + str[0]
    else:
        return str[len(str) - 1] + str[1:len(str) - 1] + str[0]


""" Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc' """

def front3(str):
    if len(str) < 3:
        return str + str + str
    else:
        return str[:3] + str[:3] + str[:3]


""" Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi' """

def string_times(str, n):
    new_str = ''
    for i in range(n):
        new_str = new_str + str
    return new_str


""" Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc' """

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


""" Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello' """

def string_bits(str):
    new_str = ''
    for i in range(len(str)):
        if i % 2 == 0:
            new_str = new_str + str[i]
    return new_str

    