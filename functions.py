def get_todos(filename="todo.txt"):
    """Read a text file and return the list of 
    to-do items.
    """
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos,filename="todo.txt"):
    """Write a to-do items liast in
    a text file.
    """
    with open(filename, 'w') as file:
        file.writelines(todos)