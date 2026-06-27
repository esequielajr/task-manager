import utils
from datetime import date
from time import sleep

      
def main_menu():
    
    utils.title('TASK MANAGER')
    
    print('1 - Create')
    print('2 - View')
    print('3 - Update')
    print('4 - Delete')
    print('5 - Leave\n')


def update_menu():
    
    utils.title('UPDATE', size=5)
    
    print('1 - Title')
    print('2 - Description')
    print('3 - Priority')
    print('4 - Mark as Finished')
    print('5 - Return\n')
 
    
def newtask():
    
    task = {}
    
    while True:
        try:
            task['title'] = str(input('\nType the task title: '))
            break
        except:
            print('Error, invalid entry, try again.')
            sleep(1)
    
    while True:
        try: 
            task['description'] = str(input('\nDescribe the task: '))
            break
        except:
            print('Error, invalid entry, try again.')
            sleep(1)
        
    while True:
        try:
            priority = str(input('\nSelect a task priority (min/mid/high): '))
            if priority not in ('min', 'mid', 'high'):
                print('\nError: select one of the specified options. ')
                sleep(1)
                continue
            else:
                task['priority'] = priority
                break
        except:
            print('Error: invalid option, try again.')
            sleep(1)
             
    task['state'] = 'pending'
    task['date'] = date.today().strftime("%Y-%m-%d")
    return task     
 
           
def read_tasks():
    for task in tasks:
        yield task 

          
def list_tasks(tasks):
    
    utils.title('TASK LIST', size=12)
    
    for k, task in enumerate(read_tasks()):
        print(f'\nID: {k+1}', end=' | ')  
        print(f'TITLE: {task["title"]}', end=' | ')  
        print(f'DESCRIPTION: {task["description"]}', end=' | ')
        print(f'PRIORITY: {task["priority"]}', end=' | ')
        print(f'STATE: {task["state"]}', end=' | ')
        print(f'DATE: {task["date"]}')
     
    if len(tasks) <= 10:
        sleep(len(tasks))
    else:
        sleep(10)
        
       
def update_task():
    
    list_tasks(tasks)
    
    while True:
        try:
            select_task = int(input('\nSelect a task ID to update: '))
            
            if select_task == 0 or not tasks[select_task-1]:
                print('\nError: invalid option, try again.')
                sleep(1)
                continue
            else:
                select_task -= 1
                break
            
        except:
            print('\nError: invalid option, try again.')
            sleep(1)
            
    while True:
        try:
            update_menu()
            while True:
                try:
                    choice = int(input('Select an option: '))
                    if choice not in (1,2,3,4,5):
                        print('\nError: invalid option, try again.')
                        sleep(1)
                    else:
                        break
                except:
                    print('\nError: invalid option, try again.')
                    sleep(1)
                    
            if choice == 1:
                while True:
                    try:
                        title = str(input('\nType the new title: '))
                        tasks[select_task]['title'] = title
                        print('\nTitle updated sucessfully.')
                        sleep(1)
                        break
                    except:
                        print('\nError: invalid entry, try again.')
                        sleep(1)
            elif choice == 2:
                while True:
                    try:
                        description = str(input('\nType the new description: '))
                        tasks[select_task]['description'] = description
                        print('\nDescription updated sucessfully.')
                        sleep(1)
                        break
                    except:
                        print('\nError: invalid entry, try again.')
                        sleep(1)            
            elif choice == 3:
                while True:
                    try:
                        priority = str(input('\nSelect a task priority (min/mid/high): '))
                        if priority not in ('min', 'mid', 'high'):
                            print('\nError: select one of the specified options.')
                            sleep(1)
                        else:
                            tasks[select_task]['priority'] = priority
                            print('\nPriority updated sucessfully.')
                            sleep(1)
                            break
                    except:
                        print('\nError: invalid option, try again.')
                        sleep(1)
            elif choice == 4:
                tasks[select_task]['state'] = 'done'
                print('\nTask marked as Finished.')
                sleep(1)
            elif choice == 5:
                break
        except:
            print('\nError: invalid option, try again.')
            sleep(1)
            
        break
          
          
tasks = []


while True:
    
    while True:
        try:
            main_menu()
            choice = int(input('Select an option: '))
            if choice not in (1,2,3,4,5):
                print('\nError: invalid option, try again.')
                sleep(1)
            else:
                break
        except:
            print('\nError: invalid option, try again.')
            sleep(1)
            
    if choice == 1:
        task = newtask()
        tasks.append(task)
        print('\nTask created sucessfully.')
        sleep(1)
    elif choice == 2:
        if len(tasks) == 0:
            print('\nYou have not created tasks yet.')
            sleep(1)
        else:
            list_tasks(tasks)
    elif choice == 3:
        if len(tasks) == 0:
            print('\nYou have not created tasks yet.')
            sleep(1)
        else:
            update_task()
    elif choice == 4:
        if len(tasks) == 0:
            print('\nYou have not created tasks yet.')
            sleep(1)
        else:
            list_tasks(tasks)
            while True:
                try:
                    choice = int(input('\nSelect a task ID to delete: '))
                    if choice == 0 or not tasks[choice-1]:
                        print('\nError: invalid option, try again.')
                        sleep(1)
                    else:
                        tasks.pop(choice-1)
                        print('\nTask deleted sucessfully.')
                        sleep(1)
                        break
                except:
                    print('\nError: invalid option, try again.')
                    sleep(1)
    elif choice == 5:
        break


