# a command-line calculator supporting basic operations.

# Functions for basic operations
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Main Program
while True:
    print("\n=== Simple CLI Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3.Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5) : ")

    if choice == '5':
        print("Exiting Calculator. Goodbye!")
        break
    
    if choice in ['1','2','3','4']:
        try:
            # Get numbers from user
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
        except ValueError:
            print("Invalid Input. Please enter numbers only.")
            continue

        # Perform The choosen operation
        if choice == '1':
            print(f"Result : ", add(num1, num2))
        elif choice == '2':
            print(f"Result : ", subtract(num1, num2))
        elif choice == '3':
            print(f"Result : ", multiply(num1, num2))
        elif choice == '4':
            print(f"Result : ", divide(num1, num2))
    else:
        print("Invalid choice. Please select a valid valid option.")