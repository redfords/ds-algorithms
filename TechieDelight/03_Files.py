from pyspark.sql import SparkSession
import sys

def _set_spark_session(entidad,fecha):
    spark = SparkSession\
        .builder\
        .appName("Omni Exctract Generator ({0} - {1})".format(entidad,fecha))\
        .enableHiveSupport()\
        .master("local[2]")\
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    return spark

def execute(spark, fecha, fext, entidad, entorno, subent):
    pass

if __name__=="__main__":

    sys.setdefaultencoding = "utf-8"