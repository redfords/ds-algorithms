"""
Write a function named add_commas that accepts a string representing a number and returns a new
string with a comma at every third position, starting from the right. For example, the call of
add_commas("12345678") returns "12,345,678".
"""

def add_commas(str):
    str_commas = ''
    i = -1
    while i >= -abs(len(str)):
        str_commas = str_commas + str[i]
        if i % 3 == 0:
            str_commas = str_commas + ','
        i -= 1

    return str_commas[: : -1]   

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