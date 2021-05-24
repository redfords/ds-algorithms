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