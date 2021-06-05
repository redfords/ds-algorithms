"""
Arrays - DS
Reverse an array of integers.
"""

def reverseArray(a):
    reverse = list()
    i = 1
    while i <= (len(a)):
        reverse.append(a[-i])
        i += 1
    return reverse

def reverseArray(a):
    return a[: : -1]
