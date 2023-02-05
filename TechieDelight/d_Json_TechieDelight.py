import json
import requests
import sys
import traceback

def json_actions():
    
    """ 
    JSON Parsing
    Source: https://github.com/chrhobbs/exercise-python-json-parsing

    Exercise 1
    Using data file 'interface-data.json', create output that resembles the following:

    Interface Status
    ================================================================================
    DN                                                 Description           Speed    MTU  
    -------------------------------------------------- --------------------  ------  ------
    topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
    topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
    topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 


    Exercise 2
    Use the data to create a similar table which displays the average / max number of
    passengers per month per airline traveling through BWI airport. Format number numbers
    to 2 decimal places as needed.

    Read from https://opendata.maryland.gov/resource/6jva-hr4v.json
    """

def read_json():
    pass

if __name__=="__main__":
    try:
        json_actions()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()