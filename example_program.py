# 2. Global variable
# Using a global tasks list isn't ideal. Should be passed as parameter or encapsulated in a class.

# 3. Empty custom exceptions section
# The placeholder comment exists but no exception is defined.

# 4. Missing docstrings
# Functions lack documentation explaining parameters and return values.

# 5. Mixed concerns
# Functions handle both business logic AND user interaction (the "do you want to continue" loops shouldn't be inside each function).

# 6. Commented-out code (lines 143-182)
# Should be removed - that's what version control is for.

# 7. Date inconsistency
# Header says "January 1, 2026" but today is December 27, 2025.

# 8. view_tasks() asking to "view again"
# This is unusual - viewing tasks shouldn't loop asking if you want to view again.

# 9. Overly broad exception handling
# except Exception as e catches too much. Should catch specific exceptions.

# 10. delete_task() calls view_tasks()
# Creates tight coupling between functions. Better to return data and let caller decide what to display.

# 11. No type hints
# Modern Python recommends type annotations for better code clarity.
# # 
# Would you like me to refactor the file to follow best practices?

# Claude Sonnet 4.5 • 1x
# # """
# # Simple Calculator - Command Line Program Example
# # This program demonstrates a basic CLI interface with menu options.
# # """

# # def display_menu():
# #     """Display the calculator menu options."""
# #     print("\n=== Simple Calculator ===")
# #     print("1. Add")
# #     print("2. Subtract")
# #     print("3. Multiply")
# #     print("4. Divide")
# #     print("5. Exit")
# #     print("=" * 25)

# # def add(a, b):
# #     """Add two numbers."""
# #     return a + b

# # def subtract(a, b):
# #     """Subtract b from a."""
# #     return a - b

# # def multiply(a, b):
# #     """Multiply two numbers."""
# #     return a * b

# # def divide(a, b):
# #     """Divide a by b."""
# #     if b == 0:
# #         return "Error: Cannot divide by zero"
# #     return a / b

# # def get_numbers():
# #     """Get two numbers from the user."""
# #     try:
# #         num1 = float(input("Enter first number: "))
# #         num2 = float(input("Enter second number: "))
# #         return num1, num2
# #     except ValueError:
# #         print("Invalid input! Please enter valid numbers.")
# #         return None, None

# # def main():
# #     """Main program loop."""
# #     print("Welcome to the Calculator!")
    
# #     while True:
# #         display_menu()
# #         choice = input("\nChoose an operation (1-5): ")
        
# #         if choice == '5':
# #             print("Thank you for using the calculator. Goodbye!")
# #             break
        
# #         if choice in ['1', '2', '3', '4']:
# #             num1, num2 = get_numbers()
            
# #             if num1 is not None and num2 is not None:
# #                 if choice == '1':
# #                     result = add(num1, num2)
# #                     print(f"Result: {num1} + {num2} = {result}")
# #                 elif choice == '2':
# #                     result = subtract(num1, num2)
# #                     print(f"Result: {num1} - {num2} = {result}")
# #                 elif choice == '3':
# #                     result = multiply(num1, num2)
# #                     print(f"Result: {num1} × {num2} = {result}")
# #                 elif choice == '4':
# #                     result = divide(num1, num2)
# #                     print(f"Result: {num1} ÷ {num2} = {result}")
# #         else:
# #             print("Invalid choice! Please select a valid option (1-5).")

# # if __name__ == "__main__":
# #     main()
