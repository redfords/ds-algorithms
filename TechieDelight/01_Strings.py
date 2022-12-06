import datetime
import paramiko
import sys, os, re

class SystemFiles():
    def get_files(self, entidad):
        files = list()
        # path = "/home/goa/{}/link/transacciones_prima".format(entidad)
        path = "/files"
        patter = re.compile('((\d{8})+.txt)')

        for r, d, f in os.walk(path):
            for file in f:
                print(file)
        return files

class Utils():
    def get_last_month(self):
        today = datetime.date.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        return last_month
    
    def get_date_range(self):
        pass

entidad = sys.argv[1]

lista_archivos = SystemFiles()
utilidades = Utils()

lista_archivos = lista_archivos.get_files(entidad)



path = "./files"
filename = '{}_omni_extract_'.format(entidad)
patter = re.compile(filename + '(\d{8}).txt')
for r, d, f in os.walk(path):
    for file in f:
        try:
            dates = patter.search(os.path.join(path,file)).group(1)
            print(dates)
        except:
            continue
    