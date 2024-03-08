
# Task 1: Property Format Checker
def check_format(lines):
    for i, line in enumerate(lines):
        if line.count('=') != 1:
            print(f"Error in line {i+1}: Incorrect format.")

# Task 2: Whitespace Remover
def remove_whitespace(lines):
    return [line.strip().replace(' = ', '=') for line in lines]

# Task 3: Duplicate Property Finder
def find_duplicates(lines):
    properties = [line.split('=')[0] for line in lines]
    seen = set()
    duplicates = set()
    for prop in properties:
        if prop in seen:
            duplicates.add(prop)
        seen.add(prop)
    if duplicates:
        print(f"Duplicate properties found: {duplicates}")

if __name__ == '__main__':
    check_format("test")
    remove_whitespace("test")
    find_duplicates("test")
