import streamlit as st
import pandas as pd

#wide layout
st. set_page_config(layout="wide")

# Load the tasks data
tasks = pd.read_csv("tasks.csv")

# Create a function to add a new task
def add_task():
  task_name = st.text_input("Task name")
  status = st.selectbox("Status", ["Not Started", "In Progress", "Done"])
  assignee = st.text_input("Assignee")
  due_date = st.date_input("Due date")
  priority = st.selectbox("Priority", ["Low", "Medium", "High"])
  summary = st.text_area("Summary")
  tags = st.text_input("Tags")
  project = st.text_input("Project")
  parent_task = st.text_input("Parent task")
  sub_tasks = st.text_input("Sub tasks")

  if st.button("Add task"):
    new_task = {
      "task_name": task_name,
      "status": status,
      "assignee": assignee,
      "due_date": due_date,
      "priority": priority,
      "summary": summary,
      "tags": tags,
      "project": project,
      "parent_task": parent_task,
      "sub_tasks": sub_tasks
    }
    tasks = tasks.append(new_task, ignore_index=True)
    df = pd.DataFrame(tasks)
    df.to_csv("tasks.csv", index=False)

# Create a function to update a task
def update_task():
  task_id = st.selectbox("Select task to update", tasks["task_name"])
  task = tasks[tasks["task_name"] == task_id]

  task_name = st.text_input("Task name", task["task_name"])
  status = st.selectbox("Status", task["status"], task.columns)
  assignee = st.text_input("Assignee", task["assignee"])
  due_date = st.date_input("Due date", task["due_date"])
  priority = st.selectbox("Priority", task["priority"], task.columns)
  summary = st.text_area("Summary", task["summary"])
  tags = st.text_input("Tags", task["tags"])
  project = st.text_input("Project", task["project"])
  parent_task = st.text_input("Parent task", task["parent_task"])
  sub_tasks = st.text_input("Sub tasks", task["sub_tasks"])

  if st.button("Update task"):
    task["task_name"] = task_name
    task["status"] = status
    task["assignee"] = assignee
    task["due_date"] = due_date
    task["priority"] = priority
    task["summary"] = summary
    task["tags"] = tags
    task["project"] = project
    task["parent_task"] = parent_task
    task["sub_tasks"] = sub_tasks
    tasks.loc[tasks["task_name"] == task_id] = task
    df = pd.DataFrame(tasks)
    df.to_csv("tasks.csv", index=False)

# Create a function to delete a task
def delete_task():
  task_id = st.selectbox("Select task to delete", tasks["task_name"])
  tasks = tasks[tasks["task_name"] != task_id]
  df = pd.DataFrame(tasks)
  df.to_csv("tasks.csv", index=False)

# Display the tasks
st.title("BMS Task Tracker & Project Timeline")
st.table(tasks)

# Add a new task
if st.button("Add task"):
  add_task()

# Update a task
if st.button("Update task"):
  update_task()

# Delete a task
if st.button("Delete task"):
  delete_task()

  st.caption("This App is Designed & Developed by HUSAM")
