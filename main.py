def newtask():
    task = {}
    title = str(input('Type the task name: '))
    task['title'] = title
    description = str(input('Describe the task: '))
    task['description'] = description
    status = str(input('Type the task status: '))
    task['status'] = status
    return task 

       
def menu():
    print('TASK MANAGER')
    print('1 - Create a Task')
    print('2 - View Tasks')
    print('3 - Delete a Task')
    print('4 - Leave')


tasks = []

while True:
    menu()
    user_choice = int(input('Select an option: '))
    if user_choice == 1:
        task = newtask()
        tasks.append(task)
        print('The task was created sucessfully.')
        print(tasks)
    elif user_choice == 2:
        if len(tasks) == 0:
            print('You do not have created tasks yet.')
        else:
            print(tasks)
            select_task = int(input('Type the task number: '))
            print(tasks[select_task])
    elif user_choice == 3:
        if len(tasks) == 0:
            print('You do not have created tasks yet.')
        else:
            print(tasks)
            select_task = int(input('Type the task number: '))
            tasks.pop(select_task)
    else:
        break


