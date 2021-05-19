""" Write a function named all_less that accepts two lists of integers and returns True
if each element in the first list is less than the element at the same index in the
second list. Your function should return false if the lists are not the same length.
"""

def all_less(a, b):
    if len(a) != len(b):
        return False
    less = True
    for i in range(len(a)):
        if a[i] >= b[i]:
            less = False
    return less

"""
Write a function named average that accepts a list of integers as its parameter and returns the
average (arithmetic mean) of all elements in the list as a float. For example, if the list passed
contains the values [1, -2, 4, -4, 9, -6, 16, -8, 25, -10], the calculated average should be 2.5.
You may assume that the list contains at least one element.
"""

def average(num):
    return float(sum(num)) / float(len(num))

""" Write a function named average_length of code that computes and returns the average
string length of the elements of a list of strings. For example, if the list contains
["belt", "hat", "jelly", "bubble gum"], the average length returned should be 5.5. Assume
that the list has at least one element.
"""

def average_length(a):
    letters = 0
    for word in a:
        letters += len(word)
    return float(letters / len(a))

""" Write a function named collapse that accepts a list of integers as a parameter and
returns a new list where each pair of integers from the original list has been replaced by
the sum of that pair. For example, if a list called a stores [7, 2, 8, 9, 4, 13, 7, 1, 9, 10],
then the call of collapse(a) should return a new list containing [9, 17, 17, 8, 19].

If the list stores an odd number of elements, the element is not collapsed. For example, if
the list had been [1, 2, 3, 4, 5], then the call would return [3, 7, 5]. Your function should
not change the list that is passed as a parameter.
"""

def collapse(a):
    collapsed_list = list()
    i = 0
    while i < len(a) - 1:
        collapsed_list.append(a[i] + a[i + 1])
        i += 2 
    if len(a)%2 != 0:
        collapsed_list.append(a[-1])
    return collapsed_list

"""
Write a function named collapse_pairs that accepts a list of integers as a parameter and modifies
the list so that each of its pairs of neighboring integers (such as the pair at indexes 0-1, and
the pair at indexes 2-3, etc.) are combined into a single sum of that pair. The sum will be stored
at the even index (0,2,4, etc.) if the sum is even and at the odd index (1,3,5, etc.) if the sum
is odd. The other index of the pair will change to 0.

List [7,  2,  8,  9,  4, 22,  7,  1,  9, 10] returns [0,  9,  0, 17, 26,  0,  8,  0,  0, 19]
"""

def collapse_pairs(pairs):
    i = 0
    while i < len(pairs) - 1:
        sum_pairs = pairs[i] + pairs[i + 1]
        if sum_pairs % 2 == 0:
            pairs[i] = sum_pairs
            pairs[i + 1] = 0
        else:
            pairs[i + 1] = sum_pairs
            pairs[i] = 0
        i += 2
    
    return pairs

"""
Write a function named contains that accepts two lists of integers a1 and a2 as parameters and that
returns a value indicating whether or not a2's sequence of elements appears in a1 (True for yes,
False for no). The sequence of elements in a2 may appear anywhere in a1 but must appear consecutively
and in the same order. 
"""

def contains(main_list, sub_list):
    contains = False
    for i in range(len(main_list)):
        if main_list[i] == sub_list[0]:
            n = 1
            while (n < len(sub_list)) and (main_list[i + n] == sub_list[n]):
                n += 1
            
            if n == len(sub_list):
                contains = True
    return contains

