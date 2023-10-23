#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""

import json
import requests

import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_rl + "/" + sys.argv[1]

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {sys.argv[1]: []}
    for task in tasks:
        dictionary[sys.argv[1]].append({
            "task": task.get('title'),

            "completed": task.get('completed'),

            "username": username
        })
    with open('{}.json'.format(sys.argv[1]), 'w') as filename:
        json.dump(dictionary, filename)
