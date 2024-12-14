print("Todo List App\n")

user_prompt = "Enter a task to complete: "
# todos = []
exit_char = 'q'

while True:
    print("Choose an action to proceed.") 
    print("Type \"add\" to add a task, \"show\" to show current todo list, \"edit\" to edit an item,")
    print("\"done\" to mark an item as complete or \"q\" to quit.")
    user_choice = input("Action: ").lower().strip()
    print()

    match user_choice:
        case "add":
            todo = input(user_prompt) + "\n"
            print(todo.capitalize())
            print()

            # Regular file access
            # file = open('resources/data/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            # File access using 'with' context manager
            # Read text file
            with open('resources/data/todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            # Write the added item to text file
            with open('resources/data/todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            # file access
            with open('resources/data/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item.capitalize()}")

            print()

        case "edit":
            list_number = int(input("Please enter the list no. of the item you want to edit: "))
            list_number = list_number - 1
            # Read text file
            with open('resources/data/todos.txt', 'r') as file:
                todos = file.readlines()
            
            item_to_edit = todos[list_number]
            print(f"This is the item you want to replace -> '{item_to_edit.strip('\n')}'")

            new_item = input("Enter a replacement for the chosen item: ")
            todos[list_number] = new_item + '\n'

            # Write changes to text file
            with open('resources/data/todos.txt', 'w') as file:
                file.writelines(todos)

            print()
        case "done":
            list_no = int(input("Please enter the list no. of the item you want to mark as complete: "))

            # Read text file
            with open('resources/data/todos.txt', 'r') as file:
                todos = file.readlines()

            list_item = todos.pop(list_no - 1)

            # Write changes to the text file
            with open('resources/data/todos.txt', 'w') as file:
                file.writelines(todos)
            
            print(f"item no.{list_no} with the content: '{list_item.strip('\n')}' has been marked as complete and " +
                  "removed from the list.")
            # print("removed from the list.")
            print()
        case "q":
            break
            
print("Goodbye!")

