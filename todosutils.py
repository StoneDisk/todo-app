FILEPATH = 'resources/data/todos.txt'


# Read text file
def get_todos(file_path=FILEPATH):
    with open(file_path, 'r') as file:
        todos_list = file.readlines()
    return todos_list


# Write the list items to text file
def write_todos(list, file_path=FILEPATH):
    with open(file_path, 'w') as file:
        file.writelines(list)


if __name__ == "__main__":
    print("This is the todoutils module.")
    print("It contains functions for dealing with creation of todo lists.")
