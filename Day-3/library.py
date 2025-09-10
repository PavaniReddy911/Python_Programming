library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    if book_id in library:
        print(f"Book ID {book_id} already exists with title: '{library[book_id]}'")
    else:
        library[book_id] = title
        print(f"Book '{title}' added with ID {book_id}.")


def remove_book():
    book_id = input("Enter Book ID to remove: ")
    if book_id in library:
        removed_title = library.pop(book_id)
        print(f"Book '{removed_title}' with ID {book_id} removed.")
    else:
        print(f"No book found with ID {book_id}.")

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in library:
        print(f"Book ID {book_id} → Title: '{library[book_id]}'")
    else:
        print(f"No book found with ID {book_id}.")

def update_book():
    book_id = input("Enter Book ID to update: ")
    if book_id in library:
        new_title = input("Enter new title: ")
        old_title = library[book_id]
        library[book_id] = new_title
        print(f"Book ID {book_id} updated from '{old_title}' to '{new_title}'.")
    else:
        print(f"No book found with ID {book_id}.")

def display_books():
    if library:
        print("All books in the library:")
        for book_id, title in library.items():
            print(f"ID: {book_id} → Title: '{title}'")
    else:
        print("Library is empty.")

def count_books():
    print(f"Total number of books in the library: {len(library)}")

def title_exists():
    title = input("Enter Book Title to check: ")
    if title in library.values():
        print(f"The book title '{title}' exists in the library.")
    else:
        print(f"The book title '{title}' does not exist in the library.")

while True:
    print("\n Library Management System ")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Update Book Title")
    print("5. Display All Books")
    print("6. Count Total Books")
    print("7. Check if Book Title Exists")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        search_book()
    elif choice == '4':
        update_book()
    elif choice == '5':
        display_books()
    elif choice == '6':
        count_books()
    elif choice == '7':
        title_exists()
    elif choice == '8':
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
