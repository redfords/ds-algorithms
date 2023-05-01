import sys, traceback
from subprocess import PIPE, Popen

def _get_lineas(data_path):

    file = Popen(["hadoop", "fs", "-cat", data_path], stdout=PIPE)
    n_line = 0
    total = 0
    
    for line in file.stdout:
        new_line = line.strip().replace('|', '').replace('"', '')
        n_line += 1
        if len(new_line) != 908:
            print('Linea con problema: {}'.format(n_line))
            print('Largo: {}'.format(len(new_line)))
            print(new_line)
            print('Linea original:')
            print(line)
            total += 1

    print('Total lineas con problema: {}'.format(total))

if __name__ == "__main__":
    try:
        data_path = sys.argv[1]
        _get_lineas(data_path)

    except Exception as e:
        print(e)
        traceback.print_exc()
        sys.exit(OSError)