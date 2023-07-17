#plfileok.py (v 1.4)
#Script to check initial requirements and formats of a file before processing it an sending it to RAW (Landing File OK).
#It will show the amount of records at the end also.
#It will check if headers and fields are the same amount, if delimiters are OK, if there is no line breaks.
#It will estimate if the encoding is OK.
#It will also test gzip files.

#Dependencias
import os, sys, traceback, chardet, gzip

#Constants
class bcolors:
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#Functions
def _file_is_empty(path):
    return os.stat(path).st_size==0

def _fw_process_iteration(file_to_check,header):
    
    all_tests_OK=False
    errors=[]
    no_break_lines=True
    chars_amt_ok=True

    line_counting=0
    lines = file_to_check.readlines()

    amount_regs=len(lines)
    if (header=='h'):
        amount_regs = str(int(amount_regs)-1)
        
    chars_amt=len(lines[0])

    for line in lines:
        line_counting+=1
        if (len(line.strip())==0):
            no_break_lines=False
            errors.append("Line break! At line "+str(line_counting))
        else:
            if(len(line)!=chars_amt):
                chars_amt_ok=False
                errors.append("No same amount of chars! At line "+str(line_counting))
            else:
                chars_amt=len(line)
        
    file_to_check.close()
    
    all_tests_OK=chars_amt_ok+1+no_break_lines
    return [all_tests_OK,errors,amount_regs]

def _check_fixed_width_file(path_file,header,isgzip):
    
    print("")
    print("---------------------------------------------------------------------")
    print("________________( Checking file with fixed width... )________________")
    print("---------------------------------------------------------------------")
    print("")

    if isgzip=='gzip':
       file_to_check=gzip.open(path_file, "r")
       return _fw_process_iteration(file_to_check,header)
    else:
        with open(path_file, "r") as file_to_check:
            return _fw_process_iteration(file_to_check,header) 

def _delim_process_iteration(file_to_check,header,delimiter):
    all_tests_OK=False
    errors=[]
    fields_amt_ok=True
    delimiter_ok=True
    no_break_lines=True

    line_counting=0
    lines = file_to_check.readlines()

    amount_regs=len(lines)
    if (header=='h'):
        amount_regs = str(int(amount_regs)-1)
        
    fields_amt=len(str(lines[0]).split(delimiter))
        
    #First it checks at least 2 records delimited
    if (fields_amt<2):
        delimiter_ok=False
        errors.append("First line with no delimiters!")
    else:
        for line in lines:
            line_str=str(line)
            line_counting+=1
            if (len(line_str.strip())==0):
                no_break_lines=False
                errors.append("Line break! At line "+str(line_counting))
            else:
                if(len(line_str.split(delimiter))!=fields_amt):
                    fields_amt_ok=False
                    errors.append("No same amount of fields! At line "+str(line_counting))
                else:
                    fields_amt=len(line_str.split(delimiter))
        
    file_to_check.close()
    all_tests_OK=fields_amt_ok+delimiter_ok+no_break_lines
    return [all_tests_OK,errors,amount_regs]

def _check_planding_file_ok(path_file,header,delimiter,width,enc,isgzip):
    
    #Check empty file
    if _file_is_empty(path_file):
        return [0,['Empty file!!'],0] 

    #Check corrupted chars (encoding ok)
    if enc=='enc':
        with open(path_file, 'rb') as file_check_encode:
            result = chardet.detect(file_check_encode.read())
            print("")
            print("Checking encoding...")
            print(str(result))    
            print("")
            file_check_encode.close()

        if float(result.get('confidence'))<0.3:
            return [0,['Bad encoding! Less than 0.3!!'],0]

    if width=='fw':
        return _check_fixed_width_file(path_file,header,isgzip)

    print("")
    print("--------------------------------------------------------------------")
    print("________________( Checking file with delimiters... )________________")
    print("--------------------------------------------------------------------")
    print("")

    if isgzip=='gzip':
       file_to_check=gzip.open(path_file, "r")
       return _delim_process_iteration(file_to_check,header,delimiter)
    else:
        with open(path_file, "r") as file_to_check:
            return _delim_process_iteration(file_to_check,header,delimiter)    
       

#Execution
if __name__=="__main__":
   try:
       #Receives as params path file, header or not, valid delimiter, if it is fixed width or not (fw or nfw),
       # check enc or not (enc or nenc) and if is gzip or not (gzip or ngzip) 
       #Example1: python plfileok.py /home/csvs/creditcards20230405.csv h "|" nfw enc ngzip
       #Example2: python plfileok.py /home/dats/mlmovements20220311.dat nh no fw enc ngzip
       #Example3: python plfileok.py /home/dats/tlmovements20211321.dat h "-" nfw nenc gzip
       print("")
       print(">>>>>>>----------------( Pre Landing Files OK 1.4 )----------------<<<<<<<")
       print("")

       path_file = sys.argv[1]
       header = sys.argv[2]
       delimiter = sys.argv[3]
       width=sys.argv[4]
       enc=sys.argv[5]
       isgzip=sys.argv[6]

       print("---> Starting File Check...")
       print("")
       result = _check_planding_file_ok(path_file,header,delimiter,width,enc,isgzip)

       if (result[0]==3):
           print(bcolors.OK_GREEN + "SUCCESS! The file is OK!" + bcolors.ENDC)
       else:
           print(bcolors.FAIL + "WARNING! The file is NOT OK!" + bcolors.ENDC)
           print("")
           print("Errors detected ({0}): ".format(len(result[1])))
           print(result[1])
       
       print("")
       print("COUNTS:")
       print("The file has {0} records.".format(result[2])) 
       print("")

       
   except Exception as e:
       print("There was a problem running the script!! " + str(e))
       traceback.print_exc()
       print("--------------------------------------(HELP)-----------------------------------------")
       print("If you have trouble running the script, remember this is the command to execute it: ")
       print('        python pl_file_ok.py <file path> <h or nh> <delimiter> <fixed width or not>')
       print("For example: ")
       print('        python plfileok.py /home/csvs/creditcards20230405.csv h "|" nfw enc ngzip')
       print('        python plfileok.py /home/dats/mlmovements20220311.dat nh no fw enc ngzip')
       print('        python plfileok.py /home/dats/mlmovements20220311.dat nh no fw enc ngzip')
       print('        python plfileok.py /home/dats/tlmovements20211321.dat h "-" nfw nenc gzip')
       print('')
       print('WARNING! If you make a mistake in the args input and you enter a valid delimiter but')
       print('you do not put fixed width with "no" but with "fw" the script will consider your file as fw one!')
       print('')
       print("-------------------------------------------------------------------------------------")
       sys.exit(os.EX_IOERR)
