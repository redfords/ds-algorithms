import pylightxl as xl
import sys
import glob, os
import paramiko

def read_file():

    path = os.getcwd()
    file = glob.glob(os.path.join(path, "*.xlsx"))
    try:
        data = xl.readxl(fn=file[0])
    except UserWarning as e:
        print(e)
        sys.exit()
    except IndexError:
        print('No se encontró archivo compatible')
        sys.exit()

    return data

def read_sheet(data, zona):
   
    sheet = list()
    try:
        for row in data.ws(ws=zona[0]).rows:
            sheet.append(row)
    except UserWarning as e:
        print(e)
        sys.exit()

    return sheet

def get_query(tabla, cols, iniciativa, zona):

    return f"""
        CREATE EXTERNAL TABLE de_{tabla['entidad']}_{zona[1]}.{tabla['nombre']} (
            {', '.join(cols)}
            )       
        COMMENT '{tabla['descripcion']}' 
        PARTITIONED BY (
            {tabla['particion']})
            )
        STORED AS PARQUET
        LOCATION 'hdfs://nameservice1/user/admin/dev/{
                tabla['entidad']}/{zona[2]}/{iniciativa}'
        TBLPROPERTIES ('external.table.purge'='true');
        """

def send_query(query):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    server = "172.30.213.121"
    username = "jpiovaroli"
    password = "xcvb0987"
    command = f'hive -e "{query}"'

    ssh.connect(server, username=username, password=password)    
    stdin = ssh.exec_command(command)
    stdin.close()
    print("Tabla creada")

    return

def check_query(query):

    print(query)
    print("Enviar query? (S/n)")
    r = input()

    while(r.lower() != 'n'):
        if r.lower() == 's' or r == '':
            send_query(query)
            return
        else:
            r = input()
        return
    
def get_size(size):

    if str(size).endswith(')'):
        num = size.partition('(')
        return f"({num[0]},{num[2]}"
    else:
        return f"({str(size)})"

def get_partition(row, inc):

    return f"{row[1].lower()} {row[2 + inc]}({row[6]}"

def get_col(row, inc):

    name = row[1].lower()
    data_type = row[2 + inc]
    size = (get_size(row[6]) if inc == 1 else '')
    comment = row[3 + inc]

    return f"{name} {data_type}{size} COMMENT '{comment}'"

def get_col_select(row):
    name = row[2].lower()

    return f"{name}"

def get_select_query(tabla, cols_select):
    
    print(f"""
        SELECT
        {', '.join(cols_select)}
        FROM $SUBENTORNO_$ENTIDAD_1raw.{tabla['origen']}
        WHERE fecha_proceso = '$FECHA_PROCESO'
    """)

def get_data(sheet, zona, iniciativa):

    row = 0
    inc = 0
    if '1raw' not in zona:
        inc = 1
    
    while row < len(sheet):
        tabla = dict()
        if sheet[row][0] == 'Descripcion de tabla':
            row += 1
            if inc == 1:
                tabla['origen'] = sheet[row][1].lower()
            row += 1
            tabla['nombre'] = sheet[row][1].lower()
            tabla['entidad'] = sheet[row][5].lower()
            tabla['descripcion'] = sheet[row + 1][1]
            row += 4
            cols = list()
            cols_select = list()
            while sheet[row][0] != 'Generado por el proceso':
                if sheet[row][1] == '':
                    row += 1
                else:
                    cols.append(get_col(sheet[row], inc))
                    cols_select.append(get_col_select(sheet[row]))
                    row += 1
            tabla['particion'] = get_partition(sheet[row], inc)
            query = get_query(tabla, cols, iniciativa, zona)
            check_query(query)

            get_select_query(tabla, cols_select)
        row += 1

def main():

    iniciativa = sys.argv[1]
    zonas = [
        # ('2. Zona Cruda', '1raw', '01-raw'),
        ('3. Zona Curada', '2cur', '02-cur'),
        ('4. Zona Refinada', '3ref', '03-ref')
    ]
    data = read_file()

    for zona in zonas:
        sheet = read_sheet(data, zona)
        get_data(sheet, zona, iniciativa)

if __name__ == "__main__":
    main()
