import a_Strings_Leetcode as a
import sys
import traceback

def a_strings():
    str = "255.100.50.0"
    a.defang_ip_addr(str)

if __name__=="__main__":
    try:
        a_strings()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()