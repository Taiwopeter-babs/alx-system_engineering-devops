#!/usr/bin/python3
"""This script sends a request to an api and prints the
response
"""
import requests
from sys import argv


def gather_data(emp_id):
    """returns data about and employee from an api"""

    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url_users = "https://jsonplaceholder.typicode.com/users/{}"

    payload = {"userId": emp_id}

    # make requests via the APIs
    todo = requests.get(url_todo.format(emp_id)).json()
    resp_user = requests.get(url_users.format(emp_id)).json()

    # get the total number of tasks for employee and the employee's name
    emp_name = resp_user.get("name")

    # get the completed tasks
    done = [task.get("title") for task in todo if task.get("completed")]
    # output
    first_line = "Employee {} is done with tasks({}/{}):"
    print(first_line.format(emp_name, len(done), len(todo)))

    # print the title of the completed tasks
    [print("\t {}".format(task)) for task in done]


if __name__ == "__main__":
    gather_data(int(argv[1]))
