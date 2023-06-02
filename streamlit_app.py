import streamlit as st

# Create a list to store tasks
tasks = []

# Departments
departments = ['Technical', 'Marketing', 'Office Bearers','Sponsorships']

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
    st.title("Organization Task Dashboard")
    <iframe
     src="https://husam007.notion.site/BMS-Dubai-Main-Dashboard-5d9bd82d7ec34cb8bbff0df0e0cfebdd/?embed=true"
     height="450"
     style="width:100%;border:none;"
     ></iframe>

    # Sidebar to add new tasks
    st.sidebar.header("Add New Task")
    new_task = st.sidebar.text_input("Enter task")
    department = st.sidebar.selectbox("Department Assigned To", departments)
    assigned_to = st.sidebar.multiselect("Assigned To", assignees)
    date_to_be_completed = st.sidebar.date_input("Date to be Completed")
    task_description = st.sidebar.text_area("Task Description")
    add_button = st.sidebar.button("Add Task")

    if add_button and new_task != "":
        task = f"**Task:** {new_task}\n" \
               f"**Department:** {department}\n" \
               f"**Assigned To:** {', '.join(assigned_to)}\n" \
               f"**Date to be Completed:** {date_to_be_completed}\n" \
               f"**Task Description:** {task_description}"
        add_task(task)
        st.sidebar.success("Task added successfully!")

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
                st.sidebar.success("Task marked as completed!")

if __name__ == "__main__":
    main()