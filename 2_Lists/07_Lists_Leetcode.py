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

"""
Kids With the Greatest Number of Candies
Easy

865

197

Add to List

Share
Given the array candies and the integer extraCandies, where candies[i] represents the number of
candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or
she can have the greatest number of candies among them. Notice that multiple kids can have the
greatest number of candies.

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies.
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number.
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number.
"""

def kidsWithCandies(candies, extraCandies):
    max_candies = list()
    for c in candies:
        if c + extraCandies >= max(candies):
            max_candies.append(True)
        else:
            max_candies.append(False)
    return max_candies

# using list comprehension
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [True if (x + extraCandies) >= max_candies else False for x in candies]

"""
Number of Good Pairs
Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
"""

def numIdenticalPairs(nums):
    pair = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                pair += 1
    return pair

"""
How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and
nums[j] < nums[i].
Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
"""

def smallerNumbersThanCurrent(nums):
    smaller = list()
    for index in range(len(nums)):
        count = 0
        for n in nums[: index] + nums[index + 1 :]:
            if n < nums[index]:
                count += 1
        smaller.append(count)
    return smaller

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))