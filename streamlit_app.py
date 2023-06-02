import streamlit as st
import pandas as pd

# Create a dataframe to store tasks
tasks_df = pd.DataFrame(columns=['Task Name', 'Department', 'Assigned To', 'Deadline', 'Details', 'Status'])

# Function to add a new task
def add_task(task_name, department, assigned_to, deadline, details):
    global tasks_df
    new_task = pd.Series([task_name, department, assigned_to, deadline, details, 'Pending'], index=tasks_df.columns)
    tasks_df = tasks_df.append(new_task, ignore_index=True)

# Function to update task status
def update_task_status(index, status):
    global tasks_df
    tasks_df.at[index, 'Status'] = status

# Function to delete a task
def delete_task(index):
    global tasks_df
    tasks_df = tasks_df.drop(index)

# Function to display tasks
def display_tasks():
    st.subheader('Tasks List')
    st.dataframe(tasks_df)

# Main function
def main():
    st.title('Tasks Tracker')

    task_name = st.text_input('Task Name')
    department = st.selectbox('Assigned to Department', ['Department A', 'Department B', 'Department C'])
    assigned_to = st.text_input('Assigned to')
    deadline = st.date_input('Deadline Date')
    details = st.text_area('Details')

    if st.button('Add Task'):
        add_task(task_name, department, assigned_to, deadline, details)
        st.success('Task added successfully!')

    display_tasks()

    if st.checkbox('Mark Task as Completed'):
        completed_task_index = st.number_input('Enter the index of the task to mark as completed', min_value=0, max_value=len(tasks_df)-1, value=0, step=1)
        update_task_status(completed_task_index, 'Completed')
        st.success('Task status updated!')

    if st.checkbox('Delete Task'):
        delete_task_index = st.number_input('Enter the index of the task to delete', min_value=0, max_value=len(tasks_df)-1, value=0, step=1)
        delete_task(delete_task_index)
        st.success('Task deleted successfully!')

if __name__ == '__main__':
    main()
