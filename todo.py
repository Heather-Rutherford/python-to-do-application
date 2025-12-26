# User Interface (UI) and Storage Method

# Build a simple Command Line Interface (CLI) 
# that welcomes users and displays a menu 
# with options to add, view, delete tasks, 
# or quit the application.

# The tasks should be stored in a Python list

#################################
# VERSION 1.0                   #
# Author: Heather Rutherford    #
# Date: January 1, 2026         #
# Class: To-Do Class            #
#################################

class ToDoTask:
    def __init__(self, title, description, start_date, end_date):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
    
    def __str__(self):
        return f"{self.title}: {self.description} (From {self.start_date} to {self.end_date})"

################################
# Global list to store tasks
################################
tasks = []

################################
# User Interface Functions
################################

# Main Menu Display Function
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

# Add Task Function
def add_task():
    try:
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        task = ToDoTask(title, description, start_date, end_date)
        tasks.append(task)
        print(f'Task "{title}" added.')
    except Exception as e:
        print(f"An error occurred while adding a task: {e}")

# View Tasks Function
def view_tasks():
    try:
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
    except  Exception as e:
        print(f"An error occurred while viewing tasks: {e}")
        
# Delete Task Function
def delete_task():
    try:
        view_tasks()
        if tasks:
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f'Task "{removed_task.title}" deleted.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while deleting a task: {e}")
        
################################
# Main Program Loop
################################
def main():
    print("Welcome to the To-Do List Application!")
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '4':
            print("Exiting the application. Goodbye!")
            break
        # Further options will be implemented here


        if choice in ['1', '2', '3']:
            
            if choice == '1':
                add_task()
                input("Press Enter to continue...") # This line pauses the program until the user presses the Enter key
            elif choice == '2':
                view_tasks()
                input("Press Enter to continue...") # This line pauses the program until the user presses the Enter key
            elif choice == '3':
                delete_task()
                input("Press Enter to continue...") # This line pauses the program until the user presses the Enter key
        else:
            print("Invalid choice! Please select a valid option (1-5).")
            
if __name__ == "__main__":
    main()



# def add_task():
#     task = input("Enter a new task: ")
#     tasks.append(task)
#     print(f'Task "{task}" added.')

# def view_tasks():
#     if not tasks:
#         print("No tasks in the list.")
#     else:
#         print("\nYour Tasks:")
#         for idx, task in enumerate(tasks, start=1):
#             print(f"{idx}. {task}")

# def delete_task():
#     view_tasks()
#     if tasks:
#         try:
#             task_num = int(input("Enter the task number to delete: "))
#             if 1 <= task_num <= len(tasks):
#                 removed_task = tasks.pop(task_num - 1)
#                 print(f'Task "{removed_task}" deleted.')
#             else:
#                 print("Invalid task number.")
#         except ValueError:
#             print("Please enter a valid number.")

# while True:
#     display_menu()
#     choice = input("Choose an option (1-4): ")
    
#     if choice == '1':
#         add_task()
#     elif choice == '2':
#         view_tasks()
#     elif choice == '3':
#         delete_task()
#     elif choice == '4':
#         print("Exiting the application. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select a valid option.")
