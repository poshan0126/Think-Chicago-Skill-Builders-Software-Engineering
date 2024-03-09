
# The Welcoming Program

# Task 1: Personalized Greeting
def personalized_greeting():
    name = input("What's your name? ")
    print(f"Hello, {name}! Nice to meet you.")

# Task 2: Respond Based on Feeling
def ask_feeling():
    feeling = input("How are you feeling today? ")
    if 'sad' in feeling.lower() or 'down' in feeling.lower():
        print("I'm sorry to hear that. I hope things get better soon.")
    else:
        print("That's great to hear!")

# Task 3: Error Handling for Name Input
def get_name():
    while True:
        name = input("Please enter your name (letters only): ")
        if name.isalpha():
            print(f"Hello, {name}! How can I assist you today?")
            break
        else:
            print("Invalid input. Please use letters only.")

# Function Calls
personalized_greeting()
ask_feeling()
get_name()
