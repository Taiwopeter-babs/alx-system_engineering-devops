#!/usr/bin/python3
"""This script sends a request to an api and exports the
response
"""
import json
import requests


def export_all_data_json():
    """returns data about and employee from an api and exports
    it to json file
    """

    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    url_users = "https://jsonplaceholder.typicode.com/users/"

    try:
        # payload1 = {"userId": emp_id}
        # payload2 = {"id": emp_id}

        # make requests via the APIs
        resp_todo = requests.get(url_todo)
        resp_user = requests.get(url_users)

        # deserialize the responses
        emp_todo = resp_todo.json()
        emp_info = resp_user.json()

        # list of employees
        users = [user.get("username") for user in emp_info]

        idx = curr_pos = 0
        user_id = 1
        employees_dict = {}

        while user_id <= 10:

            emp_tasks = []  # list of each employee tasks

            pos = curr_pos
            count = 0
            while pos < len(emp_todo):

                """since the amount of tasks per employee is known,
                a definite limit is used
                """
                if count < 20:
                    info_dict = {
                        "username": users[idx],
                        "task": emp_todo[pos].get("title"),
                        "completed": emp_todo[pos].get("completed"),
                    }
                    emp_tasks.append(info_dict)
                else:
                    break
                count += 1
                pos += 1
            curr_pos = pos
            employees_dict.update({str(user_id): emp_tasks})

            user_id += 1
            idx += 1

        file_name = "todo_all_employees.json"

        # export data to json file
        with open(file_name, mode="w", encoding="utf-8") as json_file:
            json.dump(employees_dict, json_file)

    except requests.exceptions.RequestException:
        return


if __name__ == "__main__":
    export_all_data_json()
