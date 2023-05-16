from functions import show, get_todolist, write_todolist
from time import strftime

dt = strftime("%d %b, %Y %H:%M:%S")
print(f"It is {dt}")

while True:

    todo = input("Type add, show, edit, complete or exit: ")
    if todo.startswith('add '):
        todo = todo.removeprefix("add ")
        print(todo.title(), "has been added to your list of Todos.")
        todolist = get_todolist()
        todolist.append(todo.title() + '\n')
        write_todolist(todolist)
    elif todo == "show":
        show(todolist)
    elif todo.startswith('edit '):
        todo = todo.removeprefix('edit ')
        todo = todo.title() + '\n'
        num = todolist.index(todo)

        todolist = get_todolist()

        new = input("Enter new todo: ")
        new = new.title() + '\n'

        todolist[num] = new

        write_todolist(todolist)
        print('Your list has successefully been edited.')
    elif todo.startswith('complete '):

        todolist = get_todolist()

        todo = todo.removeprefix('complete ')

        todo = todo.title() + '\n'
        todolist.remove(todo)
        print('Good job!!')

        write_todolist(todolist)

    elif todo == "exit":
        break
    else:
        print("Command unknown")

print('Bye!!')
