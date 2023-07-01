import sys, json, traceback

class NoGroupException(Exception):
    '''Raise when the group argument is missing'''

class NoPanException(Exception):
    '''Raise when the pan argument is missing'''

class TRXFormatNotValidException(Exception):
    '''Raise when the input is not json format'''

WS_USER = {
    "a": "SV_SPFSERVICES_0386",
    "b": "SV_SPFSERVICES_0071"
}

WS_PASSWORD = {
    "a": "*7BR5CpZBYdiaLqVP9(n",
    "b": "gRTq4ErLcJ_TGwy_LVhR"
}

class Transaction:
    def __init__(self, trx_type, trx_data, trx_pan, group, acc_no = 0):
        pass

def generate_xml(data: json, group: str, pan_no: str) -> list:
    """Returns a list of an xml per trx"""
    trx_obj = Transaction(trx_type=data["request"]["idActivity"],
                          trx_data=data,
                          trx_pan=pan_no,
                          group=group)
    
    return [fill_xml(trx_obj, pan_no)]

def fill_xml(trx_obj: str, group: str) -> str:
    """Returns the xml template with the trx data"""
    return """<?xml version="1.0" encoding="UTF-8"?>
                    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.ws.spfservices.redlink.com.ar/">
                    <soapenv:Header>
                        <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" soapenv:mustUnderstand="1">
                            <wsse:UsernameToken wsu:Id="UsernameToken-C734DACD44C7F029F816195003929764">
                                <wsse:Username>%s</wsse:Username>
                                <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">%s</wsse:Password>
                            </wsse:UsernameToken>
                        </wsse:Security>
                    </soapenv:Header>
                    <soapenv:Body>
                        <ser:uploadTransaction>
                            <!--Optional:-->
                            <requerimientoUploadTransaction>
                                <cabecera>
                                <idRequerimiento>%s</idRequerimiento>
                                <ipCliente>%s</ipCliente>
                                <timeStamp>%s</timeStamp>
                                <idEntidad>%s</idEntidad>
                                <canal>%s</canal>
                                </cabecera>
                                <datosTransaction>
                                <fiidTerm>%s</fiidTerm>
                                <termId>%s</termId>
                                <fiidCard>%s</fiidCard>
                                <pan>%s</pan>
                                <seqNum>%s</seqNum>
                                <tranDat>%s</tranDat>
                                <tranTim>%s</tranTim>
                                <typ>%s</typ>
                                <typCde>%s</typCde>
                                <postDat>%s</postDat>
                                <tranCde>%s</tranCde>
                                <fromAcct>%s</fromAcct>
                                <tipoDep>%s</tipoDep>
                                <toAcct>%s</toAcct>
                                <importe>%s</importe>
                                <respCde>%s</respCde>
                                <issuerFiid>%s</issuerFiid>
                                <termType>%s</termType>
                                <tipoCambio>%s</tipoCambio>
                                <tipoCambioC>%s</tipoCambioC>
                                <cuota>%s</cuota>
                                <ente>%s</ente>
                                <termLn>%s</termLn>
                                <crncyCde>%s</crncyCde>
                                <cardType>%s</cardType>
                                <codigoPais>%s</codigoPais>
                                <locTerm>%s</locTerm>
                                <denEstabl>%s</denEstabl>
                                <establecimiento>%s</establecimiento>
                                <rubro>%s</rubro>
                                <cvvrc>%s</cvvrc>
                                <direccionIp>%s</direccionIp>
                                <canal>%s</canal>
                                <producto>%s</producto>
                                <tel>%s</tel>
                                <crdLn>%s</crdLn>
                                <codigoPaisEntidad>%s</codigoPaisEntidad>
                                </datosTransaction>
                            </requerimientoUploadTransaction>
                        </ser:uploadTransaction>
                    </soapenv:Body>
                    </soapenv:Envelope>
    """

if __name__ == "__main__":
    sys.setdefaultencoding = "utf-8"

    try:
        group = sys.argv[1].lower()
    except:
        raise NoGroupException("Group must be the first argument.")
    try:
        pan_no = sys.argv[2].lower()
    except:
        raise NoPanException("Pan number must be the second argument.")
    try:
        with open('sample_trx.json') as file:
            trx = json.load(file)
    except:
        raise TRXFormatNotValidException("TRX Input content is not of valid json type.")
    try:
        print('#&&#'.join(generate_xml(trx, group, pan_no)))
    except Exception as e:
        print("Json could not be created with input.")
        traceback.print_exc()
    


