FILEPATH = "todos.txt"


# input: filepath (parameter)
# with default argument/parameter
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        # yellow underlined todos: Shadows name 'todos' from outer scope. And it's not a good idea to have this variable with the same name as in function.
        # todos = file.readlines()
        todos_local = file_local.readlines()
    return todos_local

# docstring
# print(help(get_todos))


# no return anything, except of None. Behaves as procedure.
# with default argument/parameter
# Hint: non-default parameter must not follows default parameters
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# docstring
# print(help(write_todos))

# print("I am outside!")

# print(__name__)     # __main__
# But its value is main
# only when we execute functions.py directly.

# When you run main.py
# and main.py runs functions.py
# through that import statement,
# then the value of name is the name of that file.
# Functions, in this case.
# But when you run functions.py directly
# the value of that variable is __main__.

# case, main.py = '134-Organising-the-Code-in-Modules.py'

# print(type(__name__))       # <class 'str'>
# it is executed in this script, directly
if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())

# code experiment: introduce an error
# print(x)