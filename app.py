import sqlite3

DATABASE_FILE = 'librarymy_db.db'

def connect_db():
    """Connects to the library database."""
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def close_db(conn):
    """Closes the database connection."""
    conn.close()

def add_book(isbn, title, author, publisher): # Corrected to accept publisher
    """Adds a new book to the database."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Books (ISBN, Title, Author, Publisher)
            VALUES (?, ?, ?, ?)
        ''', (isbn, title, author, publisher))
        conn.commit()
        print("Book added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Book with ISBN {} already exists.".format(isbn))
    finally:
        close_db(conn)

# ... (other functions) ...

