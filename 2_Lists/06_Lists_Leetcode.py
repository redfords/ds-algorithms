from functools import reduce
from itertools import accumulate

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
        for j in range(i + 1, len(arr) + 1, 2):
            arr_sum += sum(arr[i : j])
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

"""
Find the Highest Altitude
There is a biker going on a road trip. The road trip consists of n + 1 points at different
altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude
between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
"""

def largestAltitude(gain):
    return max(accumulate([0] + gain))

"""
Flipping an Image
Given an n x n binary matrix image, flip the image horizontally, then invert it.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].
 
Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""

def flipAndInvertImage(image):
    reverse = list()
    replace = {0: 1, 1: 0}
    # for row in image:
    #     reverse.append([replace.get(x, x) for x in row][: : -1])

    return [[replace.get(x, x) for x in row][: : -1] for row in image]

"""
Cells with Odd Values in a Matrix
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where
each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations
on the matrix.

For each location indices[i], do both of the following:
Increment all the cells on row ri.
Increment all the cells on column ci.

Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the
increment to all locations in indices.
"""

def oddCells(m, n, indices):
    row = [0] * m
    col = [0] * n

    for x,y in indices:
        row[x] += 1
        col[y] += 1
        
    odd = 0
    for i in range(m):
        for j in range(n):   
            if (row[i] + col[j]) % 2:
                odd += 1
    return odd

# m = 2
# n = 3
# indices = [[0,1],[1,1]]
# print(oddCells(m, n, indices))

"""
Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.
"""

def findNumbers(nums):
    return sum(len(str(n)) % 2 == 0 for n in nums)

"""
Minimum Operations to Make the Array Increasing
You are given an integer array nums (0-indexed). In one operation, you can choose an element of
the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An
array of length 1 is trivially strictly increasing.

Example 1:
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].

Example 2:
Input: nums = [1,5,2,4,1]
Output: 14
"""

def minOperations(nums):
    ops = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] <= nums[i]:
            diff = nums[i] - nums[i + 1] + 1
            nums[i + 1] += diff
            ops += diff
    return ops

# nums = [1,5,2,4,1]
# print(minOperations(nums))

"""
Maximum Product of Two Elements in an Array
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum
value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""

def maxProduct(nums):
    i = max(nums)
    nums.pop(nums.index(i))
    j = max(nums)
    return (i - 1) * (j - 1)

"""
Number of Students Doing Homework at a Given Time
Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started their homework at the time startTime[i] and finished it at time endTime[i].
Return the number of students doing their homework at time queryTime. More formally, return the
number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

Example 1
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
"""

def busyStudent(startTime, endTime, queryTime):
    return sum(queryTime in range(startTime[i], endTime[i] + 1) for i in range(len(startTime)))

# startTime = [9,8,7,6,5,4,3,2,1]
# endTime = [10,10,10,10,10,10,10,10,10]
# queryTime = 5

# print(busyStudent(startTime, endTime, queryTime))

"""
Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]
"""

def sumZero(n):
    if n % 2 == 0:
        return [i for i in range(1, n, 2)] + [-i for i in range(1, n, 2)]
    return [i for i in range(1, n, 2)] + [-i for i in range(1, n, 2)] + [0]

"""
Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

def countNegatives(grid):
    return sum(n < 0 for sub in grid for n in sub)

"""
Sort Array By Parity
Given an array nums of non-negative integers, return an array consisting of all the even
elements of nums, followed by all the odd elements of nums.
 
Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

def sortArrayByParity(nums):
    return [n for n in nums if n % 2 == 0] + [n for n in nums if n % 2 != 0]

"""
Final Prices With a Special Discount in a Shop
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special
discount for items in the shop, if you buy the ith item, then you will receive a discount
equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i],
otherwise, you will not receive any discount at all.
Return an array where the ith element is the final price you will pay for the ith item of the shop
considering the special discount.

Example 1:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
"""

def finalPrices(prices):
    final = list()
    discount = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                discount = prices[j]
                break;
        final.append(prices[i] - discount)
        discount = 0
    return final

"""
Sum of Unique Elements
You are given an integer array nums. The unique elements of an array are the elements that appear
exactly once in the array.
Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
"""

def sumOfUnique(nums):
    return sum([n for n in nums if nums.count(n) == 1])

"""
Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the
elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""

def replaceElements(arr):
    for i in range(len(arr)):
        right = arr[i + 1 :]
        if not right:
            arr[i] = -1
        else:
            arr[i] = max(right)
    return arr

"""
Array Partition I
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),
..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6).
min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
"""

def arrayPairSum(nums):
    nums = sorted(nums, reverse = True)
    return sum(nums[i] for i in range(1, len(nums), 2))

"""
Maximum Number of Balls in a Box
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit
inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1
to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits
of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6
and the ball number 10 will be put in the box number 1 + 0 = 1.

Return the number of balls in the box with the most balls.

Example 1:
Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
"""

def countBalls(lowLimit, highLimit):
    count = dict()
    for n in range(lowLimit, highLimit + 1):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        count[r] = count.get(r, 0) + 1
    return max(count.values())

"""
Height Checker
A school is trying to take an annual photo of all the students. They are asked to stand in a
single file line in non-decreasing order by height. Let this ordering be represented by the
integer array expected where expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are
standing in. Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i].

Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
"""

def heightChecker(heights):
    expected = sorted(heights)
    return sum(heights[i] != expected[i] for i in range(len(heights)))

"""
Matrix Diagonal Sum
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the
secondary diagonal that are not part of the primary diagonal.

Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""

def diagonalSum(mat):
    total = 0
    k = len(mat) - 1
    for i in range(len(mat)):
        total += mat[i][i]
        total += mat[i][k] if k != i else 0
        k -= 1
    return total

"""
Make Two Arrays Equal by Reversing Sub-arrays
Given two integer arrays of equal length target and arr.
In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to
make any number of steps.
Return True if you can make arr equal to target, or False otherwise.

Example 1:
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
"""

def canBeEqual(target, arr):
    pass

target = [1,2,3,4]
arr = [2,4,1,3]
canBeEqual(target, arr)

"""
The K Weakest Rows in a Matrix
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing
civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will
appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
"""

def kWeakestRows(mat, k):
    soldiers = [row.count(1) for row in mat]
    order = sorted(range(len(soldiers)), key = lambda k: soldiers[k])
    return order[: k]

"""
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of
each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""

def sortedSquares(nums):
    return sorted([n ** 2 for n in nums])

"""
Sort Array By Parity II
Given an array of integers nums, half of the integers are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

def sortArrayByParityII(nums):
    odd = list()
    even = list()
    for n in nums:
        if n % 2 == 0:
            odd.append(n)
        else:
            even.append(n)
    return [i for sublist in zip(odd, even) for i in sublist]
