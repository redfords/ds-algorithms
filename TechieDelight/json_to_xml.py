import sys, json, traceback

class NoGroupException(Exception):
    '''Raise when the group argument is missing'''

class NoPanException(Exception):
    '''Raise when the pan argument is missing'''

class TRXFormatNotValidException(Exception):
    '''Raise when the input is not json format'''

if __name__ == "__main__":
    sys.setdefaultencoding = "utf-8"

    try:
        group = sys.argv[1].lower()
    except:
        raise NoGroupException("Group must be the first argument.")
    try:
        pan_no = sys.argv[2].lower()
    except:
        raise NoPanException("Pan number must be the second argument.")
    try:
        with open('sample_trx.json') as file:
            trx = json.load(file)
    except:
        raise TRXFormatNotValidException("TRX Input content is not of valid json type.")
    try:
        print()
    except Exception as e:
        print("Json could not be created with input.")
        traceback.print_exc()
    


