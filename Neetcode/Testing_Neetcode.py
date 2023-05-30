import a_Arrays_Hashing as a
import sys
import traceback

def a_strings():
    nums = [1,2,3,4]
    # nums = [1,1,1,3,3,4,3,2,4,2,5]
    a.contains_duplicate(nums)

    # s = "anagram"
    # t = "nagaram"
    s = "rat"
    t = "car"

    return a.is_anagram(s, t)

if __name__=="__main__":
    try:
        result = a_strings()
        print(result)

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()