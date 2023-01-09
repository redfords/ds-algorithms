"""
Shakespeare used over 20,000 words in his works. But how would you
determine that? Download a copy of the file www.py4e.com/code3/romeo.txt.
List all unique words, sorted in alphabetical order, that are stored in
the file containing a subset of Shakespeare’s work.
"""

def count_unique_words():
    unique_words = list()
    words = list()

    for line in fhand:
        words = line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    unique_words.sort()
    print(unique_words)

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

count_unique_words()
fhand.close()

""" 
Given an array of ints, return the number of 9's in the array.

array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""

def array_count9(nums):
    return sum(num == 9 for num in nums)

"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
"""

def array_front9(nums):
    length = len(nums)
    if length > 4:
        length = 4

    for i in range(length):
        if nums[i] == 9:
            return True
    return False

"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 is in the array.

array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

"""
Given 2 strings, a and b, return the number of the positions where they contain the
same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az"
substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'axc') → 0
"""

def string_match(a, b):
    length = min(len(a), len(b))
    return sum(a[i] + a[i+1] == b[i] + b [i+1] for i in range(length - 1))

"""
Given an array of ints length 3, return an array with the elements "rotated left"
so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
"""

def rotate_nums(nums):
    return nums[1:] + [nums[0]]

"""
Given an array length 1 or more of ints, return the difference between the largest
and smallest values in the array.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
"""

def big_diff(nums):
    return max(nums) - min(nums)

"""
Return the "centered" average of an array of ints, which is the mean average of the
values, except ignoring the largest and smallest values in the array. You may assume that
the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""

def centered_average(nums):
    max_num = nums[0]
    min_num = nums[0]
    
    for num in nums:
        max_num = max(num, max_num) 
        min_num = min(num, min_num)
    
    nums.remove(max_num)
    nums.remove(min_num)
    
    nums_sum = 0
    count = 0
    for num in nums:
        nums_sum += num
        count += 1
    return nums_sum / count


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