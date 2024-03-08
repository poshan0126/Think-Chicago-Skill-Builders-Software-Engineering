
# Task 1: Input Length Validator
def validate_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        return False
    return True

# Task 2: Password Complexity Checker
def check_password_complexity(password):
    import re
    if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}', password):
        return True
    return False

# Task 3: Email Formatter
def format_email(email):
    return email.lower().replace(' ', '.')

if __name__ == '__main__':
    format_email('xyz@gmail.com')
    check_password_complexity('xyz@gmail.com')
    validate_name_length('xyz@gmail.com')
