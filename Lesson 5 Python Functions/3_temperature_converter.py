
# The Temperature Converter

# Task 1: Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Task 2: Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Task 3: User Interface
def temperature_converter():
    choice = input("Convert to (C)elsius or (F)ahrenheit? Enter C or F: ")
    if choice.lower() == 'c':
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"{temp}F is {fahrenheit_to_celsius(temp):.2f}C")
    elif choice.lower() == 'f':
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp}C is {celsius_to_fahrenheit(temp):.2f}F")
    else:
        print("Invalid choice.")

temperature_converter()
