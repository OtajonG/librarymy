from librarymy_db import add_book, get_book, get_all_books, update_book, delete_book, search_books

def run_tests():
    print("\n=== Running Database Tests ===")

    # Add test data
    print("\n--- Adding Test Books ---")
    try:
        add_book("978-0345391803", "The Hitchhiker's Guide", "Douglas Adams", "English", None)
        add_book("978-1234567890", "Python Crash Course", "Eric Matthes", "English", 2019)
        add_book("978-0987654321", "Learning SQL", "Alan Beaulieu", "English", 2020)
        add_book("978-1122334455", "Data Science for Dummies", "Lillian Pierson", "English", 2017)
        print("Books added successfully!")
    except Exception as e:
        print("Error adding books:", e)

    # Test Read (get_book)
    print("\n--- Test Read (get_book) ---")
    try:
        book = get_book("978-0345391803")
        print("Book found:", book)
    except Exception as e:
        print("Error fetching book:", e)

    # Test Read (get_all_books)
    print("\n--- Test Read (get_all_books) ---")
    try:
        all_books = get_all_books()
        print(f"Total books found: {len(all_books)}")
        for book in all_books:
            print(book)
    except Exception as e:
        print("Error fetching all books:", e)

    # Test Update
    print("\n--- Test Update ---")
    try:
        update_book("978-0345391803", "The Hitchhiker's Guide (Updated)", "Douglas Adams", "English", None)
        print("Book updated successfully!")
        print("Updated Book:", get_book("978-0345391803"))
    except Exception as e:
        print("Error updating book:", e)

    # Test Delete (Uncomment to enable deletion test)
    # print("\n--- Test Delete ---")
    # try:
    #     delete_book("978-0345391803")
    #     print("Book deleted successfully!")
    # except Exception as e:
    #     print("Error deleting book:", e)

    # Test Search Functionality
    print("\n--- Search Books Tests ---")
    search_queries = [
        "The Hitchhiker's Guide",
        "Douglas Adams",
        "Hitch",
        "Adam",
        "Python",
        "SQL",
        "Data",
        "douglas adams",  # Case insensitive test
        "Nonexistent Book",  # Should return no results
        "Random Author"
    ]

    for query in search_queries:
        try:
            results = search_books(query)
            print(f"\nSearch for '{query}': Found {len(results)} result(s).")
            for book in results:
                print(book)
        except Exception as e:
            print(f"Error searching for '{query}':", e)

    print("\n=== Database Tests Completed ===")

# Run the test script
if __name__ == "__main__":
    run_tests()