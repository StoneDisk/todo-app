import streamlit as st
import todosutils

todo_list = todosutils.get_todos()


def add_todo():
    todo_item = st.session_state['task_input'] + '\n'
    todo_list.append(todo_item)
    todosutils.write_todos(todo_list)


st.title("Todo App")
st.subheader("This is a minimal todo app")
st.write("Use this app to remember daily tasks.")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="**Enter a task:** ", placeholder="Add a new task...",
              key='task_input', on_change=add_todo)

# print("Script executed.")

st.session_state
