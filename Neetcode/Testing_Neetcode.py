import a_Arrays_Hashing as a
import sys
import traceback

def a_strings():
    nums = [1,2,3,4]
    # nums = [1,1,1,3,3,4,3,2,4,2,5]
    a.contains_duplicate(nums)

    # s = "anagram"
    # t = "nagaram"
    s = "srats"
    t = "scars"
    a.is_anagram(s, t)

    nums = [2,7,11,15]
    target = 9
    # nums = [3,2,4]
    # target = 6
    # nums = [3,3]
    # target = 6
    a.two_sum(nums, target)

    x = 121
    # x = -121
    a.is_palindrome(x)

    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    return a.longest_common_prefix(strs)

if __name__=="__main__":
    try:
        result = a_strings()
        print(result)

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()