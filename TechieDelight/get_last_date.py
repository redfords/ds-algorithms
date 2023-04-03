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

def _get_table_max_process_date(table_location):
        
        cmd = "hdfs dfs -ls %s" % (table_location)
        files = subprocess.check_output(cmd, shell=True).strip().split('\n')
        for path in files:
            print(path)
        #path_table = 'hdfs://' + outdat + '/spin_off/spin_off_reborn_{}_{}'.format(entity, fecha_extract)
        #parseo.coalesce(1).write.option("sep", "|").format("com.databricks.spark.csv").option("header", "false").option(
        #            "ignoreLeadingWhiteSpace", "false").option("ignoreTrailingWhiteSpace", "false").mode("append").save(path_spin_off)

        #print("El spinoff de fecha: {} y entidad: {} se genero correctamente".format(fecha_extract, entity))
        return ""

def _get_table(tables, server):
     pass

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