import sys, traceback

class bcolors:
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def _check_file(path,header,delimiter):

    with open(path, "r") as file:
        lines = file.readlines()

if __name__ == "__main__":
    try:
        path = sys.argv[1]
        header = sys.argv[2]
        delimiter = sys.argv[3]

        result = _check_file(path,header,delimiter)
        print(result)

        # if (result[0]==3):
        #     print(bcolors.OK_GREEN + "SUCCESS! The file is OK!" + bcolors.ENDC)
        # else:
        #     print(bcolors.FAIL + "WARNING! The file is NOT OK!" + bcolors.ENDC)
        #     print("")
        #     print("Errors detected: ")
        #     print(result[1])

    except Exception as e:
        print(e)
        traceback.print_exc()
        sys.exit(OSError)