
# The Shopping List Maker

shopping_list = []

# Task 1: Add Items
def add_item(item):
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

# Task 2: Remove Items
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

# Task 3: Print List
def print_list():
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")

# Sample Function Calls
add_item("Milk")
add_item("Eggs")
remove_item("Milk")
print_list()
