#!/usr/bin/python3
import json
import requests

url_users = 'https://jsonplaceholder.typicode.com/users'
url_todos = 'https://jsonplaceholder.typicode.com/todos'

users = requests.get(url_users).json()
todos = requests.get(url_todos).json()

data = {}
for user in users:
    user_id = user['id']
    username = user['username']
    tasks = [
        {
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        }
        for task in todos if task['userId'] == user_id
    ]
    data[user_id] = tasks

with open('todo_all_employees.json', 'w') as f:
    json.dump(data, f)
