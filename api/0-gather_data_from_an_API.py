#!/usr/bin/python3
"""Given employee ID, returns information about TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    _id = sys.argv[1]
    name_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    name = requests.get(name_url).json().get('name')
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        _id)
    todo = requests.get(todo_url)

    all_tasks = [task for task in todo.json()]
    completed = [task for task in todo.json() if task.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), len(all_tasks)))
    for task in completed:
        print("\t {}".format(task.get('title')))