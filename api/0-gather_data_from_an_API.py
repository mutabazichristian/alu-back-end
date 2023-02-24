#!/usr/bin/python3
#this is a script that takes in a system argument as employee id and iterates through an api to find out which tasks he has completed
import requests
import sys

#getting id from system arguments
employee_ID = sys.argv[1];

url = 'https://jsonplaceholder.typicode.com/todos';
# sending request to api
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    # initialize a dictionary to store the completed task count for each employee
    employee_completed_tasks = {}
    
    # loop through each task in the response
    for task in data:
        employee_id = task['userId']
        completed = task['completed']
        
        # if the task is completed, increment the counter for the employee
        if completed:
            if employee_id in employee_completed_tasks:
                employee_completed_tasks[employee_id] += 1
            else:
                employee_completed_tasks[employee_id] = 1
    
    # print the completed task count for each employee
    for employee_id, completed_tasks in employee_completed_tasks.items():
        print(f"Employee {employee_id} is done with {completed_tasks} tasks.")
else:
    print('Error:', response.status_code)
