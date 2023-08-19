todo_list = []
marked_taskList=[]



def add_task():
    task_description = input("Enter task description: ")
    priority = input("Enter task priority (optional): ")
    due_date = input("Enter task due date (optional, format: YYYY-MM-DD): ")
    task = {
        'description': task_description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    todo_list.append(task)
    print("Task added successfully")



def complete_task():
    task_number=int(input("Enter task number to be marked: "))
    if task_number > 0 and task_number<=len(todo_list):
        taskdict=todo_list[task_number-1]
        if taskdict['completed']==True:
            print("Task is already marked")
        else:
            marked_taskList.append( taskdict)
            taskdict['completed']=True
            print("Task marked as completed")
    else:
        print("Invalid task Number")
    while True:
        c_tasks = input("Do you want to see the completed marked tasks? Write Yes/No: ")
        if c_tasks == "Yes":
            for x in marked_taskList:
             print(x)
            break  
        elif c_tasks == "No":
            break 
        else:
            print("Invalid input. Please enter Yes or No.")


def view_todo_list():
    if len(todo_list) == 0:
        print("No tasks found. Task list is empty.")
        return
    def sort_key(task):
        if task['priority'] is not None and task['due_date'] is not None:
            return task['priority'], task['due_date']
        elif task['priority'] is not None:
            return task['priority'], '0-0-0'  
        elif task['due_date'] is not None:
            return 'aaa', task['due_date']  
        else:
            return 'ZZZ', '9999-12-31'
    sorted_list = sorted(todo_list, key=sort_key)
    for i, task in enumerate(sorted_list, start=1):
        completed_status = 'X' if task['completed'] else ' '
        description = task['description']
        priority = task['priority'] if task['priority'] else 'No Priority'
        due_date = task['due_date'] if task['due_date'] else 'No Due Date'
        print(f"{i}. [{completed_status}] {description} (Priority: {priority}, Due Date: {due_date})")
    print("End of to-do list")




def remove_task():
    if len(todo_list) == 0:
        print("No tasks to remove")
        return
    task_number = int(input("Enter task number to remove: "))
    if task_number > 0 and task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Removed task: {removed_task['description']}")
    else:
        print("Invalid task number")



def saveTask():
    if len(todo_list) == 0:
        print("No tasks found. Task list is empty.")
        return
    file_path = input("Enter file path to save tasks: ")
    with open(file_path, 'w') as file:
        for task in todo_list:
            file.write(f"{task['description']},{task['priority']},{task['due_date']},{task['completed']}\n")
    print("Tasks saved to file")


def Tasks_from_file():
    file_name = input("Enter file name to load tasks from: ")

    try:
        with open(file_name, 'r') as file:
            first_line = file.readline()
            if not first_line:
                print("The file is empty. No tasks to load.")
                return

            for line in file:
                task_data = line.strip().split(',')
                task = {
                    'description': task_data[0],
                    'priority': task_data[1],
                    'due_date': task_data[2],
                    'completed': task_data[3] == 'True'
                }
                todo_list.append(task)

        print("Tasks loaded from file")
        while True:
            loaded_tasks = input("Do you want to see the Loaded tasks? Write Yes/No: ")
            if loaded_tasks == "Yes":
                view_todo_list()
                break  
            elif loaded_tasks == "No":
                break 
            else:
                print("Invalid input. Please enter Yes or No.")
    except FileNotFoundError:
        print("File not found.")



def add_priority():
    task_number = int(input("Enter task number to add priority: "))
    if task_number > 0 and task_number <= len(todo_list):
        priority = input("Enter priority for the task: ")
        task = todo_list[task_number - 1]
        task['priority'] = priority
        print("Priority added to the task")
    else:
        print("Invalid task number")



def add_due_date():
    task_number = int(input("Enter task number to add due date: "))
    if task_number > 0 and task_number <= len(todo_list):
        due_date = input("Enter due date for the task (format: YYYY-MM-DD): ")
        task = todo_list[task_number - 1]
        task['due_date'] = due_date
        print("Due date added to the task")
    else:
        print("Invalid task number")



while True:
    print("To-Do List Manager")
    print("-----------------")
    print("1. Add a task\n2. Complete a task\n3. View to-do list sorted by Priority")
    print("4. Remove a task\n5. Save the task list to file\n6. Load tasks from file")
    print("7. Add priority to task\n8. Add due date to task\n9. Exit")

    user_input = input("Enter your choice (1-9): ")

    if user_input == '1':
        add_task()
    elif user_input == '2':
        complete_task()
    elif user_input == '3':
        view_todo_list()
    elif user_input == '4':
        remove_task()
    elif user_input=='5':
        saveTask()
    elif user_input=='6':
        Tasks_from_file()
    elif user_input== '7':
        add_priority()
    elif user_input== '8':
        add_due_date()
    elif user_input== '9':
        break
    else:
        print("Invalid input. Try Again")    


