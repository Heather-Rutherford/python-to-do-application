# User Interface (UI) and Storage Method

# Build a simple Command Line Interface (CLI) 
# that welcomes users and displays a menu 
# with options to add, view, delete tasks, 
# or quit the application.

# The tasks should be stored in a Python list

#################################
# VERSION 1.0                   #
# Author: Heather Rutherford    #
# Date: December 27, 2025       #
# Class: To-Do Class            #
#################################

################################
# Custom Exceptions
################################

class NoTasksToDeleteError(Exception):
    """Raised when attempting to delete from an empty task list"""
    def __init__(self, message="No tasks exist to delete"):
        self.message = message
        super().__init__(self.message)
    
#################################
# Classes                       #
#################################

class ToDoTask:
    """Class representing a single To-Do task."""
    
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        
    def __str__(self) -> str:
        return f'Title: {self.title}\n Description: {self.description}\n'

class ToDoTaskManager:
    """Class to manage To-Do tasks."""
    
    def __init__(self) -> None:
        self.tasks = []
        
    def add_task(self, title: str, description: str) -> ToDoTask:
        """Add a new task."""
        task = ToDoTask(title, description)
        self.tasks.append(task)
        return task
    
    def get_all_tasks(self) -> list:
        """Return all tasks."""
        return self.tasks.copy()
    
    def delete_task(self, index: int) -> ToDoTask:
        """Delete a task at a given index."""
        if not self.tasks:
            raise NoTasksToDeleteError()
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        else:
            raise ValueError("Invalid task number.")
        
    def is_empty(self) -> bool:
        """Check if the task list is empty."""
        return len(self.tasks) == 0

################################
# User Interface Functions
################################

# Main Menu Display Function
def display_menu():
    print("\nTo-Do List Application\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

# Add Task Function
def add_task(manager):
    while True:
        try:
            title = input("\nEnter task title or press Enter to cancel: ")
            if title.strip() == '':
                break
            description = input("Enter task description: ")
            task = manager.add_task(title, description)
            print(f'Task "{title}" added.')
        except Exception as e:
            print(f"\nAn error occurred while adding a task: {e}")
            
        more = input("\nDo you want to add another task? (y/n): ").strip().lower()
        while more not in ['y', 'n']:
            more = input("\nInvalid answer. Please enter 'y' or 'n': ").strip().lower()
        if more != 'y':
            break
 
# View Tasks Function
def view_tasks(action, manager):
    try:
        tasks = manager.get_all_tasks()
        if not tasks:
            print("\nNo tasks in the list.")
        else:
            print("\nYour Tasks:\n")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
    except Exception as e:
        print(f"\nAn error occurred while viewing tasks: {e}")
    
    if action == 'view':
        input("\nPress any key to return to the main menu...")
        
# Delete Task Function
def delete_task(manager):
    while True:
        try:
           tasks = manager.get_all_tasks()
           if not tasks:
                raise NoTasksToDeleteError()
           
           view_tasks('delete', manager)
           task_num_input = input("\nEnter the task number to delete or press Enter to cancel: ")
           if task_num_input.strip() == '':
               break
           task_num = int(task_num_input)
           manager.delete_task(task_num - 1)
           print(f'\nTask number {task_num} deleted.')
            
        except NoTasksToDeleteError as e:
            print(e.message)
            input("\nPress any key to return to the main menu...")
            break
        except ValueError:
            print("\nPlease enter a valid number.")
        except Exception as e:
            print(f"\nAn error occurred while deleting a task: {e}")

        more = input("\nDo you want to delete another task? (y/n): ").strip().lower()
        while more not in ['y', 'n']:
            more = input("\nInvalid answer. Please enter 'y' or 'n': ").strip().lower()
        if more != 'y':
            break
                
################################
# Main Program Loop
################################
def main():
    manager = ToDoTaskManager()
    print("\nWelcome to the To-Do List Application!")
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '4':
            print("\nExiting the application. Goodbye!\n1")
            break

        if choice in ['1', '2', '3']:
            
            if choice == '1':
                add_task(manager)
            elif choice == '2':
                view_tasks('view', manager)
            elif choice == '3':
                delete_task(manager)
        else:
            print("Invalid choice! Please select a valid option (1-4).")
            
if __name__ == "__main__":
    main()
