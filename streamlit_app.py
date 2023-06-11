import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load the YAML file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Render the login widget
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome {name}')
    st.title('Organization Task Dashboard')

    # Create a list to store tasks
    tasks = []

    # Departments
    departments = ['Technical', 'Marketing', 'Office Bearers', 'Sponsorships']

    # Assignees
    assignees = ['HUSAM', 'Sanjay', 'Marshal', 'Sai']

    # Function to add a task
    def add_task(task):
        tasks.append(task)

    # Function to mark a task as completed
    def complete_task(task_index):
        if task_index < len(tasks):
            tasks[task_index] = f"✅ {tasks[task_index]}"

    # Streamlit app layout
    def main():
        st.header("Add New Task")
        new_task = st.text_input("Enter task")
        department = st.selectbox("Department Assigned To", departments)
        assigned_to = st.multiselect("Assigned To", assignees)
        date_to_be_completed = st.date_input("Date to be Completed")
        task_description = st.text_area("Task Description")
        add_button = st.button("Add Task")

        if add_button and new_task != "":
            task = f"**Task:** {new_task}\n" \
                f"**Department:** {department}\n" \
                f"**Assigned To:** {', '.join(assigned_to)}\n" \
                f"**Date to be Completed:** {date_to_be_completed}\n" \
                f"**Task Description:** {task_description}"
            add_task(task)
            st.success("Task added successfully!")

        # Display the list of tasks
        st.header("Tasks")
        if len(tasks) == 0:
            st.info("No tasks added yet.")
        else:
            for i, task in enumerate(tasks):
                st.write(f"{i+1}. {task}")

                # Checkbox to mark a task as completed
                complete_checkbox = st.checkbox("Complete", key=f"complete_checkbox_{i}")
                if complete_checkbox:
                    complete_task(i)
                    st.success("Task marked as completed!")

    if __name__ == "__main__":
        main()

else:
    st.error('Username/password is incorrect')
