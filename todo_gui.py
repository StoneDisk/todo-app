import todosutils as tu
import FreeSimpleGUI as sg


label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Type task here", key="user_input")
add_button = sg.Button("Add")

item_list = tu.get_todos()
list_box = sg.Listbox(values=item_list, 
                      key="items",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

layout = [[label], [input_box, add_button], [list_box, edit_button]]

window = sg.Window("Todo App", layout, font=("Helvetica", 16))

while True:
    event, values = window.read()
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
        case 'Edit': # incomplete case block, do not trigger!
            selected_item = values['items'][0]
            print(selected_item)

            rep_item = values["user_input"]

            todos = tu.get_todos()
            index = todos.index(selected_item)
            todos[index] = rep_item
            tu.write_todos(todos)
            window['items'].update(values=todos)
        case 'items':
            selected_item = values['items'][0]
            # mod_item = selected_item.split(' ', 1)[1]
            window['user_input'].update(value=selected_item)                  

window.close()
