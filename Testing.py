from Coursera import a_Strings_Coursera as a
import sys
import traceback

if __name__=="__main__":
    try:
        str = 'X-DSPAM-Confidence:0.8475'
        a.convert_to_float(str)

        str = ['candy', 'x', 'not bad', 'note']
        for s in str:
            a.not_string(s)

        str = ['Java', 'Chocolate', 'abc']
        for s in str:
            a.front3(s)
        
        str = 'Hi'
        n = 3
        a.string_times(str, n)

        str = ['Java', 'Chocolate', 'abc']
        for s in str:
            a.front_times(s, n)

        str = 'Heeololeo'
        a.string_bits(str)

        str = 'Hi-There'
        a.double_char(str)

        str = 'hiABChi hi'
        print(a.count_hi(str))

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()