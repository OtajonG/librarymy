from database import add_book, get_book, get_all_books, update_book, delete_book, search_books

# Add test data
add_book("978-0345391803", "The Hitchhiker's Guide", "English", "Douglas Adams", None)
add_book("978-1234567890", "Python Crash Course", "English", "Eric Matthes", 2019)
add_book("978-0987654321", "Learning SQL", "English", "Alan Beaulieu", 2020)
add_book("978-1122334455", "Data Science for Dummies", "English", "Lillian Pierson", 2017)

# Test Read (get_book)
print("\n--- Test Read (get_book) ---")
book = get_book("978-0345391803")
print("Book by ISBN:", book)

# Test Read (get_all_books)
print("\n--- Test Read (get_all_books) ---")
all_books = get_all_books()
print("All books:", all_books)

# Test Update
print("\n--- Test Update ---")
update_book("978-0345391803", "The Hitchhiker's Guide Updated", "English", "Douglas Adams", None)
print("Book updated successfully!")

# Test Delete (Uncomment to test)
# print("\n--- Test Delete ---")
# delete_book("978-0345391803")
# print("Book deleted successfully!")

# Search books tests
print("\n--- Search Books Tests ---")

# Exact matches:
print("Search for 'The Hitchhiker's Guide':", search_books("The Hitchhiker's Guide"))
print("Search for 'Douglas Adams':", search_books("Douglas Adams"))

# Partial matches:
print("Search for 'Hitch':", search_books("Hitch"))
print("Search for 'Adam':", search_books("Adam"))
print("Search for 'Python':", search_books("Python"))
print("Search for 'SQL':", search_books("SQL"))
print("Search for 'Data':", search_books("Data"))

# Case-insensitive matches:
print("Search for 'douglas adams':", search_books("douglas adams"))

# No matches:
print("Search for 'Nonexistent Book':", search_books("Nonexistent Book"))
print("Search for 'Random Author':", search_books("Random Author"))

# Print all books
print("\n--- All Books ---")
all_books = get_all_books()
for book in all_books:
    print(book)