import a_Arrays_Hashing as a
import sys
import traceback

def a_strings():
    nums = [1,2,3,4]
    # nums = [1,1,1,3,3,4,3,2,4,2,5]
    result = a.contains_duplicate(nums)

    print(result)

if __name__=="__main__":
    try:
        a_strings()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()