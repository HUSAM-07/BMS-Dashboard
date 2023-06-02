import streamlit as st
import pandas as pd

# Create a list to store tasks
tasks = []

# Departments
departments = ['Department A', 'Department B', 'Department C']

# Assignees
assignees = ['John', 'Jane', 'Mike', 'Emily']

# Function to add a task
def add_task(task):
    tasks.append(task)

# Streamlit app layout
def main():
    st.title("Organization Task Dashboard")

    # Sidebar to add new tasks
    st.sidebar.header("Add New Task")
    new_task = st.sidebar.text_input("Enter task")
    department = st.sidebar.selectbox("Department Assigned To", departments)
    assigned_to = st.sidebar.multiselect("Assigned To", assignees)
    date_to_be_completed = st.sidebar.date_input("Date to be Completed")
    task_description = st.sidebar.text_area("Task Description")
    add_button = st.sidebar.button("Add Task")

    if add_button and new_task != "":
        task = {
            'Task': new_task,
            'Department': department,
            'Assigned To': ', '.join(assigned_to),
            'Date to be Completed': date_to_be_completed,
            'Task Description': task_description,
            'Status': 'In Progress'
        }
        add_task(task)
        st.sidebar.success("Task added successfully!")

    # Display the list of tasks in a table
    st.header("Tasks")
    if len(tasks) == 0:
        st.info("No tasks added yet.")
    else:
        df = pd.DataFrame(tasks)
        st.table(df)

if __name__ == "__main__":
    main()
