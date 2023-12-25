FILEPATH = "todos_file.txt"


def get_todos(filepath=FILEPATH):
    """ Read the todos_file.txt and returns
        the todo items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the received argument to todos file
    """
    with open(filepath, 'w') as file_output:
        file_output.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello!")
