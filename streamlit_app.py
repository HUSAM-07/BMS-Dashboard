import streamlit as st
import pandas as pd

# Create a list of tasks
tasks = [
  {"title": "Task 1", "description": "This is the first task.", "status": "Incomplete"},
  {"title": "Task 2", "description": "This is the second task.", "status": "Incomplete"},
  {"title": "Task 3", "description": "This is the third task.", "status": "Incomplete"}
]

# Create a table of tasks
df = pd.DataFrame(tasks)
df = df.set_index("title")

# Display the table of tasks
st.table(df)

# Add a new task
def add_task():
  title = st.text_input("Title")
  description = st.text_input("Description")
  status = st.selectbox("Status", ["Incomplete", "Complete"])

  if title and description and status:
    tasks.append({"title": title, "description": description, "status": status})

# Delete a task
def delete_task():
  title = st.selectbox("Select a task to delete", tasks)

  if title:
    tasks.remove(title)

# Update a task
def update_task():
  title = st.selectbox("Select a task to update", tasks)

  if title:
    description = st.text_input("New description")
    status = st.selectbox("New status", ["Incomplete", "Complete"])

    tasks[title]["description"] = description
    tasks[title]["status"] = status

# Add a button to add a new task
if st.button("Add Task"):
  add_task()

# Add a button to delete a task
if st.button("Delete Task"):
  delete_task()

# Add a button to update a task
if st.button("Update Task"):
  update_task()
