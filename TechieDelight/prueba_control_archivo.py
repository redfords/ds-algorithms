import traceback, sys, os

class bcolors:
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def _check_file(path_file, header, delimiter):
    errors = list()

    with open(path_file, "r") as file:

        lines = file.readlines()
        line_count = 0

        try:
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
                
            if header == "h":
                    line_count -= 1
            
        except:
            errors.append("File is empty")
        
    file.close()
    return [errors, line_count]

if __name__ == "__main__":

    try:
        path_file = sys.argv[1]
        header = sys.argv[2]
        delimiter = sys.argv[3]

        result = _check_file(path_file, header, delimiter)

        if not result[0]:
            print(bcolors.OK_GREEN + "SUCCESS! The file is OK!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "WARNING! The file is NOT OK!" + bcolors.ENDC)
            
            for line in result[0]:
                print(line)
        print("Cent. de registros: " + str(result[1]))
        


    except Exception as e:
        traceback.print_exc()
        print(e)
        sys.exit(os.EX_IOERR)