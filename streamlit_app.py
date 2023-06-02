import streamlit as st
import pandas as pd

# Create a database to store the tasks
db = pd.DataFrame({
    "Task Name": [],
    "Task Assigned to Department": [],
    "Task Assigned to": [],
    "Deadline Date": [],
    "Details": [],
    "Task Status": []
})

# Create a function to add a new task
def add_task():
    task_name = st.text_input("Task Name")
    task_assigned_to_department = st.text_input("Task Assigned to Department")
    task_assigned_to = st.text_input("Task Assigned to")
    deadline_date = st.date_input("Deadline Date")
    details = st.text_area("Details")
    task_status = st.radio("Task Status", ("Pending", "Completed"))

    # Add the task to the database
    db = db.append({
        "Task Name": task_name,
        "Task Assigned to Department": task_assigned_to_department,
        "Task Assigned to": task_assigned_to,
        "Deadline Date": deadline_date,
        "Details": details,
        "Task Status": task_status
    }, ignore_index=True)

# Create a function to update a task
def update_task(task_id):
    task = db[db["Task ID"] == task_id]

    task_name = st.text_input("Task Name", task["Task Name"])
    task_assigned_to_department = st.text_input("Task Assigned to Department", task["Task Assigned to Department"])
    task_assigned_to = st.text_input("Task Assigned to", task["Task Assigned to"])
    deadline_date = st.date_input("Deadline Date", task["Deadline Date"])
    details = st.text_area("Details", task["Details"])
    task_status = st.radio("Task Status", ("Pending", "Completed"), value=task["Task Status"])

    # Update the task in the database
    db.loc[db["Task ID"] == task_id, ["Task Name", "Task Assigned to Department", "Task Assigned to", "Deadline Date", "Details", "Task Status"]] = [task_name, task_assigned_to_department, task_assigned_to, deadline_date, details, task_status]

# Create a function to delete a task
def delete_task(task_id):
    db = db[db["Task ID"] != task_id]

# Create a function to mark a task as completed
def mark_task_as_completed(task_id):
    db.loc[db["Task ID"] == task_id, "Task Status"] = "Completed"

# Display the tasks in a table
st.table(db)

# Add a new task button
if st.button("Add New Task"):
    add_task()

# Update a task button
if st.button("Update Task"):
    task_id = st.number_input("Task ID")
    update_task(task_id)

# Delete a task button
if st.button("Delete Task"):
    task_id = st.number_input("Task ID")
    delete_task(task_id)

# Mark a task as completed button
if st.button("Mark Task as Completed"):
    task_id = st.number_input("Task ID")
    mark_task_as_completed(task_id)
