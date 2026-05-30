from datetime import date

def newtask():
    task = {}
    task['title'] = str(input('Type the task name: '))
    task['description'] = str(input('Describe the task: ')) 
    while True: 
        priority = str(input('Select a task priority (min/mid/high): '))
        if priority not in ('min', 'mid', 'high'):
            print('Error: select one of the specified options.')
        else:
            break
    task['priority'] = priority
    task['date'] = date.today().strftime("%Y-%m-%d")
    return task 

       
def menu():
    print('TASK MANAGER')
    print('1 - Create')
    print('2 - View')
    print('3 - Delete')
    print('4 - Leave')


tasks = []

while True:
    menu()
    choice = int(input('Select an option: '))
    if choice == 1:
        task = newtask()
        tasks.append(task)
        print('Task created sucessfully.')
        print(tasks)
    elif choice == 2:
        if len(tasks) == 0:
            print('You have not created tasks yet.')
        else:
            print(tasks)
    elif choice == 3:
        if len(tasks) == 0:
            print('You have not created tasks yet.')
        else:
            print(tasks)
            select_task = int(input('Type the task number: '))
            tasks.pop(select_task)
    else:
        break


