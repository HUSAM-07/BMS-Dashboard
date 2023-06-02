import streamlit as st
import pandas as pd

# Create a database of tasks
tasks = pd.DataFrame({
    'Task Name': ['Task 1', 'Task 2', 'Task 3'],
    'Task Assigned to Department': ['Department 1', 'Department 2', 'Department 3'],
    'Task Assigned to': ['Employee 1', 'Employee 2', 'Employee 3'],
    'Deadline Date': ['2023-06-03', '2023-06-04', '2023-06-05'],
    'Details': ['This is the details for Task 1.', 'This is the details for Task 2.', 'This is the details for Task 3.'],
    'Task Status': ['Not Started', 'In Progress', 'Completed']
})

# Display the tasks in a table
st.table(tasks)

# Add a new task
def add_task():
    task_name = st.text_input('Task Name')
    task_assigned_to_department = st.selectbox('Task Assigned to Department', tasks['Task Assigned to Department'].unique())
    task_assigned_to = st.selectbox('Task Assigned to', tasks['Task Assigned to'].unique())
    deadline_date = st.date_input('Deadline Date')
    details = st.text_area('Details')
    task_status = st.selectbox('Task Status', tasks['Task Status'].unique())

    new_task = {
        'Task Name': task_name,
        'Task Assigned to Department': task_assigned_to_department,
        'Task Assigned to': task_assigned_to,
        'Deadline Date': deadline_date,
        'Details': details,
        'Task Status': task_status
    }

    tasks = tasks.append(new_task, ignore_index=True)

# Update a task
def update_task():
    task_id = st.selectbox('Select a task to update', tasks['Task Name'].unique())
    task = tasks[tasks['Task Name'] == task_id]

    task_name = st.text_input('Task Name', value=task['Task Name'])
    task_assigned_to_department = st.selectbox('Task Assigned to Department', tasks['Task Assigned to Department'].unique(), value=task['Task Assigned to Department'])
    task_assigned_to = st.selectbox('Task Assigned to', tasks['Task Assigned to'].unique(), value=task['Task Assigned to'])
    deadline_date = st.date_input('Deadline Date', value=task['Deadline Date'])
    details = st.text_area('Details', value=task['Details'])
    task_status = st.selectbox('Task Status', tasks['Task Status'].unique(), value=task['Task Status'])

    tasks.loc[tasks['Task Name'] == task_id, 'Task Name'] = task_name
    tasks.loc[tasks['Task Name'] == task_id, 'Task Assigned to Department'] = task_assigned_to_department
    tasks.loc[tasks['Task Name'] == task_id, 'Task Assigned to'] = task_assigned_to
    tasks.loc[tasks['Task Name'] == task_id, 'Deadline Date'] = deadline_date
    tasks.loc[tasks['Task Name'] == task_id, 'Details'] = details
    tasks.loc[tasks['Task Name'] == task_id, 'Task Status'] = task_status

# Delete a task
def delete_task():
    task_id = st.selectbox('Select a task to delete', tasks['Task Name'].unique())
    tasks = tasks[tasks['Task Name'] != task_id]

# Mark a task as completed
def mark_task_as_completed():
    task_id = st.selectbox('Select a task to mark as completed', tasks
