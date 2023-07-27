from sys import argv
from traceback import print_exc
from itertools import chain
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf, col, when, lit, create_map
from pyspark.sql.session import SparkSession

class OmniReporteExtendido():
    def execute(self, path_input, path_output, mes_proceso):
        _pattern = 'reporte_extendido'

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

        data = self.contexts['spark'].read.csv('hdfs://' + path_input, sep='|', header=True, inferSchema = False)
        
        data = data.withColumn("monto", udf_monto("amt_1"))\
            .withColumn("monto", col("monto")/100)
        data = data.withColumn("importe", col("monto").cast('decimal(16,2)'))

        data = data.withColumn("moneda", when(col("orig_crncy_cde") == "032", "ARS").otherwise("USD"))
        data = data.withColumn("cuil", col("crd_pan").substr(6, 11))

        data = data.withColumn("fecha", udf_fecha("tran_dat"))\
            .withColumn("hora", udf_hora("tran_tim"))

        tipo = {
            "180100": "INVERSIÓN EN PLAZO FIJO CON DÉBITO EN CUENTA CORRIENTE EN PESOS",
            "181100": "INVERSIÓN EN PLAZO FIJO CON DÉBITO EN CAJA DE AHORRO EN PESOS",
            "180700": "INVERSIÓN EN PLAZO FIJO CON DÉBITO EN CUENTA CORRIENTE EN DOLARES",
            "181500": "INVERSIÓN EN PLAZO FIJO CON DÉBITO EN CUENTA CORRIENTE EN DOLARES",
            "2P0011": "Solicitud De Prestamo a Caja de Ahorro",
            "2P0001": "Solicitud De Prestamo a Cuenta Corriente",
            "401115": "Compra de Dolares desde Caja de Ahorro en Pesos",
            "400115": "Compra de Dolares a Cuenta Corriente en Pesos",
            "401511": "Venta de Dolares a Caja de Ahorro en Pesos",
            "401501": "Venta de Dolares a Cuenta Corriente en Pesos"
        }

        data = data.withColumn("codigo",
            when((col("t_cde") == "18") & (col("t_from") == "01"), "180100")
            .when((col("t_cde") == "18") & (col("t_from") == "11"), "181100")
            .when((col("t_cde") == "18") & (col("t_from") == "07"), "180700")
            .when((col("t_cde") == "18") & (col("t_from") == "15"), "181500")
            .when((col("t_cde") == "2P") & (col("t_to") == "11"), "2P0011")
            .when((col("t_cde") == "2P") & (col("t_to") == "01"), "2P0001")
            .when((col("t_cde") == "40") & (col("t_from") == "15") & (col("t_to") == "11"), "401511")
            .when((col("t_cde") == "40") & (col("t_from") == "15") & (col("t_to") == "01"), "401501")
            .when((col("t_cde") == "40") & (col("t_from") == "11") & (col("t_to") == "15"), "401115")
            .when((col("t_cde") == "40") & (col("t_from") == "01") & (col("t_to") == "15"), "400115")
            .otherwise("0"))
        
        map_tipo = create_map([lit(x) for x in chain(* tipo.items())])
        data = data.withColumn("tipo", map_tipo.getItem(col("codigo")))
        data = data.withColumn("cantidad", lit("1"))
        data = data.withColumnRenamed("term_typ", "canal")\
            .withColumnRenamed("resp_byte_2", "codigo_respuesta")
        
        data = data.orderBy("tran_dat")
        data = data.select("canal", "moneda", "codigo", "tipo", "cuil", "fecha", "hora", "importe", "cantidad", "codigo_respuesta")

        for codigo in tipo.keys():
            data = data.filter("codigo = {c}".format(codigo))
            if codigo != "180100": data.drop("codigo_respuesta")
            data.coalesce(1).write.option("sep", "|").format("com.databricks.spark.csv")\
                .option("header","true").option("ignoreLeadingWhiteSpace", "false")\
                .option("ignoreTrailingWhiteSpace", "false").mode("append").save(path_output + "/{c}".format(codigo))

if __name__=="__main__":
    try:
        path_input = argv[1]
        path_output = argv[2]
        mes_proceso = argv[3]

        reporte_extendido = OmniReporteExtendido()
        reporte_extendido.execute(path_input, path_output, mes_proceso)
	
    except Exception as e:
        print_exc()
        exit(1)