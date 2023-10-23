#!/usr/bin/python3
""" script to use REST API to give employee ID"""

import requests

import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + sys.argv[1]

    response = requests.get(url)
    em_Name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)

    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(em_Name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
