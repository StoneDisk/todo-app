import todosutils
import FreeSimpleGUI as fsg


label = fsg.Text("Enter a task")
input_box = fsg.InputText(tooltip="Type task here")
add_button = fsg.Button("Add")

window = fsg.Window("Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

