from todosutils import get_todos, write_todos

print("Todo List App\n")

user_prompt = "Enter a task to complete: "
# todos = []
exit_char = 'q'

while True:
    print("Choose an action to proceed.") 
    print("Type \"add <task>\" to add a task, \"show\" to show current todo list, \"edit <list_no.>\" to edit an item,")
    print("\"done <list_no.>\" to mark an item as complete or \"quit\" to exit the program.")
    user_choice = input("Action: ").lower().strip()
    print()

    if user_choice.startswith('add'):
        todo = user_choice[4:]
        print(todo.capitalize())
        print()

        todos = get_todos()
            
        todos.append(todo + '\n')

        write_todos(todos)
        

    elif user_choice.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item.capitalize()}")

        print()

    elif user_choice.startswith('edit'):
        try:
            list_number = int(user_choice[5:])
            list_number = list_number - 1
            todos = get_todos()
                
            item_to_edit = todos[list_number]
            print(f"This is the item you want to replace -> '{item_to_edit.strip('\n')}'")

            new_item = input("Enter a replacement for the chosen item: ")
            todos[list_number] = new_item + '\n'

            # Write changes to text file
            write_todos(todos)

            print()
        except ValueError:
            print("Your command is not valid. Please follow this syntax for 'edit' command")
            print("edit <no._of_item_in_todo_list>")
            print("Ex: edit 3")
            print()
            continue

    elif user_choice.startswith('done'):
        try:
            list_no = int(user_choice[5:])

            todos = get_todos()

            list_item = todos.pop(list_no - 1)

            # Write changes to the text file
            write_todos(todos)
                
            print(f"item no.{list_no} with the content: '{list_item.strip('\n')}' has been marked as complete and " +
                "removed from the list.")
            # print("removed from the list.")
            print()
        except IndexError:
            print("That item no. does not exist.")
            print()
            continue

    elif user_choice.startswith('quit'):
        break
    else:
        print("You have entered an unknown command!")
            
print("Goodbye!")

