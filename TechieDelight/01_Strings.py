import datetime
import sys, os, re

class SystemFiles():
    def get_files(self, entidad):
        # path = "/home/goa/{}/link/transacciones_prima".format(entidad)
        filename = '{}_omni_extract_'.format(entidad)
        patter = re.compile(filename + '(\d{8}).txt')
        files_in_server = list()
        for r, d, f in os.walk(path):
            for name in f:
                try:
                    file = patter.search(os.path.join(path,name)).group(1)
                    files_in_server.append(file)
                except:
                    continue
        return files_in_server

class Utils():
    def get_last_month(self):
        today = datetime.date.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        return last_month
     
    def get_date_range(self, last_month):
        date_range = list()
        year_month = last_month.strftime("%Y%m")
        
        for d in range(1, last_month.day + 1):
            date_range.append(year_month + str('%02d' % d))
        return date_range

entidad = sys.argv[1]

system_files = SystemFiles()
utilidades = Utils()

last_month = utilidades.get_last_month()
date_range = utilidades.get_date_range(last_month)

files_in_server = system_files.get_files(entidad)

for date in date_range:
    if date not in files_in_server:
        print(date)