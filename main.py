from datetime import date

def newtask():
    task = {}
    task['title'] = str(input('\nType the task name: '))
    task['description'] = str(input('\nDescribe the task: ')) 
    while True: 
        priority = str(input('\nSelect a task priority (min/mid/high): '))
        if priority not in ('min', 'mid', 'high'):
            print('\nError: select one of the specified options.')
        else:
            break
    task['priority'] = priority
    task['date'] = date.today().strftime("%Y-%m-%d")
    return task 

       
def menu(): 
    print('\nTASK MANAGER\n')
    print('1 - Create')
    print('2 - View')
    print('3 - Delete')
    print('4 - Leave\n')


tasks = []

while True:
    menu()
    choice = int(input('Select an option: '))
    if choice == 1:
        task = newtask()
        tasks.append(task)
        print('\nTask created sucessfully.')
        print('\n', tasks)
    elif choice == 2:
        if len(tasks) == 0:
            print('\nYou have not created tasks yet.')
        else:
            print('\n', tasks)
    elif choice == 3:
        if len(tasks) == 0:
            print('\nYou have not created tasks yet.')
        else:
            print('\n', tasks)
            select_task = int(input('\nType the task number: '))
            tasks.pop(select_task)
    else:
        break


