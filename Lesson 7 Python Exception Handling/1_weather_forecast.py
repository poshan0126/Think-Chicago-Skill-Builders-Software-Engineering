
# Exceptional Weather Forecast

# Task 1: User Input Loop
while True:
    user_input = input("Enter the temperature in Fahrenheit, or 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break

    # Task 2: Temperature Conversion
    try:
        temperature = float(user_input)
    except ValueError:
        print("Please enter a valid numerical temperature.")
    else:
        def fahrenheit_to_celsius(fahrenheit):
            return (fahrenheit - 32) * 5/9
        print(f"The temperature in Celsius is {fahrenheit_to_celsius(temperature):.2f} degrees.")

    # Task 3: User Experience
    finally:
        print("Thank you for using the weather forecast application.")
