import sqlite3

def connect_db():
    """Connects to the library database."""
    conn = sqlite3.connect('librarymy_db.db')
    return conn

def close_db(conn):
    """Closes the database connection."""
    conn.close()

def add_book(isbn, title, language, author):
    """Adds a new book to the database."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Books (ISBN, Title, Language, Author)
            VALUES (?, ?, ?, ?)
        ''', (isbn, title, language, author))
        conn.commit()
        print("Book added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Book with ISBN {} already exists.".format(isbn))
    finally:
        close_db(conn)

def get_book(isbn):
    """Retrieves a book from the database by ISBN."""

    def get_book(isbn):
        print(f"DEBUG: Searching for ISBN: {isbn}")  # Add this line
        try:
            # Your database code here...
            # Example for SQLite:
            conn = sqlite3.connect('your_database.db')  # change your_database.db to your database name.
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
            book = cursor.fetchone()
            conn.close()

            if book:
                print(f"DEBUG: Book found: {book}")  # Add this line
                # Your code to format the book data...
                return {
                    "isbn": book[0],
                    "title": book[1],
                    # ... other fields ...
                }
            else:
                print(f"DEBUG: Book not found in database for ISBN: {isbn}")  # add this line
                return None
        except Exception as e:
            print(f"DEBUG: Error in get_book: {e}")  # Add this line
            return None
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Books WHERE ISBN = ?
    ''', (isbn,))
    book = cursor.fetchone()
    close_db(conn)
    return book

def get_all_books():
    """Retrieves all books from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Books
    ''')
    books = cursor.fetchall()
    close_db(conn)
    return books

def update_book(isbn, title, language, author):
    """Updates a book's information in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Books
        SET Title = ?, Language = ?, Author = ?
        WHERE ISBN = ?
    ''', (title, language, author, isbn))
    conn.commit()
    close_db(conn)
    print("Book updated successfully!")

def delete_book(isbn):
    """Deletes a book from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Books WHERE ISBN = ?
    ''', (isbn,))
    conn.commit()
    close_db(conn)
    print("Book deleted successfully!")


def search_books(query):
    conn = connect_db()  # Corrected function name
    cursor = conn.cursor()
    query = "%" + query + "%"  # Add wildcards for LIKE operator
    cursor.execute("SELECT * FROM Books WHERE Title LIKE ? OR Author LIKE ?", (query, query))  # Corrected column names
    books = cursor.fetchall()
    close_db(conn)  # Corrected function name
    return books

    def add_book(isbn, title, language, author, publication_year):
        """Adds a new book to the database."""
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Books (ISBN, Title, Language, Author, PublicationYear)
                VALUES (?, ?, ?, ?, ?)
            ''', (isbn, title, language, author, publication_year))
            conn.commit()
            print("Book added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Book with ISBN {} already exists.".format(isbn))
        finally:
            close_db(conn)