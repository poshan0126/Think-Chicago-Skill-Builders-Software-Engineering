def main():
    name = input("What is your name? ")
    print(f"Hello, {name}! How are you feeling today?")
    mood = input()
    if 'sad' in mood.lower() or 'down' in mood.lower():
        print("I'm sorry to hear that. I hope things get better soon.")
    else:
        print("That's great to hear!")

if __name__ == '__main__':
    main()
