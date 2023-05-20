import sys, traceback

class bcolors:
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def _check_file(path, header, delimiter):
    errors = list()

    with open(path, "r") as file:
        lines = file.readlines()

        # Get number of columns from first line
        try:
            num_cols = len(lines[0].split(delimiter))
            if num_cols == 1:
                errors.append("First line with no delimiters!")
        except:
            print("File is empty")

        line_count = 0

        for line in lines:
            line_count += 1
            
            if line.strip() == "":
                errors.append("Line break! At line " + str(line_count))
            
            elif len(line.split(delimiter)) != num_cols:
                errors.append("No same amount of columns! At line " + str(line_count))

        if header == "h":
            line_count -= 1

    file.close()

    return [errors, line_count]

if __name__ == "__main__":
    try:
        path = sys.argv[1]
        header = sys.argv[2]
        delimiter = sys.argv[3]

        result = _check_file(path, header, delimiter)

        if not result[0]:
            print(bcolors.OK_GREEN + "SUCCESS! The file is OK!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "WARNING! The file is NOT OK!" + bcolors.ENDC)
            print("")
            print("Errors detected: ")
            for r in result[0]:
                print(r)
        
        print("")
        print("COUNTS:")
        print("The file has {0} records.".format(result[1])) 
        print("")

    except Exception as e:
        print(e)
        traceback.print_exc()
        sys.exit(OSError)