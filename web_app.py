import streamlit as st
import functions


todos = functions.read_file()


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_file(todos)


st.title("My todo App")
st.subheader("This is my todo app.")
st.text("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label_visibility="hidden", label="Enter a todo", placeholder="Add a new todo... ",
              on_change=add_todo, key='new_todo')
