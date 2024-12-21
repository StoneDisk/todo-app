import todosutils
import FreeSimpleGUI as sg


label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Type task here")
add_button = sg.Button("Add")

window = sg.Window("Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

