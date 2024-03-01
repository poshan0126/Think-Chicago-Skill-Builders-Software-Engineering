try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ZeroDivisionError:
    pass
except ValueError:
    pass

filename = input("Enter a filename to read: ")
try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    pass