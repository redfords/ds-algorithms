from pyspark.sql import SparkSession

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
    pass