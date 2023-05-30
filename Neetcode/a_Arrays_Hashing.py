"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

def contains_duplicate(nums):
    distinct = set()
    for num in nums:
        if num in distinct:
            return True
        distinct.add(num)
    return False

    # distinct = set(nums)
    # return len(nums) != len(distinct)

"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    count_s = dict()
    count_t = dict()

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    return count_s == count_t


    # for c in s:
    #     if c in t:
    #         t = t.replace(c, '', 1)
    #     else:
    #         return False
    # return len(t) == 0