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
