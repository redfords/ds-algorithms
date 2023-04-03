#Script de PySpark para obtener la fecha de proceso maxima de una tabla

import sys,traceback,os,subprocess
from pyspark.sql import SparkSession

def _setSparkSession(entidad,fechaextract):
    spark = SparkSession\
        .builder\
        .appName("Omni Find Last Process Dates ({0} - {1})".format(entidad,fechaextract))\
        .enableHiveSupport()\
        .master("local[2]")\
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    return spark

def _get_table_max_process_date(location):
    cmd = "hdfs dfs -ls %s" % (location)
    files = subprocess.check_output(cmd, shell=True).strip().split('\n')
    dates = [path[-8:] for path in files[1:]]
    return max(dates)

def _get_table(tables, server):
    for table in tables[1:]:
        t = table.split(";")
        alias = t[0]
        location = server + t[1]
        print("Tabla: "+alias+", Max fecha_proceso: "+_get_table_max_process_date(location))

#Execution
if __name__=="__main__":
   try:
       #Recibe por parametro la location de la tabla y su alias
        server=sys.argv[1]
        tables=sys.stdin.read().splitlines()

        _get_table(tables, server)
       
   except Exception as e:
       print("There was a problem getting the max process date!! "+str(e))
       print(traceback.print_exc())
       traceback.print_exc()
       sys.exit(os.EX_IOERR)