## SE Foundations Module Project: To Do Application

## Overview

In this project, you will build a functional To-Do List Application using Python from scratch. This assignment will help you strengthen your understanding of Python concepts such as syntax, data types, control structures, functions, and error handling, all while creating a practical, interactive command-line application.

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Heather-Rutherford/python-to-do-application.git
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-app
   ```

## Running the Application

Run the application using Python:

```bash
python todo.py
```

## How to use the file

After running the file, a menu will display as shown below:

To-Do List Application

1. Add Task
2. View Tasks
3. Delete Task
4. Quit

Choose an option (1-4):

Option 1 - Add Task will allow you to add the title and description of a task. You will be prompted as to whether you want to add another task. Add another task if you desire. Otherwise, pressing 'n' will exit the 'Add Task' option and return to the main menu.

Option 2 - View Tasks will allow you to view the tasks that you have entered via Option 1 minus any tasks you may have deleted via Option 3. You will be asked to press any key to return to the main menu.

Option 3 - Delete Task will display your list of tasks and a prompt for the task number you want to delete. If you mistakenly entered Option 3, you can cancel the option by pressing the 'Enter' key to return to the menu.

If you do intend to delete a task, type the number and press 'Enter'. You will be prompted as to whether you want to delete another task. If you press 'n', Option 3 will be cancelled and you will be returned to the menu. Otherwise, press 'y' and your task list will be displayed again and you will be prompted to type the task number to delete.

Option 4 will exit the program.
