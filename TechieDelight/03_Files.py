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
    name_cde = {
            "bsf": "0071",
            "ber": "0386",
            "bsc": "0086",
            "bsj": "0045"
    }
    name = name_cde.get(entidad)

    def _sql_from_ref(spark,subent,entity,fecha_extract):
        pass

    def _format_monto(monto):
        pass

    def _reverse_format_monto(montoStr):
        pass

    def _generate_spin_off(final_data,fecha_extract,entity,outdat):
        pass

    def _generate_header_trailer(final_df,fecha_extract,name):
        pass

    def _header_and_trailer(final_df,fecha_extract,name,entity,outdat):
        pass



if __name__=="__main__":

    sys.setdefaultencoding = "utf-8"

    try:
        params = sys.argv[2].split("-")
        fecha = params[0].lower()
        fext = fecha[2:8]
        entidad = params[1].lower()
        entorno = sys.argv[1].lower()
        subent = entorno[0:2]

        spark = _set_spark_session(entidad, fecha)

        execute(spark, fecha, fext, entidad, entorno, subent)

    except Exception as e:
        print("Error de ejecucion! "+str(e))
        sys.exit(os.EX_IOERR)