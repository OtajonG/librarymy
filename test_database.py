from database import *

# Test Create
add_book("978-0345391803", "The Hitchhiker's Guide to the Galaxy", "English", "Douglas Adams")

# Test Read (get_book)
book = get_book("978-0345391803")
print("Book by ISBN:", book)

# Test Read (get_all_books)
all_books = get_all_books()
print("All books:", all_books)

# Test Update
update_book("978-0345391803", "The Hitchhiker's Guide", "English", "Douglas Adams")

# Test Delete
# delete_book("978-0345391803")