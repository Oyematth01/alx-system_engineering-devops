#!/usr/bin/python3
"""
Fetch and display TODO list progress for a given employee ID.
Export the data to a CSV file.
"""
import csv
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

        if not user_data:
            print(f"User with ID {employee_id} not found.")
            return

        employee_name = user_data.get('username').strip()

        # Fetch TODO list for the employee
        todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Export to CSV
        file_name = f"{employee_id}.csv"
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([
                    employee_id,
                    employee_name,
                    task.get('completed'),
                    task.get('title')
                ])

        print(f"Data exported to {file_name}")

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
