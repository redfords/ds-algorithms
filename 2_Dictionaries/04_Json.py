import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

"""
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
}
"""

