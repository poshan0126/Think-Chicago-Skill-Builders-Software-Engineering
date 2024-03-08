shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"Added {item} to the list.")

def main():
    add_item(input("What would you like to add to the shopping list? "))
    print(f"Current shopping list: {shopping_list}")

if __name__ == '__main__':
    main()
