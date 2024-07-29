#!/usr/bin/python3
"""
This script fetches and displays TODO list progress for a given employee ID.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    """
    try:
        # Fetch employee details
        user_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        user_response = requests.get(user_url)
        user_data = user_response.json()

        employee_name = user_data.get('name')

        # Fetch TODO list for the employee
        todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        completed_tasks = [
            task for task in todos_data if task.get('completed')
        ]
        num_completed_tasks = len(completed_tasks)

        # Display the result
        print(
            f"Employee {employee_name} is done with tasks("
            f"{num_completed_tasks}/{total_tasks}):"
        )
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
