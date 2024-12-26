import todosutils as tu
import FreeSimpleGUI as sg
import time


sg.theme("DarkGrey15")

clock_label = sg.Text("", key="clock")
task_input_label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Type task here", key="user_input")
add_button = sg.Button("Add", size=10)

item_list = tu.get_todos()
list_box = sg.Listbox(values=item_list, 
                      key="items",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit", key="Quit")

layout = [[clock_label], 
          [task_input_label], 
          [input_box, add_button], 
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("Todo App", layout, font=("Helvetica", 14))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    match event:
        case 'Add':
            todos = tu.get_todos()
            user_todo = values["user_input"] + "\n"
            todos.append(user_todo)
            tu.write_todos(todos)
            window['items'].update(values=todos)
        case 'Edit':
            try:
                selected_item = values['items'][0]
                print(selected_item)

                rep_item = values["user_input"]

                todos = tu.get_todos()
                index = todos.index(selected_item)
                todos[index] = rep_item
                tu.write_todos(todos)
                window['items'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 16))
        case 'Complete':
            try:
                item_to_remove = values['items'][0]
                todo_list = tu.get_todos()
                todo_list.remove(item_to_remove)
                tu.write_todos(todo_list)
                window['items'].update(values=todo_list)
                window['user_input'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 16))
        case 'items':
            selected_item = values['items'][0]
            # mod_item = selected_item.split(' ', 1)[1]
            window['user_input'].update(value=selected_item)                  

window.close()
