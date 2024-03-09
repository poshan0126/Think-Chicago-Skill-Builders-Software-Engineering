
# Interactive Help Desk Bot

# Task 1: Command Parser
def parse_command(user_input):
    commands = {"help": "How can I assist you?", "issue": "Please describe your issue.", "contact support": "You can reach support at support@example.com."}
    for command, response in commands.items():
        if command in user_input.lower():
            return response
    return "Command not recognized."

# Task 2: Issue Categorizer
def categorize_issue(issue_description):
    categories = {"login": "Login Issue", "performance": "Performance Issue", "error": "Error Issue"}
    for keyword, category in categories.items():
        if keyword in issue_description.lower():
            return category
    return "General Issue"

# Task 3: Auto-Response Generator
def generate_auto_response():
    return "For FAQs, please visit our FAQ section. For more help, contact support@example.com or submit a ticket through our ticket submission page."

# Calls with dummy values
command_response = parse_command("I need help with my account")
print(command_response)
issue_category = categorize_issue("I am experiencing performance issues")
print(issue_category)
auto_response = generate_auto_response()
print(auto_response)
