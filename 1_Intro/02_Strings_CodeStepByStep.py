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

