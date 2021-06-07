from functools import reduce

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

"""
Decompress Run-Length Encoded List
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate
all the sublists from left to right to generate the decompressed list.
Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
"""

def decompressRLElist(nums):
    decomp = list()
    for i in range(0, len(nums), 2):
        decomp += [nums[i + 1]] * nums[i]
    return decomp

"""
Create Target Array in the Given Order
Given two arrays of integers nums and index. Your task is to create target array under the
following rules:
Initially target array is empty. From left to right read nums[i] and index[i], insert at index
index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

Example 1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
"""

def createTargetArray(nums, index):
    order_nums = list()
    for i in range(len(nums)):
        order_nums.insert(index[i], nums[i])
    return order_nums

"""
Count Items Matching a Rule
You are given an array items, where each items[i] = [typei, colori, namei] describes the type,
color, and name of the ith item. You are also given a rule represented by two strings, ruleKey
and ruleValue.
The ith item is said to match the rule if one of the following is true:
ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

Example 1:
Input: items = [["phone","blue","pixel"],["laptop","silver","dell"],["phone","gold","iphone"]],
ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["laptop","silver","dell"].
"""

def countMatches(items, ruleKey, ruleValue):
    count = 0
    match = -1
        
    if ruleKey == "type":
        match = 0
    if ruleKey == "color":
        match = 1
    if ruleKey == "name":
        match = 2
        
    for item in items:
        if item[match] == ruleValue:
            count += 1
    return count

items = [["phone","blue","pixel"],["laptop","silver","dell"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

"""
XOR Operation in an Array
Given an integer n and an integer start.
Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.

Example 1:
Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
"""

def xorOperation(n, start):
    numbers = list()
    for num in range(start, start + (2 * n), 2):
        numbers.append(num)
    return reduce(lambda x, y: x ^ y, numbers)

"""
Sum of All Odd Length Subarrays
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
"""

def sumOddLengthSubarrays(arr):
    arr_sum = 0
    for i in range(len(arr)):
        j = i + 1
        while j <= len(arr):
            arr_sum += sum(arr[i : j])
            j += 2
    return arr_sum

"""
Count Good Triplets
Given an array of integers arr, and three integers a, b and c. You need to find the number of
good triplets. A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.
Return the number of good triplets.

Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
"""

def countGoodTriplets(arr, a, b, c):
    good_triplets = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j + 1, len(arr)):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c:
                        good_triplets += 1
    return good_triplets

# arr = [7,3,7,3,12,1,12,2,3]
# a = 5
# b = 8
# c = 1
# print(countGoodTriplets(arr, a, b, c))