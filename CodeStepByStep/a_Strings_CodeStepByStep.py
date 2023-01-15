"""
Write a function named add_commas that accepts a string representing a number and returns a new
string with a comma at every third position, starting from the right. For example, the call of
add_commas("12345678") returns "12,345,678".
"""

def add_commas(str):
    with_commas = ''
    for i in range(1, len(str)+1):
        with_commas += str[-i]
        if i % 3 == 0:
            with_commas += ','
    return with_commas[::-1]

"""
Number of overlapping occurrences of substring
"""

def occ_str(str, substr):
    n_occ = 0
    len_substr = len(substr)
    for i in range(len(str) - len_substr):
        if substr in str[i:i + len_substr]:
            n_occ += 1
    return n_occ

# def occ_str(str, substr):
#     n_occ = 0
#     start = 0
#     while True:
#         start = str.find(substr, start)
#         if start == -1:
#             return n_occ
#         n_occ += 1
#         start += 1


"""
Check if all strings in list are not empty
"""

myList = ['a', 'abc', 'bc']
result = all(myList)
# print(f'Are all strings non-empty? {result}')

"""
FizzBuzz
"""

def fizzBuzz(n):
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

# fizzBuzz(15)
