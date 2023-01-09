from Coursera import a_Strings_Coursera as a
import sys
import traceback

if __name__=="__main__":
    try:
        str = 'X-DSPAM-Confidence:0.8475'
        a.convert_to_float(str)

        str = ['candy', 'x', 'not bad', 'note']
        for s in str:
            print(a.not_string(s))

        str = ['Java', 'Chocolate', 'abc']
        for s in str:
            print(a.front3(s))
        


    except Exception as e:
        print(traceback.format_exc())
        sys.exit()