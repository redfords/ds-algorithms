import pylightxl as xl
import sys, glob, os, traceback

def create_query(tabla, cols, iniciativa, zona):
    entidad = "ber"
    # """
    #     SELECT
    #     FROM $SUBENTORNO_$ENTIDAD_1raw.tabla_origen
    #     WHERE fecha_proceso = '$FECHA_PROCESO'
    # """

    query = f"""
        CREATE EXTERNAL TABLE de_{entidad}_{zona[1]}.{tabla['nombre']} (
            {'|'.join(cols)}
            )       
        COMMENT '{tabla['descripcion']}' 
        PARTITIONED BY (
            fecha_proceso VARCHAR(8)
            )
        STORED AS PARQUET
        LOCATION 'hdfs://nameservice1/user/admin/dev/{entidad}/{zona[2]}/{iniciativa}'
        TBLPROPERTIES ('external.table.purge'='true');
        """
    
    return query.replace('|', ',\n\t    ')
   
def get_size(size):
    if str(size).endswith(')'):
        num = size.partition('(')
        return f"({num[0]},{num[2]}"
    else:
        return f"({str(size)})"

def get_col(row, inc):
    name = row[1].lower()
    data_type = row[2 + inc]
    size = ''
    if inc >= 1 and data_type in ["CHAR", "VARCHAR", "DECIMAL"]:
        size = get_size(row[6])
    comment = row[3 + inc]

    return f"{name} {data_type}{size} COMMENT '{comment}'"

def get_table_data(sheet, zona, iniciativa):
    row = 0
    inc = 0
    if "2cur" in zona:
        inc = 1
    if "3ref" in zona:
        inc = 3

    while row < len(sheet):
        table = dict()
        if sheet[row][0] == "Descripcion de tabla":
            row += 1
            row += 1
            table['nombre'] = sheet[row][1].lower().strip()
            table['descripcion'] = sheet[row + 1][1]
            row += 4
            if "3ref" in zona:
                row += 1
            cols = list()
            while sheet[row][0] != 'Generado por el proceso':
                if sheet[row][1] == '':
                    row += 1
                else:
                    cols.append(get_col(sheet[row], inc))
                    row += 1

            query = create_query(table, cols, iniciativa, zona)
            print(query)
        row += 1

def read_sheet(file, zona):
    sheet = list()
    for row in file.ws(ws=zona[0]).rows:
        sheet.append(row)
    
    return sheet

def read_file(file_name):
    file = xl.readxl(fn=file_name)

    return file

if __name__ == "__main__":

    try:
        file_name = sys.argv[1]
        iniciativa = sys.argv[2]
        
        zonas = [ 
            ['2. Zona Cruda', '1raw', '01-raw'],
            ['3. Zona Curada', '2cur', '02-cur'],
            ['4. Zona Refinada', '3ref', '03-ref']
        ]

        file = read_file(file_name)

        for zona in zonas:
            print("Tablas", zona[0])
            sheet = read_sheet(file, zona)
            get_table_data(sheet, zona, iniciativa)

    except Exception as e:
        traceback.print_exc()
        print(e)
        sys.exit(os.EX_IOERR)