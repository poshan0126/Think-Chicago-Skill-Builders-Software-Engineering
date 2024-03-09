
# Calculator Concierge

# Task 1: Calculator Setup
print("Operations: add, subtract, multiply, divide")
operation = input("Choose an operation: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Task 2: Operation Execution
def calculate(operation, num1, num2):
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result is {result}")

# Task 3: Polite Error Handling
    finally:
        print("Thank you for using Calculator Concierge.")

calculate(operation, num1, num2)
