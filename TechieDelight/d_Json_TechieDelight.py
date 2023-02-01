import json
import requests
import sys
import traceback

def json_actions():
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




if __name__=="__main__":
    try:
        json_actions()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()


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

Read from http://data.maryland.gov/api/views/6jva-hr4v/rows.json?accessType=DOWNLOAD
"""

