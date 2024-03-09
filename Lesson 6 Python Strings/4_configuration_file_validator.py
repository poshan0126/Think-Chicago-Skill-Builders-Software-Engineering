
# Configuration File Validator

# Task 1: Property Format Checker
def check_format(config_lines):
    for i, line in enumerate(config_lines):
        if "=" not in line or line.count("=") != 1:
            print(f"Error on line {i+1}: Incorrect format")

# Task 2: Whitespace Remover
def remove_whitespace(config_lines):
    return [line.strip().replace(" = ", "=") for line in config_lines]

# Task 3: Duplicate Property Finder
def find_duplicates(config_lines):
    properties = {}
    for i, line in enumerate(config_lines):
        property_name = line.split("=")[0].strip()
        if property_name in properties:
            properties[property_name].append(i+1)
        else:
            properties[property_name] = [i+1]
    for property_name, lines in properties.items():
        if len(lines) > 1:
            print(f"Duplicate property '{property_name}' found on lines {', '.join(map(str, lines))}")

# Calls with dummy values
config_lines = [
    "name = John Doe",
    "email= john.doe@example.com",
    " email =jane.doe@example.com",
    "name=Johnathan Doe"
]
check_format(config_lines)
cleaned_lines = remove_whitespace(config_lines)
print(cleaned_lines)
find_duplicates(cleaned_lines)
