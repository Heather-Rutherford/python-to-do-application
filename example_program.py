"""
Simple Calculator - Command Line Program Example
This program demonstrates a basic CLI interface with menu options.
"""

def display_menu():
    """Display the calculator menu options."""
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 25)

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def get_numbers():
    """Get two numbers from the user."""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return None, None

def main():
    """Main program loop."""
    print("Welcome to the Calculator!")
    
    while True:
        display_menu()
        choice = input("\nChoose an operation (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is not None and num2 is not None:
                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} × {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} ÷ {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
