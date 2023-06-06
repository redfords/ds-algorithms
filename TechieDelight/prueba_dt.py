import sys, os, traceback
import argparse
from pylightxl import readxl, Database


def create_query(name: str, desc: str, cols: list,path: str,
                 zone: list) -> str:
    """Returns a query to create the table"""
    entidad = "ber"
    
    # """
    #     SELECT
    #     FROM $SUBENTORNO_$ENTIDAD_1raw.tabla_origen
    #     WHERE fecha_proceso = '$FECHA_PROCESO'
    # """

    query = f"""
        CREATE EXTERNAL TABLE de_{entidad}_{zone[1]}.{name} (
            {'|'.join(cols)}
            )       
        COMMENT '{desc}' 
        PARTITIONED BY (
            fecha_proceso VARCHAR(8)
            )
        STORED AS PARQUET
        LOCATION 'hdfs://nameservice1/user/admin/dev/{entidad}/{zone[2]}/{path}'
        TBLPROPERTIES ('external.table.purge'='true');
        """
    
    return query.replace('|', ',\n\t    ')

def get_col(row: list, inc: int) -> str:
    """Returns a string with the column data"""

    name = row[1].lower()
    data_type = row[2 + inc]
    size = ''

    if inc >= 1 and data_type in ["CHAR", "VARCHAR", "DECIMAL"]:
        right = 0 if inc == 1 else 2
        size = f"({str(row[6 + right])})"

    comment = row[3 + inc]

    return f"{name} {data_type}{size} COMMENT '{comment}'"

def get_table_data(sheet: list, zone: list, path: str):
    """Reads all rows in the sheet"""
    row = 0
    inc = 0
    if "2cur" in zone:
        inc = 1
    if "3ref" in zone:
        inc = 3

    while row < len(sheet):
        if sheet[row][0] == "Descripcion de tabla":
            row += 2
            name = sheet[row][1].lower().strip()
            desc = sheet[row + 1][1]
            row += 4
            if "3ref" in zone:
                row += 1
            cols = list()
            while sheet[row][0] != 'Generado por el proceso':
                if sheet[row][1] == '':
                    row += 1
                else:
                    cols.append(get_col(sheet[row], inc))
                    row += 1

            query = create_query(name, desc, cols, path, zone)
            print(query)
        row += 1

def read_sheet(db: Database, zone: str) -> list:
    """Returns a list with all the rows from a sheet"""

    sheet = list()
    for row in db.ws(ws=zone[0]).rows:
        sheet.append(row)
    
    return sheet

def read_file(file_name: str) -> Database:
    """Returns a database with the contents of a .xlsx file"""

    db = readxl(fn=file_name)

    return db

if __name__ == "__main__":

    try:
        file_name = sys.argv[1]
        path = sys.argv[2]
        
        zones = [ 
            ['2. Zona Cruda', '1raw', '01-raw'],
            ['3. Zona Curada', '2cur', '02-cur'],
            ['4. Zona Refinada', '3ref', '03-ref']
        ]

        db = read_file(file_name)

        for zone in zones:
            print("\n", zone[0])
            sheet = read_sheet(db, zone)
            get_table_data(sheet, zone, path)

    except Exception as e:
        traceback.print_exc()
        print(e)
        sys.exit(os.EX_IOERR)