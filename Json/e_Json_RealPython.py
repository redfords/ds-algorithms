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

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    todos_format = json.dumps(todos, indent=4)
    print(todos_format)

    # json.loads takes in a string and returns a json object
    # json.dumps takes in a json object and returns a string

    """
    {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
    }
    """
    # Map of userId to number of complete TODOs for that user
    todos_by_user = {}

    # Increment complete TODOs count for each user.
    for todo in todos:
        if todo["completed"]:
            try:
                # Increment the existing user's count.
                todos_by_user[todo["userId"]] += 1
            except KeyError:
                # This user has not been seen. Set their count to 1.
                todos_by_user[todo["userId"]] = 1
    print(todos_by_user)

    # Create a sorted list of (userId, num_complete) pairs.
    top_users = sorted(todos_by_user.items(), 
                    key=lambda x: x[1], reverse=True)
    print(top_users)

    # Get the maximum number of complete TODOs.
    max_complete = top_users[0][1]
    print(max_complete)

    # Create a list of all users who have completed
    # the maximum number of TODOs.
    users = []
    for user, num_complete in top_users:
        if num_complete < max_complete:
            break
        users.append(str(user))

    max_users = " and ".join(users)
    print(max_users)

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