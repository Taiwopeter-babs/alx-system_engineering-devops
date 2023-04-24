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

    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    url_users = "https://jsonplaceholder.typicode.com/users/"

    try:
        payload1 = {"userId": emp_id}
        payload2 = {"id": emp_id}

        # make requests via the APIs
        resp_todo = requests.get(url_todo, params=payload1)
        resp_user = requests.get(url_users, params=payload2)

        # deserialize the responses
        emp_todo = resp_todo.json()
        emp_info = resp_user.json()[0]

        username = emp_info.get("username")
        user_id = emp_info.get("id")
        file_name = "{}.csv".format(emp_info.get("id"))

        # exports data to csv file
        with open(file_name, mode="w") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)

            for task in emp_todo:
                list_write = [
                    user_id,
                    username,
                    task.get("completed"),
                    task.get("title"),
                ]
                writer.writerow(list_write)

    except requests.exceptions.RequestException:
        print(resp_todo.status_code)


if __name__ == "__main__":
    try:
        emp_id = argv[1]

        if emp_id.isdigit():
            emp_id = int(emp_id)
            export_data_csv(emp_id)
    except IndexError:
        pass
