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

"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def two_sum(nums, target):
    check_num = dict()

    for i, n in enumerate(nums):
        diff = target - n
        if diff in check_num:
            return [check_num[diff], i]
        check_num[n] = i
    
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]

"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

def is_palindrome(x):
    if x < 0:
        return False
    
    div = 1
    while x >= 10 * div:
        div *= 10
    
    while x:
        right = x % 10
        left = x // div
        
        if left != right:
            return False

        x = (x % div) // 10
        div = div / 100

    return True
    
    # num = str(x)
    # return num == num[::-1]

"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

def longest_common_prefix(strs):
    prefix = ''
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]