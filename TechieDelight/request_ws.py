import sys

class NoGroupException(Exception):
    '''Raise when the group argument is missing'''

ws_groups = {
    'group_1': "https://172.30.89.201/",   
    'group_2': "https://172.30.84.201/"
}

if __name__ == "__main__":
    try:
        entity = sys.arg[1].lower()
    except Exception as e:
        raise NoGroupException("Group must be the first argument on call.")
    
    header = {
        "POST": "%s:443/spfservices/ConsultaServices HTTP/1.1" % ws_entidades.get(entity)[:20],
        "Accept-Encoding": "gzip,deflate",
        "Content-Type": "text/xml;charset=UTF-8",
        "Host": "%s:443" % ws_entidades.get(entity)[8:20],
        "Connection": "Keep-Alive",
        "User-Agent": "Apache-HttpClient/4.5.5 (Java/12.0.1)"
    }

    xml_to_request = sys.stdin.read().encode('utf-8')

    try:
        
