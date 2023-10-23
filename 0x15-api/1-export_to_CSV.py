#!/usr/bin/python3
""" script to export task #0 data in the CSV format."""

import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + sys.argv[1]

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)

    tasks = response.json()

    with open('{}.csv'.format(sys.argv[1]), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'

                       .format(sys.argv[1], username, task.get('completed'),
                               task.get('title')))
