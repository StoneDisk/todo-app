import streamlit as st
import todosutils


todo_list = todosutils.get_todos()

st.title("Todo App")
st.subheader("This is a minimal todo app")
st.write("Use this app to remember daily tasks.")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new task...")
