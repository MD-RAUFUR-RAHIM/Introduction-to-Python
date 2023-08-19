print("To-Do List Manager")
print("-----------------")
print("1. Add a task\n2. Complete a task\n3. View to-do list sorted by due date\n4. Remove a task")
print("5. Save the task list to file\n6. Add priority to task\n7. Add due date to task\n8. Exit")
userinput = int(input("Enter your choice (1-8): "))
TaskList=[]
def add_task():
    description=input("Enter Description: ")
    priority=input("Enter Task priority (Not Mandatory): ")
    dueDate=input("Due Date (dd/mm/year): ")
    taskdict={
        'description': description,
        'priority' : priority,
        'dueDate': dueDate,
        'completed': False
    }
    TaskList.append(taskdict)
    print("Task Added Successfully! :) ")

def complete_task():
    task_number = int(input("Enter task number to be marked: "))
    if task_number > 0 and task_number <= len(TaskList):
        task_dict = TaskList[task_number - 1]
        if task_dict['completed']:
            print("Task is already marked as completed.")
        else:
            marked_taskList = []
            marked_taskList.append(task_dict)
            task_dict['completed'] = True
            print("Task marked as completed")
    else:
        print("Invalid task number")

    while True:
        c_tasks = input("Do you want to see the completed marked tasks? Write Yes/No: ")
        if c_tasks == "Yes":
            print(marked_taskList)
            break
        elif c_tasks == "No":
            break
        else:
            print("Invalid input. Please enter Yes or No.")


def view_todo_list():
    print("This is to view the to-do list sorted by due date")

def remove_task():
    print("This is to remove a task")

def save_tasks_to_file():
    print("This is to save the task list to a file")

def add_priority():
    print("This is to add priority to a task")

def add_due_date():
    print("This is to add a due date to a task")

while True:
    print("To-Do List Manager")
    print("-----------------")
    print("1. Add a task\n2. Complete a task\n3. View to-do list sorted by due date\n4. Remove a task")
    print("5. Save the task list to file\n6. Add priority to task\n7. Add due date to task\n8. Exit")
    userinput = int(input("Enter your choice (1-8): "))
    if userinput == 1:
        add_task()
    elif userinput == 2:
      complete_task()
    elif userinput == 3:
      view_todo_list()
    elif userinput == 4:
      remove_task()
    elif userinput == 5:
      save_tasks_to_file()
    elif userinput == 6:
      add_priority()
    elif userinput == 7:
     add_due_date()
    elif userinput == 8:
     exit_program()
    else:
     print("Invalid Input")