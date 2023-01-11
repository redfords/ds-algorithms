import a_Lists_HackerRank as a
import sys
import traceback

def a_strings():
    str = [1, 2, 3, 4, 5]
    print(a.reverse_array(str))


if __name__=="__main__":
    try:
        a_strings()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()