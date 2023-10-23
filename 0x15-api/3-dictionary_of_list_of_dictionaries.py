#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""

import json
import requests

import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    users = requests.get(url).json()

    dict_my = {}
    for user in users:
        user_my = user.get('id')
        username = user.get('username')

        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_my)
        url = url + '/todos/'
        tasks = requests.get(url).json()

        dict_my[user_my] = []
        for task in tasks:
            dict_my[user_my].append({

                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict_my, file)
