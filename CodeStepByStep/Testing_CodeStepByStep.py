import a_Strings_CodeStepByStep as a
import sys
import traceback

def a_strings():
    str = '12345678'
    a.add_commas(str)

    str = 'abcdefghghghghghgh.'
    substr = 'ghg'
    a.occ_str(str, substr)


if __name__=="__main__":
    try:
        a_strings()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()