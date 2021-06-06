"""
Running Sum of 1d Array
Given an array nums. We define a running sum as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

def runningSum(nums):
    nums_sum = list()
    for index in range(1, len(nums) + 1):
        nums_sum.append(sum(nums[: index]))
    return nums_sum

"""
Shuffle the Array
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
"""

def shuffle(nums, n):
    newindex = 1
    for index in range(n, len(nums)):
        nums.insert(newindex, nums.pop(index))
        newindex += 2
    return nums    

"""
Richest Customer Wealth
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest
customer is the customer that has the maximum wealth.

Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""

def maximumWealth(accounts):
    sum_accounts = list()
    for account in accounts:
        sum_accounts.append(sum(account))
    return max(sum_accounts)

# using list comprehension
def maximumWealth(accounts):
    sum_accounts = [sum(i) for i in accounts]
    return max(sum_accounts)

accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))