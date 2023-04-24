#!/usr/bin/python3
"""This script sends a request to an api and exports the
response
"""
import csv
import requests
from sys import argv


def export_data_csv(emp_id: int):
    """returns data about and employee from an api and exports
    it to csv file
    """

    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)

    payload = {"userId": emp_id}
    # make requests via the APIs
    todo = requests.get(url_todo, params=payload).json()
    user = requests.get(url_users).json()

    username = user.get("username")
    user_id = user.get("id")
    file_name = "{}.csv".format(user.get("id"))

    # exports data to csv file
    with open(file_name, mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)

        for task in todo:
            list_write = [
                user_id,
                username,
                task.get("completed"),
                task.get("title"),
            ]
            writer.writerow(list_write)


if __name__ == "__main__":
    export_data_csv(argv[1])
