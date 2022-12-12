from pyspark.sql import SparkSession
import sys, os

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

    def _sql_from_ref(spark, subent, entity, fecha):
        final_data_df = spark.sql("""
            SELECT * FROM {0}_{1}_3ref.Can_Ges_Extract_Prima_Individuos_FT_Pre_Archivo
            WHERE t_cde in ("31", "2P", "28", "70", "61", "62", "18", "30", "40", "68",
            "34", "35", "37", "R2", "2H", "3H", "38","70", "OP", "F1", "F2")      
            AND fecha_proceso = {2}
        """.format(subent, entity, fecha)
        )

        return final_data_df

    def _format_monto(monto):
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

    def _reverse_format_monto(monto_str):
        print("ingreso a _reverse_format_monto")

        monto_str = str(monto_str)
        last_char = monto_str[-1]
        print("last_char:{}".format(last_char))
        valor = {
                '{': '0',
                'A': '1',
                'B': '2',
                'C': '3',
                'D': '4',
                'E': '5',
                'F': '6',
                'G': '7',
                'H': '8',
                'I': '9'
        }[last_char]
        output = monto_str[:-2] +"."+ monto_str[-2] + valor
        print("output:{}".format(output))
        return output

    def _generate_spin_off(final_data, fecha_extract, entity, outdat):
        pass

    def _generate_header_trailer(final_df, fecha_extract, name):
        pass

    def _header_and_trailer(final_df, fecha_extract, name, entity, outdat):
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
        print("Error de ejecucion: "+str(e))
        sys.exit(os.EX_IOERR)