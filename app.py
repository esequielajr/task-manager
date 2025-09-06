
def newtask():
    task = {}
    title = str(input('Digite o nome da tarefa: '))
    task['title'] = title
    description = str(input('Digite a descrição da tarefa: '))
    task['description'] = description
    status = str(input('Digite o status da tarefa'))
    task['status'] = status
    return task 
       
def menu():
    print('TASK MANAGER')
    print('1 - Create a Task')
    print('2 - Search a Task')
    print('3 - Delete a Task')
    print('4 - Leave')

def start():
    tasks = []
    while True:
        menu()
        user_choose = int(input('Select an option: '))
        if user_choose == 1:
            task = newtask()
            tasks.append(task)
            print('The task was created sucessfully.')
            print(tasks)
        elif user_choose == 2:
            if len(tasks) == 0:
                print('You do not have created tasks yet.')
            else:
                print(tasks)
                select_task = int(input('Type the task number: '))
                print(tasks[select_task])
        elif user_choose == 3:
            if len(tasks) == 0:
                print('You do not have created tasks yet.')
            else:
                print(tasks)
                select_task = int(input('Type the task number: '))
                tasks.pop(select_task)
        else:
            break

start()



