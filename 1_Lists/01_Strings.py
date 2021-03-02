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

