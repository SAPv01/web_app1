import time

today = time.strftime("%b %d, %Y, %H:%M:%S")
print(f"Greetings. Today is {today}")


def read_file(filepath="todos.txt"):
    """
    This function fetches the lines from the file specified in the default arg.
    These lines will be stored in a list variable of your specification.

    """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_file(todos_list, filepath="todos.txt"):
    """
    Updates the pre-existing lines in the file specified in the filepath
    by writing the new lines in the file.

    """
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_list)
