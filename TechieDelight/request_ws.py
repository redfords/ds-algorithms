import sys, requests
from bs4 import BeautifulSoup

class NoGroupException(Exception):
    '''Raise when the group argument is missing'''

class WebServiceDownException(Exception):
    """Raise when web service is not responding"""

ws_groups = {
    'group_1': "https://172.30.89.201/",   
    'group_2': "https://172.30.84.201/"
}

user = "username"
password = "password"

def parse_response(response, xml_data):
    feedback = str(response.text())
    soup = BeautifulSoup(feedback, "xml")
    xml_parse = BeautifulSoup(xml_data, "xml")

    



if __name__ == "__main__":
    try:
        group = sys.arg[1].lower()
    except Exception as e:
        raise NoGroupException("Group must be the first argument on call.")
    
    header = {
        "POST": f"{ws_groups.get(group)[:20]}:443/spfservices/ConsultaServices HTTP/1.1",
        "Accept-Encoding": "gzip,deflate",
        "Content-Type": "text/xml;charset=UTF-8",
        "Host": f"{ws_groups.get(group)[8:20]}:443",
        "Connection": "Keep-Alive",
        "User-Agent": "Apache-HttpClient/4.5.5 (Java/12.0.1)"
    }

    xml_to_request = sys.stdin.read().encode('utf-8')

    try:
        response = requests.post(ws_groups.get(group), headers=header, data=xml_to_request, verify=False,
                                 auth=(user, password))
    except Exception as e:
        raise WebServiceDownException("The webservice is not responding at the moment.", e)
    
    print(response.text)
