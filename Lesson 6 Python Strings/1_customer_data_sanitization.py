
# Customer Data Sanitization

# Task 1: Code Correction
def format_customer_name(name):
    return name.capitalize()

# Task 2: Email Validation
def validate_emails(email_list):
    for email in email_list:
        if "@" not in email or "." not in email.split("@")[1]:
            print(f"Invalid email format: {email}")

# Task 3: Username Generation
def generate_username(first_name, last_name):
    return (first_name[:3] + last_name[:3]).lower()

# Calls with dummy values
name_formatted = format_customer_name("jOhN dOe")
print(name_formatted)

emails_to_validate = ["validemail@example.com", "noatsymbol", "nodotcom@"]
validate_emails(emails_to_validate)

username = generate_username("John", "Doe")
print(username)
