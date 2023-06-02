import streamlit as st

# Create a list to store tasks
tasks = []

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

    # Sidebar to add new tasks
    st.sidebar.header("Add New Task")
    new_task = st.sidebar.text_input("Enter task")
    add_button = st.sidebar.button("Add Task")

    if add_button and new_task != "":
        add_task(new_task)
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
