
# User Input Data Processor

# Task 1: Input Length Validator
def validate_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("First and last names must be at least 2 characters long.")

# Task 2: Password Complexity Checker
def check_password_complexity(password):
    if len(password) < 8 or not any(char.isupper() for char in password) or        not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        print("Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, and a number.")

# Task 3: Email Formatter
def format_email(email):
    return email.lower().replace(" ", ".")

# Calls with dummy values
validate_name_length("Jo", "D")
check_password_complexity("Passw1")
formatted_email = format_email("John DOE @Example.com ")
print(formatted_email)
