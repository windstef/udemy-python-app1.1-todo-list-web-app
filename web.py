# Section 19: Day 19: App 1 - Build a Todo List App | #web-apps
# 185
# Deploying the Web App to the Cloud


# following

# Section 19:
# 184
# Completing Todo Items on the Web App
from tabnanny import check



# How to run:
# terminal:
# streamlit run web.py

# generate the requirements.txt file via command:
# pip freeze > requirements.txt


# Q. what is requirements.txt?

# This is a file which will be uploaded to the server
# where we host this web app.
# So that server should know
# all the Python libraries the server needs to install
# in order to run the web app correctly.

# show the list of those packages in the command line:
# pip freeze




#######################################

import streamlit as st
from streamlit import checkbox

import functions

print("Hello from header")

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"    # st.session_state is sort of dictionary of streamlit
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# st.checkbox("Buy grocery.")
# st.checkbox("Throw the trash")

for index, todo in enumerate(todos):
    # st.checkbox(todo)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')

# print("Hello from bottom")

# st.session_state