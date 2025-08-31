import streamlit as st
import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def main():
    st.title('📝 Todo List Manager')
    if 'tasks' not in st.session_state:
        st.session_state.tasks = load_tasks()

    tasks = st.session_state.tasks

    st.subheader('Add a new task')
    new_task = st.text_input('Task title', key='new_task')
    if st.button('Add Task'):
        if new_task.strip():
            tasks.append({'title': new_task.strip(), 'done': False})
            save_tasks(tasks)
            st.rerun()
        else:
            st.warning('Task title cannot be empty.')

    st.subheader('Your Tasks')
    if not tasks:
        st.info('No tasks found.')
    else:
        for i, task in enumerate(tasks):
            col1, col2, col3 = st.columns([6,1,1])
            with col1:
                st.write(f"{i+1}. {task['title']}")
            with col2:
                if st.checkbox('Done', value=task['done'], key=f'done_{i}'):
                    task['done'] = True
                    save_tasks(tasks)
            with col3:
                if st.button('Delete', key=f'del_{i}'):
                    tasks.pop(i)
                    save_tasks(tasks)
                    st.rerun()

if __name__ == '__main__':
    main()
