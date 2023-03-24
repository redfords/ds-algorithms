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
    left = [0]
    right = [0]

    for num in nums[:-1]:
        left.append(left[-1] + num)

    for num in nums[::-1][:-1]:
        right.insert(0, right[0] + num)

    return [abs(left[i] - right[i]) for i in range(len(nums))]

"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

Input: nums = [1,2,2,1], k = 1
Output: 4
"""

def count_k_difference(nums, k):
    count = 0
    for i in range(len(nums)-1):
        n = nums[i]
        for x in nums[i+1:]:
            if abs(n - x) == k:
                count += 1
    return count

"""
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Input: grid = [
    [9,9,8,1],
    [5,6,2,6],
    [8,2,6,4],
    [6,2,2,2]]
Output: [[9,9],[8,6]]
"""

def largest_local(grid):
    for i in range(len(grid) - 2):
        print(i)
        for j in range(len(grid[0]) - 3):
            print(j)
            print(grid[i][j])
    