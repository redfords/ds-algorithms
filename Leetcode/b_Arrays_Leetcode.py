"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]]
for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
"""

def build_array(nums):
    return [nums[i] for i in nums]

"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and
ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
"""

def get_concatenation(nums):
    return nums * 2

"""
You are given a positive integer array nums. The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Input: nums = [1,15,6,3]
Output: 9
"""

def difference_of_sum(nums):
    s = sum(nums)
    d = sum(int(d) for num in nums for d in str(num))
    return abs(s - d)

"""
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.

Where:
leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return the array answer.

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
"""

def left_rigth_difference(nums):
    pass