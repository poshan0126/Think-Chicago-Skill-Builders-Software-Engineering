number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Identify the Greatest
max_number = max(number1, number2, number3)
# Identify the Smallest
min_number = min(number1, number2, number3)

print("The largest number is", max_number)
print("The smallest number is", min_number)

# Equality Check
if number1 == number2 == number3:
    print("All numbers are equal.")
elif number1 == number2 or number1 == number3 or number2 == number3:
    print("Two numbers are equal and the largest" if max_number in [number1, number2] else "Two numbers are equal.")