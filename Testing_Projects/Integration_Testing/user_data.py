# user_data.py

import requests

def get_user_data(token):
    if token == "token123":
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        return response.json()
    else:
        return None
