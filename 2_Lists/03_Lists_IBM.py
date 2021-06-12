
# Create a list a_list, with the following elements 1, hello, [1,2,3] and True.

a_list = [1, 'hello', [1, 2, 3] , True]

# Find the value stored at index 1 of a_list.

a_list[1]

# Retrieve the elements stored at index 1, 2 and 3 of a_list.

a_list[1:4]

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:

a = [1, 'a']
b = [2, 1, 'd']
a + b

"""
Remove duplicates from list, using membership operator, list in-place and converting to set.
"""

list1 = [2, 3, 7, 3, 6, 2, 8, 8]
list2 = []

for item in list1:
    if item not in list2:
        list2.append(item)

list1 = [2, 3, 7, 3, 6, 2, 8, 8]
index = 1

while index < len(list1):
    if list1[index] in list1[ : index]:
        list1.pop(index)
    else:
        index += 1

list1 = [2, 3, 7, 3, 6, 2, 8, 8]

set_list1 = set(list1)
list1 = list(set_list1)

"""
Append a list to another list, reverse list, sort list, shuffle list
"""

list1 = [6, 52, 74, 62]
list2 = [85, 17, 81, 92]

list1.extend(list2)
list1.reverse()
list1.sort() # ascending order
list1.sort(reverse = True) #descending order

import random
list1 = [2, 8, 4, 3, 1, 5]
random.shuffle(list1)

"""
List comprehension is a way of creating Python Lists, more idiomatic and concise when compared
to looping statements.
"""

list_1 = [2, 6, 7, 3]
list_2 = [1, 4, 2]
list_3 = [ x * y for x in list_1 for y in list_2 ]

# [2, 8, 4, 6, 24, 12, 7, 28, 14, 3, 12, 6]

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
list_3 = [ (x, y) for x in list_1 for y in list_2 ]

# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

list_1 = [7, 2, 6, 2, 5, 4, 3]
list_2 = [ x * x for x in list_1 if (x % 2 == 0) ]

# [4, 36, 4, 16]

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [ x * y for x in list_1 for y in list_2 if (x+y)%2 == 0 ]

# [5, 8, 12, 15]

"""
List comprehension with multiple conditions
"""

list_1 = [7, 2, -8, 6, 2, 15, 4, -2, 3, 9]
list_2 = [ x for x in list_1 if x > 0 if x % 3 == 0 ]

# [6, 15, 3, 9]

list_1 = [-2, -1, 0, 1, 2, 3]
list_2 = [4, 5, 6, 7, 8]
list_3 = [ x * y for x in list_1 for y in list_2 if x > 0 if y % 2 == 0 ]

# [4, 6, 8, 8, 12, 16, 12, 18, 24]

# slicing
start = 0
stop = 2 # the first value that is not in the slice
step = 1 # step is 1 by default

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[start:stop:step] # start through not past stop, by step

# using negative numbers
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

# step may be a negative number:
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed