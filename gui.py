import functions
from PySimpleGUI import *

label = Text("Type in a todo")

inputbox = InputText(tooltip="Enter todo", key="todo")

add_button = Button("Add")

edit_button = Button("Edit")

Show = Listbox(values=functions.get_todolist(),
               key="todolist",
               enable_events=True,
               size=[45, 10])


window = Window("TaskMaster",
                layout=[[label], [inputbox, add_button], [Show, edit_button]],
                font=("Helvetica", 20))


while True:
    event, value = window.read()
    if event == "Add":
        old_todo = value["todo"].strip()
        if old_todo != '':
            todolist = functions.get_todolist()
            new_todo = value["todo"].title() + '\n'
            todolist.append(new_todo)
            functions.write_todolist(todolist)
            window["todolist"].update(values=todolist)
            window["todo"].update(value='')
        else:
            continue
    elif event == "Edit":
        edit_todo = value["todolist"][0]
        new_todo = value["todo"].title() + '\n'
        todolist = functions.get_todolist()
        ind = todolist.index(edit_todo)
        todolist[ind] = new_todo
        functions.write_todolist(todolist)
        window['todolist'].update(values=todolist)
        window["todo"].update(value='')
    elif event == 'todolist':
        window['todo'].update(value=value['todolist'][0])
    elif event == WIN_CLOSED:
        break

window.close()
