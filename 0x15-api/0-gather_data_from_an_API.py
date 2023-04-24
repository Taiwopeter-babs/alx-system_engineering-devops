#!/usr/bin/python3
"""This script sends a request to an api and prints the
response
"""
import requests
from sys import argv


def gather_data(emp_id: int):
    """returns data about and employee from an api"""

    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)

    try:
        completed = 0
        payload = {"userId": emp_id}

        # make requests via the APIs
        todo = requests.get(url_todo, params=payload).json()
        resp_user = requests.get(url_users).json()

        # get the total number of tasks for employee and the employee's name
        emp_name = resp_user.get("name")

        # get the completed tasks
        completed = [task.get("title") for task in todo if task.get("completed")]
        total = len(completed)
        # output
        first_line = "Employee {} is done with tasks({}/{}):"
        print(first_line.format(emp_name, total, len(todo)))

        # print the title of the completed tasks
        [print("\t {}".format(task)) for task in completed]

    except requests.exceptions.RequestException:
        return


if __name__ == "__main__":
    try:
        emp_id = argv[1]

        if emp_id.isdigit():
            emp_id = int(emp_id)
            gather_data(emp_id)
    except IndexError:
        pass
