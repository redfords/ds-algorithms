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
