library = []

def add_book(title, author):
    library.append({'title': title, 'author': author})
    print(f"Added {title} by {author} to the library.")

def main():
    add_book('1984', 'George Orwell')
    print(f"Library contents: {library}")

if __name__ == '__main__':
    main()
