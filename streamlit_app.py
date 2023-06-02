import streamlit as st
import pandas as pd

# Function to add a new task
def add_task(task_name, department, assigned_to, deadline, details, tasks_df):
    new_task = pd.DataFrame(
        [[task_name, department, assigned_to, deadline, details, 'Pending']],
        columns=tasks_df.columns
    )
    tasks_df = pd.concat([tasks_df, new_task], ignore_index=True)
    return tasks_df

# Function to update task status
def update_task_status(index, status, tasks_df):
    tasks_df.at[index, 'Status'] = status
    return tasks_df

# Function to delete a task
def delete_task(index, tasks_df):
    tasks_df = tasks_df.drop(index)
    tasks_df.reset_index(drop=True, inplace=True)
    return tasks_df

# Function to display tasks
def display_tasks(tasks_df):
    st.subheader('Tasks List')
    st.dataframe(tasks_df)

# Main function
def main():
    st.title('Tasks Tracker')

    # Load existing tasks from a file or database
    tasks_df = pd.DataFrame(columns=['Task Name', 'Department', 'Assigned To', 'Deadline', 'Details', 'Status'])

    task_name = st.text_input('Task Name')
    department = st.selectbox('Assigned to Department', ['Department A', 'Department B', 'Department C'])
    assigned_to = st.text_input('Assigned to')
    deadline = st.date_input('Deadline Date')
    details = st.text_area('Details')

    if st.button('Add Task'):
        tasks_df = add_task(task_name, department, assigned_to, deadline, details, tasks_df)
        st.success('Task added successfully!')

    display_tasks(tasks_df)

    if st.checkbox('Mark Task as Completed'):
        completed_task_index = st.number_input('Enter the index of the task to mark as completed', min_value=0, max_value=len(tasks_df)-1, value=0, step=1)
        tasks_df = update_task_status(completed_task_index, 'Completed', tasks_df)
        st.success('Task status updated!')

    if st.checkbox('Delete Task'):
        delete_task_index = st.number_input('Enter the index of the task to delete', min_value=0, max_value=len(tasks_df)-1, value=0, step=1)
        tasks_df = delete_task(delete_task_index, tasks_df)
        st.success('Task deleted successfully!')

if __name__ == '__main__':
    main()
