"""
DESCOMPRIMIR

Copiar en coded_string la columna data para descomprimir.

Para buscar en cyberbank por fecha y hora:
SELECT *
FROM CBANKDB.CLIENT_AUDIT_LOG_EXTRA cale 
WHERE cale.DATE_TIME = TO_DATE('2023-07-12 23:22:57','yyyy-MM-dd HH24:MI:ss');

Para buscar en raw por fecha y hora:
SELECT *
FROM pr_bsc_1raw.cyberbank_individuos_mensajeiso
WHERE substring(date_time, 0, 19) = '2023-07-12 23:59:59';
"""

import base64
import zlib

coded_string = 'H4sIAAAAAAAAAFWOMQ7CMAxF954iyoxUx4lpxQEYUYdewEksxFBShXZAiLtDGqSK0e99+f9Xo5Se+SqXdfKS9Ulpow8FcghpvS/jc5ZC4YcjLzKmLWdacC0CYjVZQsrxMUgevv9KAqGaW9yuyIatRbbeO8fInacjmcAC0Tvu/mr3OUiWqO+J9v5zTlNRFlqwdUHz/gDEQrgRygAAAA=='
bytecode = base64.b64decode(coded_string)
decoded = zlib.decompress(bytecode, zlib.MAX_WBITS|16)
print(decoded)

"""
TIPOS DE SERVICIO

t_cde
18 - Inversion En Plazo Fijo
28 - Precancelacion De Operacion De Plazo Fijo
2H - Realizar Anticipo De Haberes
2P - Solicitud De Prestamo
30 - Consulta De Saldos
34 - Asignacion De Usuario, Clave De Acceso A Homebanking
35 - Consulta De Tipo De Cambio
37 - Consulta Publicitaria De Plazos Y Tasas De Operaciones De Plazo Fijo
38 - Consulta De Saldo De Plazo Fijo
3H - Consulta De Importe Disponible Para Anticipo De Haberes
40 - Compra/Venta De Dolares
62 - Login En Home Banking
70 - Ultimos Movimientos
F1 - Fci Subscripcion
F2 - Fci - Anulacion Subscripcion
OP - Ofrecimiento de Productos

t_cde + t_from
6101 - Mensaje A La Institucion - Solicitud De Extracto
6102 - Mensaje A La Institucion - Solicitud De Chequeras
6109 - Solicitud De Modificacion Del Limite De Extraccion
6110 - Seleccion De Cuenta Primaria
6111 - Mensaje A La Institucion - Cierre De Cuenta
"""