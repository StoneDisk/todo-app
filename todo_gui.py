import todosutils
import FreeSimpleGUI as sg


label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Type task here")
add_button = sg.Button("Add")

layout = [[label], [input_box, add_button]]

window = sg.Window("Todo App", layout)
window.read()
window.close()

