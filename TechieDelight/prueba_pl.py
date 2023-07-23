import sys, gzip, os, traceback
# import cchardet as chardet

class bcolors:
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def _delim_process_iter(file, header, delimiter):
    errors = list()
    n_line = 0
    lines = file.readlines()
    line_count = len(lines)
    if (header == 'h'): line_count -= 1
    num_cols = len(str(lines[0]).split(delimiter))
    if (num_cols == 1):
        errors.append("First line with no delimiters!")
    else:
        for line in lines:
            line_str = str(line)
            n_line += 1
            if (len(line_str.strip())==0):
                errors.append("Line break! At line " + str(n_line))
            else:
                if(len(line_str.split(delimiter)) != num_cols):
                    errors.append("No same amount of fields! At line " + str(n_line))
    return [errors, line_count]

def _fw_process_iter(file, header):
    errors = list()
    n_line = 0
    lines = file.read().splitlines()
    line_count = len(lines)
    if (header == 'h'): line_count -= 1
    char_count = len(lines[0])
    for line in lines:
        n_line += 1
        if (len(line.strip()) == 0):
            errors.append("Line break! At line " + str(n_line))
        else:
            if(len(line) != char_count):
                errors.append("No same amount of chars! At line " + str(n_line))
    return [errors, line_count]

def _read_file(file, header, delimiter, width):
    if width == "fw":
        return _fw_process_iter(file, header)
    else:
        return _delim_process_iter(file, header, delimiter)
    
# def _get_encoding(path):
    # try:
        # with gzip.open(path, 'rb') as file:
            # return chardet.detect(file.read())
    # except:
        # with open(path, 'rb') as file:
            # return chardet.detect(file.read())

def _check_planding_file(path, header, delimiter, width):
    # check if file is empty
    if not os.stat(path).st_size:
        return [['Empty file!!'], 0]
    
    # check file encoding
    # print("Checking encoding...")
    # encoding = _get_encoding(path)
    # print(encoding, '\n')
    # if float(encoding.get('confidence')) < 0.3:
        # return [['Bad encoding! Less than 0.3!!'], 0]
    
    # get no. of records and check line by line
    try:
        with gzip.open(path, 'r') as file:
            return _read_file(file, header, delimiter, width)
    except:
        with open(path, "rb") as file:
            return _read_file(file, header, delimiter, width)

if __name__=="__main__":
    try:
        path = sys.argv[1]
        header = sys.argv[2]
        delimiter = sys.argv[3]
        width = sys.argv[4]
        print("---> Starting File Check...\n")
        result = _check_planding_file(path, header, delimiter, width)
        if (result[0]):
            print(bcolors.FAIL + "WARNING! The file is NOT OK!\n" + bcolors.ENDC)
            print("Errors detected ({0}): ".format(len(result[0])))
            print(("\n").join(result[0]), "\n")
        else:
            print(bcolors.OK_GREEN + "SUCCESS! The file is OK!\n" + bcolors.ENDC)
        print("COUNTS:")
        print("The file has {0} records.\n".format(result[1])) 
    except Exception:
        print("There was a problem running the script!!\n")
        traceback.print_exc()
        print("\nRun with the following arguments:\n"
              "python3 pl_file_ok.py <file path> <h or nh> <delimiter> <fw or nfw>\n")
        sys.exit(1)
