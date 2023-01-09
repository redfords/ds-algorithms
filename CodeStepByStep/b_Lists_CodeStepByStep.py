"""
Write a function named all_less that accepts two lists of integers and returns True
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

"""
Assume that a two-dimensional rectangular list of integers called matrix has been declared with
six rows and eight columns. Write a for loop to copy the contents of the second column into the
fifth column.
"""

def copy_column(matrix):
    for i in matrix:
        j = 0
        while j < len(i):
            if j == 1:
                i[4] = i[j]
            j += 1
    return matrix

"""
Write a function named count_duplicates that accepts a list of integers as a parameter and that
returns the number of duplicate values in the list. A duplicate value is a value that also occurs
earlier in the list. If a list named a contains [1, 4, 2, 4, 7, 1, 1, 9, 2, 3, 4, 1], then call
call of count_duplicates() should return 6 because there are three duplicates of the value 1, one
duplicate of the value 2, and two duplicates of the value 4.
"""

def count_duplicates(numbers):
    n_set = set()
    for n in numbers:
        if numbers.count(n) > 1:
            n_set.add(n)
    return len(n_set)

"""
Write a function named count_unique that accepts a list of integers as a parameter and returns a
count of the number of unique values that occur in the list. If the list contains multiple occurrences
of the same element value, only one of those occurrences should count toward your total. For example,
if a list named numbers stores [7, 7, 2, 2, 1, 2, 2, 7], the call of count_unique(numbers) should
return 3 because there are 3 unique values: 7, 2, and 1.
"""

def count_unique(num):
    unique_num = []
    for n in num:
        if n not in unique_num:
            unique_num.append(n)
    return len(unique_num)

"""
Write a function named double_list that takes a list of strings as a parameter and that replaces every
string with two of that string. For example, if the list stores the values ["how", "are", "you?"]
before the function is called, it should store the values ["how", "how", "are", "are", "you?", "you?"]
after the function finishes executing.
"""

def double_list(words):
    double_words = []
    for word in words:
        double_words.append(word)
        double_words.append(word)
    return double_words

"""
Write a function is_palindrome that accepts a list of strings as its argument and returns True if that
list is a palindrome (if it reads the same forwards as backwards) and False if not. The list
["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"] is a palindrome, so passing that list to
your function would return True. Lists with zero or one element are considered to be palindromes.
"""

def is_palindrome(words):
    if len(words) == 0 or len(words) == 1:
        return True
    i = 0
    j = 1
    while i < len(words):
        if words[i] != words[-j]:
            return False
        i += 1
        j += 1
    return True

"""
Write a function named is_sorted that accepts a list of real numbers as a parameter and returns True
if the list is in sorted (nondecreasing) order and False otherwise. For example, if lists named a and
and b store [16.1, 12.3, 22.2, 14.4] and [1.5, 4.3, 7.0, 19.5, 25.1, 46.2] respectively, the calls
is_sorted(a) and is_sorted(b) should return False and True respectively. Assume the list has at least
one element. A one-element list is considered to be sorted.
"""

def is_sorted(num):
    if len(num) == 1:
        return True
    i = 0
    while i < len(num) - 1:
        if num[i] > num[i + 1]:
            return False
        i += 1
    return True

"""
Write a function named split that accepts a list of integers as a parameter and returns a new list
twice as large as the original, replacing every integer from the original list with a pair of integers,
each half the original. If a number in the original list is odd, then the first number in the new pair
should be one higher than the second so that the sum equals the original number. For example, if a
variable named a refers to a list storing the values [18, 7, 4, 24, 11], the call of split(a) should
return a new list containing [9, 9, 4, 3, 2, 2, 12, 12, 6, 5].
"""

def split(num):
    split_num = []
    for n in num:
        div = int(n / 2)
        if n % 2 == 0:
            split_num.append(div)
            split_num.append(div)
        else:
            split_num.append(div + 1)
            split_num.append(div)
    return split_num

"""
Write a function named longest_sorted_sequence that accepts a list of integers as a parameter and
that returns the length of the longest sorted (nondecreasing) sequence of integers in the list.
"""

def longest_sorted_sequence(num):
    seq = 1
    longest_seq = 1
    
    if len(num) == 0:
        return 0

    for n in range(len(num) - 1):
        if num[n] <= num[n + 1]:
            seq += 1
        if num[n] > num[n + 1] or n == len(num) - 2:
            if seq > longest_seq:
                longest_seq = seq
            seq = 1
    return longest_seq

"""
Write a function price_is_right that accepts a list of integers bids and an integer price as
parameters. The function returns the element in the bids list that is closest in value to price
without being larger than price. For example, if bids stores the elements [200, 300, 250, 999, 40],
then price_is_right(bids, 280) should return 250, since 250 is the bid closest to 280 without going
over 280. If all bids are larger than price, then your function should return -1.
"""

def price_is_right(bids, price):
    new_bids = []

    for bid in bids:
        if bid == price:
            return bid
        elif bid < price:
            new_bids.append(bid)

    if len(new_bids) == 0:
        return -1
    else:
        return max(new_bids)
