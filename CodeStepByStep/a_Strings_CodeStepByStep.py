"""
Write a function named add_commas that accepts a string representing a number and returns a new
string with a comma at every third position, starting from the right. For example, the call of
add_commas("12345678") returns "12,345,678".
"""

def add_commas(str):
    with_commas = ''
    for i in range(1, len(str)+1):
        with_commas = with_commas + str[-i]
        if i % 3 == 0:
            with_commas = with_commas + ','
    return with_commas[::-1]

"""
Caesar Cipher
A Caesar cipher is a simple substitution cipher in which each letter of the plain text is
substituted with a letter found by moving n places down the alphabet. For example, assume
the input plain text is the following:

abcd xyz
If the shift value, n, is 4, then the encrypted text would be the following:

efgh bcd
You are to write a function that accepts two arguments, a plain-text message and a number
of letters to shift in the cipher. The function will return an encrypted string with all
letters transformed and all punctuation and whitespace remaining unchanged.

Note: You can assume the plain text is all lowercase ASCII.
"""

def caesar_cipher(message, num):
    letters = string.ascii_lowercase
    mask = letters[num :] + letters[: num]
    translation_table = str.maketrans(letters, mask)

    return message.translate(translation_table)

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
