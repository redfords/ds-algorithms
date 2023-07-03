import sys, json, traceback

class NoGroupException(Exception):
    '''Raise when the group argument is missing'''

class NoPanException(Exception):
    '''Raise when the pan argument is missing'''

class TRXFormatNotValidException(Exception):
    '''Raise when the input is not json format'''

GROUP_ID = {
    "a": "0001",
    "b": "0002"
}

GROUP_NODES = {
    "a": "172.30.215.100",
    "b": "172.30.215.101"
}

WS_USER = {
    "a": "sv_services_0001",
    "b": "sv_services_0002"
}

WS_PASSWORD = {
    "a": "g6skUqnC817Hjs23",
    "b": "kID9Hndy7f2B1a6x"
}

class Transaction:
    def __init__(self, trx_type, trx_data, trx_pan, group, acc_no = 0):
        self.trx_type = trx_type
        self.trx_data = trx_data
        self.trx_group = group
        # header
        self.idRequerimiento = self._get_idRequerimiento()
        self.ipCliente = GROUP_NODES.get(self.trx_group)
        self.timeStamp = self._get_timeStamp()
        self.idEntidad = GROUP_ID.get(self.trx_group)
        self.canalCabecera = "HBP"
        # transaction data
        self.fiidTerm = GROUP_ID.get(self.trx_group)
        self.termId = "0"*16
        self.fiidCard = self._get_fiidCard()
        self.pan = trx_pan
        self.seqNum = self._get_seqNum()
        self.tranDat = self._get_tranDat()
        self.tranTim = self._get_tranTim()
        self.typ = "0210"
        self.typCde =  "31"
        self.postDat = self._get_tranDat()
        self.tranCde =  self._get_tranCde(acc_no)
        self.fromAcct = self._get_fromAcct()
        self.tipoDep = "0"
        self.toAcct = self._get_toAcct()
        self.importe = self._get_importe()
        self.respCde = self._get_respCde()
        self.issuerFiid = self._get_issuerFiid()
        self.termType = self._get_termType()
        self.tipoCambio = "0"*8
        self.tipoCambioC = "0"*8
        self.cuota = "0"*5
        self.ente = "0"*3
        self.termLn = GROUP_ID.get(self.trx_group)
        self.crncyCde = self._get_crncyCde(acc_no)
        self.cardType = "P "
        self.codigoPais = "032"
        self.locTerm = "0"*13
        self.denEstabl = "0"*25
        self.establecimiento = "0"*15
        self.rubro = "0"*5
        self.cvvrc = "0"
        self.direccionIp = self._get_direccionIp()
        self.canal = self._get_canal()
        self.producto = "0"*2
        self.tel = "0"*20
        self.crdLn = self._get_crdLn()
        self.codigoPaisEntidad = "032"

    def _get_idRequerimiento(self):
        pass

    def _get_timeStamp(self):
        pass

    def _get_fiidCard(self):
        pass

    def _get_seqNum(self):
        pass

    def _get_tranDat(self):
        pass

    def _get_tranCde(self):
        pass

    def _get_fromAcct(self):
        pass

    def _get_toAcct(self):
        pass

    def _get_importe(self):
        pass

    def _get_respCde(self):
        pass

    def _get_issuerFiid(self):
        pass

    def _get_termType(self):
        pass

    def _get_crncyCde(self):
        pass

    def _get_direccionIp(self):
        pass

    def _get_canal(self):
        pass

    def _get_crdLn(self):
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
    return f"""<?xml version="1.0" encoding="UTF-8"?>
                    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.ws.spfservices.redlink.com.ar/">
                    <soapenv:Header>
                        <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" soapenv:mustUnderstand="1">
                            <wsse:UsernameToken wsu:Id="UsernameToken-C734DACD44C7F029F816195003929764">
                                <wsse:Username>{WS_USER.get(group)}</wsse:Username>
                                <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{WS_PASSWORD.get(group)}</wsse:Password>
                            </wsse:UsernameToken>
                        </wsse:Security>
                    </soapenv:Header>
                    <soapenv:Body>
                        <ser:uploadTransaction>
                            <!--Optional:-->
                            <requerimientoUploadTransaction>
                                <cabecera>
                                <idRequerimiento>{trx_obj.idRequerimiento}</idRequerimiento>
                                <ipCliente>{trx_obj.ipCliente}</ipCliente>
                                <timeStamp>{trx_obj.timeStamp}</timeStamp>
                                <idEntidad>{trx_obj.idEntidad}</idEntidad>
                                <canal>{trx_obj.canal}</canal>
                                </cabecera>
                                <datosTransaction>
                                <fiidTerm>{trx_obj.fiidTerm}</fiidTerm>
                                <termId>{trx_obj.termId}</termId>
                                <fiidCard>{trx_obj.fiidCard}</fiidCard>
                                <pan>{trx_obj.pan}</pan>
                                <seqNum>{trx_obj.seqNum}</seqNum>
                                <tranDat>{trx_obj.tranDat}</tranDat>
                                <tranTim>{trx_obj.tranTim}</tranTim>
                                <typ>{trx_obj.typ}</typ>
                                <typCde>{trx_obj.typCde}</typCde>
                                <postDat>{trx_obj.postDat}</postDat>
                                <tranCde>{trx_obj.tranCde}</tranCde>
                                <fromAcct>{trx_obj.fromAcct}</fromAcct>
                                <tipoDep>{trx_obj.tipoDep}</tipoDep>
                                <toAcct>{trx_obj.toAcct}</toAcct>
                                <importe>{trx_obj.importe}</importe>
                                <respCde>{trx_obj.respCde}</respCde>
                                <issuerFiid>{trx_obj.issuerFiid}</issuerFiid>
                                <termType>{trx_obj.termType}</termType>
                                <tipoCambio>{trx_obj.tipoCambio}</tipoCambio>
                                <tipoCambioC>{trx_obj.tipoCambioC}</tipoCambioC>
                                <cuota>{trx_obj.cuota}</cuota>
                                <ente>{trx_obj.ente}</ente>
                                <termLn>{trx_obj.termLn}</termLn>
                                <crncyCde>{trx_obj.crncyCde}</crncyCde>
                                <cardType>{trx_obj.cardType}</cardType>
                                <codigoPais>{trx_obj.codigoPais}</codigoPais>
                                <locTerm>{trx_obj.locTerm}</locTerm>
                                <denEstabl>{trx_obj.denEstabl}</denEstabl>
                                <establecimiento>{trx_obj.establecimiento}</establecimiento>
                                <rubro>{trx_obj.rubro}</rubro>
                                <cvvrc>{trx_obj.cvvrc}</cvvrc>
                                <direccionIp>{trx_obj.direccionIp}</direccionIp>
                                <canal>{trx_obj.canal}</canal>
                                <producto>{trx_obj.producto}</producto>
                                <tel>{trx_obj.tel}</tel>
                                <crdLn>{trx_obj.crdLn}</crdLn>
                                <codigoPaisEntidad>{trx_obj.codigoPaisEntidad}</codigoPaisEntidad>
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
    


