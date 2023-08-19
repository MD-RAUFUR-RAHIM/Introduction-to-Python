print("To-Do List Manager")
print("-----------------")
print("1. Add a task\n2. Complete a task\n3. View to-do list sorted by due date\n4. Remove a task")
print("5. Save the task list to file\n6. Add priority to task\n7. Add due date to task\n8. Exit")
userinput = input("Enter your choice (1-8): ")

def add_task():
    print("This is to add a task")

def complete_task():
    print("This is to complete a task")
if userinput == 1:
    add_task()
elif userinput == 2:
    complete_task()

else:
    print("Invalid Input")
