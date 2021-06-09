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

"""
FizzBuzz
"""

import math
import os
import random
import re
import sys

def fizzBuzz(n):
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

fizzBuzz(15)
