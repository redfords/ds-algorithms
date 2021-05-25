"""
Number of overlapping occurrences of substring
"""

string = 'abcdefghghghghghgh.'
substring = 'ghg'

count = 0
start = 0

for i in range(len(string)):
    i = string.find(substring, start)
    if i > 0:
        start = i + 1
        count += 1
    else:
        break

"""
Check if all strings in list are not empty
"""

myList = ['a', 'abc', 'bc']
result = all(myList)
print(f'Are all strings non-empty? {result}')