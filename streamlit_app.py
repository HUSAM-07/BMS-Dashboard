```python
import streamlit as st
import pandas as pd

# Create a list of tasks
tasks = []

# Create a table of tasks
df = pd.DataFrame(tasks)
df = df.set_index("title")

# Display the table of tasks
st.table(df)

# Add a new task
def add_task():
  title = st.text_input("Title")
  description = st.markdown("Description")
  status = st.selectbox("Status", ["Incomplete", "Complete"])
  assigned_to_department = st.text_input("Assigned to Department")
  assigned_to = st.text_input("Assigned to")

  if title and description and status and assigned_to_department and assigned_to:
    tasks.append({"title": title, "description": description, "status": status, "assigned_to_department": assigned_to_department, "assigned_to": assigned_to})

# Delete a task
def delete_task():
  title = st.selectbox("Select a task to delete", tasks)

  if title:
    tasks.remove(title)

# Update a task
def update_task():
  title = st.selectbox("Select a task to update", tasks)

  if title:
    description = st.markdown("New Description")
    status = st.selectbox("New status", ["Incomplete", "Complete"])
    assigned_to_department = st.text_input("New Assigned to Department")
    assigned_to = st.text_input("New Assigned to")

    tasks[title]["description"] = description
    tasks[title]["status"] = status
    tasks[title]["assigned_to_department"] = assigned_to_department
    tasks[title]["assigned_to"] = assigned_to

# Add a button to add a new task
if st.button("Add Task"):
  add_task()

# Add a button to delete a task
if st.button("Delete Task"):
  delete_task()

# Add a button to update a task
if st.button("Update Task"):
  update_task()

# Add a timeline view based off a monthly overlook
if st.checkbox("Show timeline view"):
  st.line_chart(df.set_index("status"))



