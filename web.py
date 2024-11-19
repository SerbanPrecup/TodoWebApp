import streamlit as st
from streamlit.web.cli import activate

import functions as f
todos = f.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    f.write_todos(todos)



st.title("My Todo App")

st.subheader("This is my todo App.")

st.write("This app is to increase your productivity.")

for todo in todos:
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="",placeholder="Add a new todo...",on_change=add_todo,key="new_todo")



# st.checkbox("Buy")
# st.checkbox("Bu2y")