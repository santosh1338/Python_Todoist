

def show(todolist):
    if len(todolist) == 0:
        print("You don't have any Todo.")
    else:
        for i, it in enumerate(todolist):
            nit = it.strip('\n')
            print(f"{i+1}- {nit}")


def get_todolist(path='Todos.txt'):
    with open(path, 'r') as file:
        todolist = file.readlines()
    return todolist


def write_todolist(arg, path='Todos.txt'):
    with open(path, 'w') as file:
        file.writelines(arg)
