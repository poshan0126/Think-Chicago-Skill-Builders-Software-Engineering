
# Task 1: Command Parser
def parse_command(user_input):
    commands = ["help", "issue", "contact support"]
    for command in commands:
        if command in user_input.lower():
            return command
    return "Unknown command"

# Task 2: Issue Categorizer
def categorize_issue(issue):
    categories = {
        "login": "Login Issue",
        "performance": "Performance Issue",
        "error": "System Error"
    }
    for keyword, category in categories.items():
        if keyword in issue.lower():
            return category
    return "General Issue"

# Task 3: Auto-Response Generator
def generate_auto_response(command):
    if command == "help":
        return "Please visit our FAQ section."
    elif command == "issue":
        return "Please describe your issue in more detail."
    elif command == "contact support":
        return "Contacting support, please wait..."
    else:
        return "How can I assist you?"
if __name__ == '__main__':
    parse_command("test")
    categorize_issue("test@test.com")
    generate_auto_response("test")