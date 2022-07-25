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