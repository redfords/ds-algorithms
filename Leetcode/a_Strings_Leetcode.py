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

"""
A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:

<col> denotes the column number c of the cell. It is represented by alphabetical letters.
<row> is the row number r of the cell. The rth row is represented by the integer r.
You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1,
<row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.

Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be represented as strings in the
format mentioned above and be sorted in non-decreasing order first by columns and then by rows.

Example 1:
Input: s = "K1:L2"
Output: ["K1","K2","L1","L2"]
"""

def cells_in_range(s):
    cells = []
    c1 = ord(s[0])
    c2 = ord(s[3])+1
    r1 = int(s[1])
    r2 = int(s[4])+1
    for i in range(c1, c2):
        for n in range(r1, r2):
            cells.append(chr(i) + str(n))
    return cells

"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
"""

def balanced_string_split(s):
    pass

"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively.
The steps to decode message are as follows:
Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.

Example 1:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
"""

def decode_message(key, message):
    new_key = ''
    check = set()
    for k in key:
        if k != ' ' and k not in check:
            new_key += k
            check.add(k)
    decoded = ''
    for m in message:
        if m != ' ':
            i = new_key.index(m)
            decoded += chr(i+97)
        else:
            decoded += ' '
    return decoded

"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example 1:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
"""

def sort_sentence(s):
    sentence = ''
    words = s.split()

    for i in range(1, len(words)+1):
        for w in words:
            if int(w[-1:]) == i:
                sentence += ' ' + w[:-1]
    return sentence.strip()

"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
"""

def check_if_pangram(sentence):
    # abc = set()
    # for n in range(97, 123):
    #     abc.add(chr(n))

    # for letter in abc:
    #     if letter not in sentence:
    #         return False
    # return True

    s = set(sentence)
    return len(s) == 26    
"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
"""

def array_strings_are_equal(word1, word2):
    return ''.join(word1) == ''.join(word2)

"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...".
We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
"""

def unique_morse_representations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    unique_words = {
        "".join(morse[ord(c) - 97] for c in word)
        for word in words
    }
    return len(unique_words)

"""
Given a VPS represented as string s, return the nesting depth of s.

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
"""

def max_depth(s):
    depth = 0
    open = 0
    for c in s:
        if c == '(':
            open += 1
            depth = max(depth, open)
        if c == ')':
            open -= 1
    return depth

"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s and an integer k. You want to truncate s such that it contains only the first k words. Return s after truncating it.

Example 1:
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
"""

def truncate_sentence(s, k):
    s = s.split()
    return ' '.join(s[:k])

"""
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.

Example 1:
Input: s = "l|*e*et|c**o|*de|"
Output: 2
"""

# def count_asterisks(s):
#     a = 0
#     bar = 0
#     for ch in s:       
#         if ch == '|':
#             bar += 1
#         if bar % 2 == 0 and ch == '*':
#             a += 1
#     return a


def count_asterisks(s):
    return sum([a.count('*') for a in s.split('|')][0::2])

"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"
"""

def to_lower_case(s):
    return ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s)

"""
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
"""

def count_consistent_strings(allowed, words):
    cons = 0
    for word in words:
        is_cons = True
        for ch in word:
            if ch not in allowed:
                is_cons = False
                break
        if is_cons:
            cons += 1
    return cons

"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

def reverse_words(s):
    return " ".join(word[::-1] for word in s.split())

"""
There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

You are given a string rings of length 2n that describes the n rings that are placed onto the rods.
Every two characters in rings forms a color-position pair that is used to describe each ring where:

The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2,
and a blue ring placed onto the rod labeled 1.

Return the number of rods that have all three colors of rings on them.

Example 1:
Input: rings = "B0B6G0R6R0R6G9"
Output: 1
"""

def count_points(rings):
    rods = {rings[i] for i in range(1, len(rings), 2)}
    return sum(all(color + rod in rings for color in 'RGB')
        for rod in rods)

"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.

Example 1:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
"""

def sort_people(names, heights):
    # sorted_heights = sorted(heights,reverse=True)
    # return [names[heights.index(i)] for i in sorted_heights]    

    return [b for a, b in sorted(zip(heights, names), reverse=True)]

"""
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
"""

def remove_outer_parentheses(s):
    res = ''
    count = 0
    for i in range(len(s)):
        if s[i] == '(' and count == 0:
            count += 1
        elif s[i] == '(' and count >= 1:
            res += s[i]
            count += 1
        elif s[i] == ')' and count > 1:
            res += s[i]
            count -= 1
        elif s[i] == ')' and count == 1:
            count -= 1
    return res
        

