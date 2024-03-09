
# The Calculator App

# Task 1: Arithmetic Operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Task 2 & 3: User Input and Error Handling
def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")
        if operation == '+':
            print("Result:", add(num1, num2))
        elif operation == '-':
            print("Result:", subtract(num1, num2))
        elif operation == '*':
            print("Result:", multiply(num1, num2))
        elif operation == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operation.")
    except ValueError:
        print("Error: Please enter a valid number.")

calculator()
