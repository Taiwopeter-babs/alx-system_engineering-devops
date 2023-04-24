#!/usr/bin/python3
"""This script sends a request to an api and exports the
response
"""
import json
import requests
from sys import argv


def export_data_json(emp_id: int):
    """returns data about and employee from an api and exports
    it to json file
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
        file_name = "{}.json".format(emp_info.get("id"))

        # create a of tasks dictionary
        # print(emp_todo)
        tasks_list = []
        for task in emp_todo:
            kwargs = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            new_dict = dict(**kwargs)
            tasks_list.append(new_dict)
        task_dict = {str(user_id): tasks_list}

        # export data to json file
        with open(file_name, mode="w", encoding="utf-8") as json_file:
            json.dump(task_dict, json_file)

    except requests.exceptions.RequestException:
        return


if __name__ == "__main__":
    try:
        emp_id = argv[1]

        if emp_id.isdigit():
            emp_id = int(emp_id)
            export_data_json(emp_id)
    except IndexError:
        pass
