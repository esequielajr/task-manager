import utils
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
	
    utils.title('TASK MANAGER')
    
    print('1 - Create')
    print('2 - View')
    print('3 - Delete')
    print('4 - Leave\n')

    
def read_tasks():
    for task in tasks:
        yield task 

          
def list_tasks(tasks):
    
    print('\nTASKS LIST')
    
    for k, task in enumerate(read_tasks()):
        print(f'\nID: {k+1}', end=' | ')  
        print(f'TITLE: {task["title"]}', end=' | ')  
        print(f'DESCRIPTION: {task["description"]}', end=' | ')
        print(f'PRIORITY: {task["priority"]}')


tasks = []


while True:
    menu()
    choice = int(input('Select an option: '))
    if choice == 1:
        task = newtask()
        tasks.append(task)
        print('\nTask created sucessfully.')
    elif choice == 2:
        if len(tasks) == 0:
            print('\nYou have not created tasks yet.')
        else:
            list_tasks(tasks)
    elif choice == 3:
        if len(tasks) == 0:
            print('\nYou have not created tasks yet.')
        else:
            list_tasks(tasks)
            select_task = int(input('\nType the task ID: '))
            tasks.pop(select_task-1)
            print('\nTask deleted sucessfully.')
    else:
        break


