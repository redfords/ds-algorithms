from sys import argv
from traceback import print_exc
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf, col, when, concat
from pyspark.sql.session import SparkSession


class OmniReporteExtendido():
    def execute(self, path_input, path_output, mes_proceso):

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

        app_name = "Reporte extendido " + str(mes_proceso)
        spark = SparkSession.builder.appName(app_name).master('yarn').enableHiveSupport()\
                    .config('spark.sql.warehouse.dir', 'hdfs://nameservice1/user/admin/test') \
                    .config('spark.executor.memory','12g') \
                    .config('spark.driver.memory','20g') \
                    .config('spark.executors.cores','4') \
                    .config('spark.cores.max','4') \
                    .config('hive.enforce.bucketing', 'false') \
                    .config('hive.enforce.sorting', 'false') \
                    .config('spark.hadoop.hive.exec.dynamic.partition','true') \
                    .config('spark.hadoop.hive.exec.dynamic.partition.mode','nonstrict') \
                    .config('spark.sql.autoBroadcastJoinThreshold','-1') \
                    .config('spark.cleaner.referenceTracking.cleanCheckpoints', 'true') \
                    .config('spark.driver.extraClassPath','/opt/cloudera/parcels/CDH-7.1.3-1.cdh7.1.3.p0.4992530/lib/spark/jars/hive-exec-3.1.3000.7.1.3.0-100.jar') \
                    .config('spark.executor.extraClassPath', '/opt/cloudera/parcels/CDH-7.1.3-1.cdh7.1.3.p0.4992530/lib/spark/jars/hive-exec-3.1.3000.7.1.3.0-100.jar') \
                    .getOrCreate()
        self.contexts = {}
        self.contexts['spark'] = spark
        
        # plazo fijo cc pesos
        data = self.contexts['spark'].read.csv('hdfs://' + path_input, sep='|', header=True, inferSchema = False)

        # where  T_cde = "18" and T_from = "01" 


        # convierto amt_1 en monto
        data = data.withColumn("monto", udf_monto("amt_1"))\
            .withColumn("monto", col("monto")/100)
        
        # reemplazo decimal
        amt = data.withColumn("amt", col("monto").cast('decimal(16,2)'))

        # convierto orig_crncy_cde en moneda

        # cuil, fecha, hora

        # term_typ, codigo, tipo, cantidad, codigo respuesta

        # order by tran_dat
        

        
        amt.show()
        amt=amt.orderBy("Codigo")        
        amt.coalesce(1).write.option("sep", "|").format("com.databricks.spark.csv").option("header","true")\
            .option("ignoreLeadingWhiteSpace", "false").option("ignoreTrailingWhiteSpace", "false").mode("append").save(path_output)



if __name__=="__main__":
    try:
        path_input = argv[1]
        path_output = argv[2]
        mes_proceso = argv[3]

        reporte_mensual = OmniReporteExtendido()
        reporte_mensual.execute(path_input, path_output, mes_proceso)
	
    except Exception as e:
        print_exc()
        exit(1)