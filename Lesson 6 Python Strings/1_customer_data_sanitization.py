
# Task 1: Code Correction
def format_name(name):
    """Formats the customer's name to have the first letter uppercase and the rest lowercase."""
    return name.capitalize()

# Task 2: Email Validation
def validate_emails(email_list):
    """Checks if email addresses are valid."""
    for email in email_list:
        if "@" in email and "." in email.split("@")[1]:
            continue
        print(f"Invalid email: {email}")

# Task 3: Username Generation
def generate_username(first_name, last_name):
    """Generates a username from the first three letters of the first and last name."""
    username = (first_name[:3] + last_name[:3]).lower()
    if len(first_name) < 3 or len(last_name) < 3:
        username = (first_name + last_name).lower()
    return username
if __name__ == '__main__':
    format_name("test")
    validate_emails("test@test.com")
    generate_username("test","test")
