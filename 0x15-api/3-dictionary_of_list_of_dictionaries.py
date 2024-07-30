#!/usr/bin/python3

import json
import requests


def fetch_and_export_tasks():
    # API URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    # Fetch data from APIs
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        raise Exception("Error fetching data from API")

    users = users_response.json()
    todos = todos_response.json()

    # Dictionary to store tasks per user
    tasks_dict = {}
    # Process users and tasks
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos if todo["userId"] == user_id
        ]
        tasks_dict[user_id] = user_tasks
    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_dict, json_file)


# Execute the function
fetch_and_export_tasks()
