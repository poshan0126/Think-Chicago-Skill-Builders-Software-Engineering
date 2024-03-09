
# The Personal Library Organizer

library = []

# Task 1: Add Books
def add_book(title, author, genre):
    library.append({'title': title, 'author': author, 'genre': genre})
    print(f"Book '{title}' by {author} added to the library.")

# Task 2: Search Function
def search_books(search_term):
    results = [book for book in library if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
    return results

# Task 3: Display Books
def display_books(sort_by='title'):
    sorted_library = sorted(library, key=lambda x: x[sort_by])
    for book in sorted_library:
        print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

# Sample Function Calls
add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
add_book("1984", "George Orwell", "Dystopian")
results = search_books("1984")
print("Search Results:")
for result in results:
    print(f"Title: {result['title']}, Author: {result['author']}")
display_books('genre')
