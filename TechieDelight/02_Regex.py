from pyspark.sql import SparkSession
import re

def _set_spark_session(entidad, fecha):
    spark = SparkSession\
        .builder\
        .appName("Omni Second Ref ({0} - {1})".format(entidad, fecha))\
        .enableHiveSupport()\
        .master("local[2]")\
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

    return spark

def _format_monto(monto):
    if re.match("^\d+?\.\d+?$", monto) is not None:
        return str(monto)
    output = ''
    last_char = monto[-1]
    valor = {
        '0': '{',
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H',
        '9': 'I'
    }[last_char]
    output = monto[:-1] + valor
    return output

    