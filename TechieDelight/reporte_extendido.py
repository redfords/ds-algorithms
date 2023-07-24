from sys import argv
from traceback import print_exc
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf, col, when, lit
from pyspark.sql.session import SparkSession


class OmniReporteExtendido():
    def execute(self):

        def format_monto(monto):
            output = ''
            last_char = monto[-1]
            valor = {
                "0": "0",
                "{": "0",
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4",
                "E": "5",
                "F": "6",
                "G": "7",
                "H": "8",
                "I": "9"
            }[last_char]
            output = monto[:-1] + valor
            return output
        udf_monto = udf(format_monto, StringType())

        def format_fecha(tran_dat):
            output = [
                '20' + str(tran_dat[0:2]),
                str(tran_dat[2:4]),
                str(tran_dat[4:6])
            ]
            return '-'.join(output)
        udf_fecha = udf(format_fecha, StringType())

        def format_hora(tran_tim):
            output = [
                str(tran_tim[0:2]),
                str(tran_tim[2:4]),
                str(tran_tim[4:6]),
                '.' + str(tran_tim[6:8])
            ]
            return ':'.join(output)
        udf_hora = udf(format_hora, StringType())

        # app_name = "Reporte extendido "
        # spark = SparkSession.builder.appName(app_name).master('yarn').enableHiveSupport()\
        #             .config('spark.sql.warehouse.dir', 'hdfs://nameservice1/user/admin/test') \
        #             .config('spark.executor.memory','12g') \
        #             .config('spark.driver.memory','20g') \
        #             .config('spark.executors.cores','4') \
        #             .config('spark.cores.max','4') \
        #             .config('hive.enforce.bucketing', 'false') \
        #             .config('hive.enforce.sorting', 'false') \
        #             .config('spark.hadoop.hive.exec.dynamic.partition','true') \
        #             .config('spark.hadoop.hive.exec.dynamic.partition.mode','nonstrict') \
        #             .config('spark.sql.autoBroadcastJoinThreshold','-1') \
        #             .config('spark.cleaner.referenceTracking.cleanCheckpoints', 'true') \
        #             .config('spark.driver.extraClassPath','/opt/cloudera/parcels/CDH-7.1.3-1.cdh7.1.3.p0.4992530/lib/spark/jars/hive-exec-3.1.3000.7.1.3.0-100.jar') \
        #             .config('spark.executor.extraClassPath', '/opt/cloudera/parcels/CDH-7.1.3-1.cdh7.1.3.p0.4992530/lib/spark/jars/hive-exec-3.1.3000.7.1.3.0-100.jar') \
        #             .getOrCreate()
        
        
        # prueba
        spark = (SparkSession
            .builder
            .appName("Testing report.")
            .getOrCreate())
        self.contexts = {}
        self.contexts['spark'] = spark
        data = self.contexts['spark'].read.csv('rep_mens.csv', sep='|', header=True, inferSchema = False)

        # filter by t_cde and t_from
        data = data.filter("t_cde = '18' AND t_from = '01'")

        # format monto
        data = data.withColumn("monto", udf_monto("amt_1"))\
            .withColumn("monto", col("monto")/100)
        data = data.withColumn("importe", col("monto").cast('decimal(16,2)'))

        # update currency code and cuil
        data = data.withColumn("moneda", when(col("orig_crncy_cde") == "032", "ARS").otherwise("USD"))
        data = data.withColumn("cuil", col("crd_pan").substr(6, 11))

        data = data.select("tran_dat", "tran_tim", "term_typ", "resp_byte_2", "importe", "moneda", "cuil")

        # format date and time
        data = data.withColumn("fecha", udf_fecha("tran_dat"))\
            .withColumn("hora", udf_hora("tran_tim"))

        # add constant columns
        data = data.withColumn("codigo", lit("180100"))\
            .withColumn("tipo", lit("INVERSIÓN EN PLAZO FIJO"))\
            .withColumn("cantidad", lit("1"))
        
        # rename columns
        data = data.withColumnRenamed("term_typ", "canal")\
            .withColumnRenamed("resp_byte_2", "codigo_respuesta")
        
        data = data.orderBy("tran_dat")

        data = data.select("canal", "moneda", "codigo", "tipo", "cuil", "fecha", "hora", "importe", "cantidad")
        data.show(5)


        # plazo fijo cc pesos
        # data = self.contexts['spark'].read.csv('hdfs://' + path_input, sep='|', header=True, inferSchema = False)


        # amt.coalesce(1).write.option("sep", "|").format("com.databricks.spark.csv").option("header","true")\
        #     .option("ignoreLeadingWhiteSpace", "false").option("ignoreTrailingWhiteSpace", "false").mode("append").save(path_output)

if __name__=="__main__":
    try:
        # path_input = argv[1]
        # path_output = argv[2]
        # mes_proceso = argv[3]

        reporte_mensual = OmniReporteExtendido()
        # reporte_mensual.execute(path_input, path_output, mes_proceso)
        reporte_mensual.execute()
	
    except Exception as e:
        print_exc()
        exit(1)