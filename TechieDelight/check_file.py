import sys, traceback

class bcolors:
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def _check_file(path,header,delimiter):

    errors = list()

    with open(path, "r") as file:
        lines = file.readlines()

        num_lines = len(lines)

        num_cols = len(lines[0].split(delimiter))

        line_count = 0
        for line in lines:
            line_count += 1
            if line.strip() == "":
                errors.append("Line break! At line " + str(line_count))
            elif len(line.split(delimiter)) != num_cols:
                errors.append("No same amount of records! At line " + str(line_count))
    
        print(header, delimiter)
        print(num_lines, num_cols)

    file.close()

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