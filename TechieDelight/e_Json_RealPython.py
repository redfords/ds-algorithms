import json
import requests
import traceback
import sys

def encode():

    """
    json encoder and decoder: https://docs.python.org/3/library/json.html#basic-usage
    """

    data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }

    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

    json_string = json.dumps(data, indent=4)
    print(json_string)

    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)

    json_string = """
    {
        "researcher": {
            "name": "Ford Prefect",
            "species": "Betelgeusian",
            "relatives": [
                {
                    "name": "Zaphod Beeblebrox",
                    "species": "Betelgeusian"
                }
            ]
        }
    }
    """
    data = json.loads(json_string)
    print(data)

def test():

    """
    json fake data for practice purposes: https://jsonplaceholder.typicode.com/
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)

if __name__=="__main__":
    try:
        encode()
        test()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()