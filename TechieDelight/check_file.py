import sys, traceback, os, chardet

class bcolors:
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def _check_file(path, header, delimiter):
    errors = list()
    line_count = 0

    with open(path, 'rb') as file:
        result = chardet.detect(file.read())
        print(result)

    if result.get('confidence') < 0.3:
        errors.append('Bad encoding! Less than 0.3!!')
        return [errors, line_count]

    with open(path, "r") as file:
        lines = file.readlines()

        # Get number of columns from first line
        if lines:
            num_cols = len(lines[0].split(delimiter))

            if num_cols == 1:
                errors.append("First line with no delimiters!")
                line_count = len(lines)
                     
            else:
                for line in lines:
                    line_count += 1
                    
                    if line.strip() == "":
                        errors.append("Line break! At line " + str(line_count))
                    
                    elif len(line.split(delimiter)) != num_cols:
                        errors.append("No same amount of columns! At line " + str(line_count))

            if header == "h" and line_count > 0:
                line_count -= 1

        else:
            errors.append("File is empty")

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
        print("There was a problem running the script!! " + str(e))
        print("")
        traceback.print_exc()
        print("")
        print("--------------------------------------(HELP)-----------------------------------------")
        print("If you have trouble running the script, remember this is the command to execute it: ")
        print('        python plfileok.py <file path> <h or nh> <delimiter>')
        print("For example: ")
        print('        python plfileok.py /home/csvs/creditcards20230405.csv h "|"')
        print("-------------------------------------------------------------------------------------")
        sys.exit(os.EX_IOERR)