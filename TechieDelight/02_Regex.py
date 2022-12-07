from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, regexp_replace, lpad, lit
from pyspark.sql.types import StringType
import re, sys, os

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

def _fill_decimals(monto):
    monto_str = str(monto)
    if '.' not in monto_str:
        return monto_str + ".00"
    else:
        monto_final = monto_str
        try:
            decimals = monto_str.split('.')
            if (len(decimals[1]) == 1):
                monto_final += "0"
        except:
            pass
        return monto_final

def execute(spark, fecha, fext, entidad, entorno, subent):
    udf_monto = udf(_format_monto, StringType())
    udf_fill = udf(_fill_decimals, StringType())

    df = spark.sql(
        """
        SELECT prefix,reg_len,reg_typ,dat_tim,rec_typ,auth_ppd,term_ln,term_fiid,term_id,crd_ln,crd_fiid,crd_pan,
        mbr_num,brch_id,regn_id,user_fld1x,typ_cde,typ,rte_stat,originator,responder,entry_tim,exit_tim,re_entry_tim,tran_dat,
        tran_tim,post_dat,acq_ichg_setl_dat,iss_ichg_setl_dat,seq_num,term_typ,tim_ofst,acq_inst_id_num,rcv_inst_id_num,
        CAST(t_cde as VARCHAR(19)),t_from,t_to,from_acct,tipo_tran,to_acct,mult_acct,
        amt_1,amt_2,amt_3,
        filler,dep_typ,resp_byte_1,resp_byte_2,term_name_loc,term_owner_name,term_city,term_st_x,term_cntry_x,oseq_num,
        otran_dat,otran_tim,b24_post_day,orig_crncy_cde,user_fld2,cuotas,imp_cuota,tna,tem,tea,cft,impacto,tasa,destino,
        filler_us_2p,interest_rate,card_type_35_40, tip_excha_comp,arbitraje,tip_excha_vend,filler_35_40,acc_stat,filler_6110,
        cant_bol,chequeras,filler_6102,rvsl_rsn,pin_ofst,shrg_grp,filler_2,tipo_dep,issuer_fiid,fee_amt,cash_fee,card_type,
        situacion_iva,datos_transaccionales,id_producto,filler_op,id_companias_de_seguro,porcentaje_comp_seg,
        cft2,tipo,numero,linea,filler_dt_2p,importe_percepcion,cotizacion_percepcion,porcentaje_percepcion,filler_dt_40,
        cbu,filler_f1_f2,emv_status,es_chip
        FROM {0}_{1}_3ref.Can_Ges_Extract_Prima_Individuos_FT_Transacciones  WHERE fecha_proceso = {2} 
    """.format(subent, entidad, fecha)
    )

    df.createOrReplaceTemplateView("df")
    x = df.count()
    print("Se levantaron esta cantidad de la 1ra de Ref: ")
    print(x)
    if x != 0:

        df = df.withColumn("amt_1", udf_fill("amt_1"))
        df = df.withColumn("amt_1", col("amt_1").cast(StringType()))
        df = df.withColumn("amt_1", regexp_replace(col("amt_1"), "[\.]", ""))
        df = df.withColumn("amt_1", lpad(udf_monto("amt_1"), 19, "0"))
        df = df.withColumn("amt_2", udf_fill("amt_2"))
        df = df.withColumn("amt_2", regexp_replace(col("amt_2"), "[\.]", ""))    
        df = df.withColumn("amt_2", lpad(udf_monto("amt_2"), 19, "0")) 
        df = df.withColumn("amt_3", udf_fill("amt_3"))   
        df = df.withColumn("amt_3", regexp_replace(col("amt_3"), "[\.]", ""))     
        df = df.withColumn("amt_3", lpad(udf_monto("amt_3"), 19, "0")) 
        
        variables_seleccionadas = [
            'prefix', 'reg_len', 'reg_typ', 'dat_tim', 'rec_typ', 'auth_ppd', 'term_ln', 'term_fiid', 'term_id', 'crd_ln', 'crd_fiid', 'crd_pan',
            'mbr_num', 'brch_id', 'regn_id', 'user_fld1x', 'typ_cde', 'typ', 'rte_stat', 'originator', 'responder', 'entry_tim', 'exit_tim', 're_entry_tim', 'tran_dat',
            'tran_tim', 'post_dat', 'acq_ichg_setl_dat', 'iss_ichg_setl_dat', 'seq_num', 'term_typ', 'tim_ofst',
            'acq_inst_id_num', 'rcv_inst_id_num', 't_cde', 't_from', 't_to', 'from_acct', 'tipo_tran', 'to_acct', 'mult_acct', 'amt_1', 'amt_2', 'amt_3',
            'filler', 'dep_typ', 'resp_byte_1', 'resp_byte_2', 'term_name_loc', 'term_owner_name', 'term_city', 'term_st_x', 'term_cntry_x', 'oseq_num',
            'otran_dat', 'otran_tim', 'b24_post_day', 'orig_crncy_cde', 'user_fld2', 'cuotas', 'imp_cuota', 'tna', 'tem', 'tea', 'cft', 'impacto', 'tasa', 'destino',
            'filler_us_2p', 'interest_rate', 'card_type_35_40', 'tip_excha_comp', 'arbitraje', 'tip_excha_vend', 'filler_35_40','acc_stat', 'filler_6110',
            'cant_bol', 'chequeras', 'filler_6102', 'rvsl_rsn', 'pin_ofst', 'shrg_grp', 'filler_2', 'tipo_dep', 'issuer_fiid', 'fee_amt', 'cash_fee', 'card_type',
            'situacion_iva', 'datos_transaccionales','id_producto','filler_op', 'id_companias_de_seguro', 'porcentaje_comp_seg',
            'cft2', 'tipo', 'numero', 'linea', 'filler_dt_2p', 'importe_percepcion', 'cotizacion_percepcion', 'porcentaje_percepcion', 'filler_dt_40', 
            'cbu','filler_f1_f2', 'emv_status', 'es_chip'
            ]

        var_final = []
        for var in variables_seleccionadas:
            if var in df.columns:
                var_final.append(var)

        df = df.select(var_final)
        df = df.withColumn("fecha_proceso", lit(fecha))
        print("Insertando en la 2da de Ref: ")
        print("""{0}_{1}_3ref.Can_Ges_Extract_Prima_Individuos_FT_Pre_Archivo""".format(subent,entidad))
        df.write.insertInto(
            "{0}_{1}_3ref.Can_Ges_Extract_Prima_Individuos_FT_Pre_Archivo".format(subent, entidad), overwrite=False
        )
        print("Inserto esta cantidad de rows: ")
        print(df.count())

    else:
        print("No hay registros para levantar")


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
        print("Error de ejecucion: " + str(e))
        sys.exit(os.EX_IOERRR)