"""
Check if Word Equals Summation of Two Words
The letter value of a letter is its position in the alphabet starting from 0 
(i.e. 'a' -> 0, 'b' -> 1, etc.).
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase
English letters 'a' through 'j' inclusive.
Return true if the summation of the numerical values of firstWord and secondWord equals the
numerical value of targetWord, or false otherwise.

Example 1:
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.
"""

def isSumEqual(firstWord, secondWord, targetWord):
    first = "".join([str(ord(i) - 97) for i in firstWord])
    second = "".join([str(ord(i) - 97) for i in secondWord])
    target = "".join([str(ord(i) - 97) for i in targetWord])

    return int(first) + int(second) == int(target)

"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1" -> 
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

def defang_ip_addr(str):
    return '[.]'.join(str.split('.'))
    # return str.replace('.', '[.]')

"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

Input: operations = ["--X","X++","X++"]
Output: 1

Input: operations = ["++X","++X","X++"]
Output: 3

Input: operations = ["X++","++X","--X","X--"]
Output: 0
"""

def final_value_after_operations(operations):
    x = 0
    for op in operations:
        if '+' in op:
            x += 1
        else:
            x -= 1
    return x

"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A". 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""

def num_jewels_in_stones(jewels, stones):
    return sum(1 for s in stones if s in jewels)

"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

Example 1:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6

Example 2:
Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
"""

def most_words_found(sentences):
    num_words = [len(s.split(' ')) for s in sentences]
    return max(num_words)

"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G",
"()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o",
and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
Input: command = "G()(al)"
Output: "Goal"

Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:
Input: command = "(al)G(al)()()G"
Output: "alGalooG"
"""

def interpret(command):
    for a, b in {"()":"o", "(al)":"al"}.items():
        command = command.replace(a, b)
    return command

"""
You are given a string s and an integer array indices of the same length. The string s will be shuffled such
that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
"""

def restore_string(s, indices):
    restored = [None] * len(indices)
    n = 0
    for i in indices:
        restored[i] = s[n]
        n += 1
    return ''.join(restored)