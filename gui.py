import functions
from PySimpleGUI import *
import time

theme("Topanga")

label = Text("Type in a todo")

clock = Text('', key='clock')

inputbox = InputText(tooltip="Enter todo", key="todo")

add_button = Button("Add", size=10)

edit_button = Button("Edit")

complete_button = Button("Complete")

exit_button = Button("Exit")

Show = Listbox(values=functions.get_todolist(),
               key="todolist",
               enable_events=True,
               size=[45, 10])


window = Window("TaskMaster",
                layout=[[clock], [label], [inputbox, add_button], [
                    Show, edit_button, complete_button], [exit_button]],
                font=("Helvetica", 20))


while True:
    event, value = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%d %b, %Y %H:%M:%S"))
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
        try:
            edit_todo = value["todolist"][0]
            new_todo = value["todo"].title() + '\n'
            todolist = functions.get_todolist()
            ind = todolist.index(edit_todo)
            todolist[ind] = new_todo
            functions.write_todolist(todolist)
            window['todolist'].update(values=todolist)
            window["todo"].update(value='')
        except IndexError:
            popup("Please select a todo to edit.", font=("Helvetica", 20))
    elif event == 'todolist':
        window['todo'].update(value=value['todolist'][0])
    elif event == 'Complete':
        try:
            complete_todo = value["todolist"][0]
            todolist = functions.get_todolist()
            todolist.remove(complete_todo)
            functions.write_todolist(todolist)
            window['todolist'].update(values=todolist)
            window["todo"].update(value='')
        except IndexError:
            popup("Please select a todo to complete.", font=("Helvetica", 20))
    elif event == WIN_CLOSED:
        break
    elif event == "Exit":
        break

window.close()
