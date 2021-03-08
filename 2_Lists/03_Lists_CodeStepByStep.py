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
