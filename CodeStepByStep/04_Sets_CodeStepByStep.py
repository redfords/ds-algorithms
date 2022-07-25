"""
Write a function named is_happy_number that returns whether a given integer is "happy". An integer
is "happy" if repeatedly summing the squares of its digits eventually leads to the number 1.

For example, 139 is happy because:
12 + 32 + 92 = 91
92 + 12 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

By contrast, 4 is not happy because:
42 = 16
12 + 62 = 37
32 + 72 = 58
52 + 82 = 89
82 + 92 = 145
12 + 42 + 52 = 42
42 + 22 = 20
22 + 02 = 4
...
"""



"""
Write a function max_length that accepts as a parameter a set of strings, and that returns the
length of the longest string in the set. If it's an empty set, it should return 0.
"""

def max_length(words):
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

"""
Write a function named num_in_common that accepts two lists of integers as parameters and returns
the count of how many unique integers occur in both lists. For example, if two lists named l1 and
l2 contains the values [3, 7, 3, -1, 2, 3, 7, 2, 15, 15] and [-5, 15, 2, -1, 7, 15, 36], your
function should return 4 because the elements -1, 2, 7, and 15 occur in both lists. Use one or more
sets as storage to help you solve this problem. Do not modify the lists passed in.
"""

def num_in_common(list_1, list_2):
    in_common = set()
    for num in list_1:
        if num in list_2:
            in_common.add(num)
    return len(in_common)

"""
Write a function named num_unique_values that accepts a list of integers as a parameter and returns
the number of unique integer values in the list. For example, if a list named l contains the values
[3, 7, 3, -1, 2, 3, 7, 2, 15, 15], the call of num_unique_values(l) should return 5. If passed the
empty list, you should return 0. Use a set as auxiliary storage to help you solve this problem. Do
not modify the list passed in.
"""

def num_unique_values(nums):
    unique_values = set()
    for num in nums:
        unique_values.add(num)
    return len(unique_values)

"""
Write a function named remove_range that accepts three parameters: a set of integers, a minimum value,
and a maximum value. The function should remove any values from the set that are between that minimum
and maximum value, inclusive. For example, if a set named s contains {3, 17, -1, 4, 9, 2, 14}, the
call of remove_range(s, 1, 10) should modify s to store {17, -1, 14}.
"""

def remove_range(nums, min_value, max_value):
    to_remove = list()
    for num in nums:
        if num > min_value and num < max_value:
            to_remove.append(num)

    nums.difference_update(to_remove)
    return nums

"""
Write a function named twice that accepts as a parameter a list of integers and returns a set
containing all the numbers in the list that appear exactly twice. For example, if a list variable
v stores {1, 3, 1, 4, 3, 7, -2, 0, 7, -2, -2, 1}, the call of twice(v) should return the set {3, 7}.

If you want an extra challenge: Use only sets as auxiliary storage.
"""

def twice_list(nums):
    return set([i for i in nums if nums.count(i) == 2])

def twice_dict(nums):
    count = dict()
    set_nums = set()

    for num in nums:
        count[num] = count.get(num, 0) + 1

    for key, value in count.items():
        if value == 2:
            set_nums.add(key)

    return set_nums

"""
Write a function named word_count that accepts a file name as a parameter and opens that file and
that returns a count of the number of unique words in the file. Do not worry about capitalization
and punctuation for example, "Hello" and "hello" and "hello!!" are different words for this problem.
Use a set as auxiliary storage.
"""

def word_count(file_name):
    handle = open(file_name)
    unique_words = set()
    for line in handle:
        words = line.split()
        for word in words:
            unique_words.add(word)

    return len(unique_words)

"""
Write a function named has_odd that takes a set of integers as a parameter and that returns True if
the set contains at least one odd integer, and False otherwise. If passed the empty set, your
function should return False.
"""

def has_odd(nums):
    for num in nums:
        if num % 2 != 0:
            return True
    return False