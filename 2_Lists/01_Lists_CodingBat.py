""" 
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3 """

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


""" Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False """

def array_front9(nums):
    length = len(nums)
    if length > 4:
        length = 4

    for i in range(length):
        if nums[i] == 9:
            return True
    return False


""" Given an array of ints, return True if the sequence of numbers 1, 2, 3 is in the array.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True """

def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
        

""" Given 2 strings, a and b, return the number of the positions where they contain the
same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az"
substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0 """

def string_match(a, b):
    length = min(len(a), len(b))
    count = 0
    for i in range(length - 1):
        if a[i] + a[i+1] == b[i] + b [i+1]:
            count += 1
    
    return count

    
""" Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7] """

def rotate_nums(nums):
    rotated = list()
    rotated = nums[1:]
    rotated.append(nums[0])
    return rotated

