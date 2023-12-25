import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This app is to add, complete and edit todos ")
st.write("This will increase the productivity.")

for index, item in enumerate(todos):
    check = st.checkbox(item,key=item)
    if check:
        todos.pop(index)
        functions.write_todos(todos)

        del st.session_state[item]
        st.rerun()

st.text_input(label='Enter a todo', placeholder="Enter a todo..", label_visibility="hidden", on_change=add_todo,
              key="new_todo")

