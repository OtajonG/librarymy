import sqlite3
import os

DATABASE_FILE = 'librarymy_db.db'

def connect_db():
    """Connects to the library database."""
    if not os.path.exists(DATABASE_FILE):
        print(f"Error: Database file '{DATABASE_FILE}' not found.")
        return None
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # Allows access to results as dictionaries
    return conn

def close_db(conn):
    """Closes the database connection."""
    if conn:
        conn.close()

def add_book(isbn, title, author, language, publication_year, pdf_filename=None):
    """Adds a new book to the database, including an optional PDF file."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Books (ISBN, Title, Author, Language, PublicationYear, PDF_File)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (isbn, title, author, language, publication_year, pdf_filename))
            conn.commit()
            print("✅ Book added successfully!")
        except sqlite3.IntegrityError:
            print(f"❌ Error: Book with ISBN {isbn} already exists.")
        finally:
            close_db(conn)

def search_books(query, publication_year=None, language=None):
    """Searches for books matching the query."""
    conn = connect_db()
    if not conn:
        return []

    cursor = conn.cursor()

    # Base SQL query
    sql = "SELECT * FROM Books WHERE (Title LIKE ? OR Author LIKE ?)"
    params = ['%' + query + '%', '%' + query + '%']

    # Add optional filters
    if publication_year:
        sql += " AND PublicationYear = ?"
        params.append(publication_year)

    if language:
        sql += " AND Language = ?"
        params.append(language)

    print("🔍 SQL Query:", sql)  # Debugging: Print the SQL query
    print("📌 Parameters:", params)  # Debugging: Print the parameters

    cursor.execute(sql, params)
    books = cursor.fetchall()
    close_db(conn)

    return [dict(book) for book in books]  # Convert results to list of dictionaries

def get_all_books():
    """Retrieves all books from the database."""
    conn = connect_db()
    if not conn:
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    close_db(conn)

    return [dict(book) for book in books]  # Convert results to dictionaries

def create_books_table():
    """Creates the Books table if it doesn't exist."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                ISBN TEXT PRIMARY KEY,
                Title TEXT NOT NULL,
                Author TEXT NOT NULL,
                Language TEXT,
                PublicationYear INTEGER,
                PDF_File TEXT  -- Stores the filename of the uploaded PDF
            )
        ''')
        conn.commit()
        print("📚 Books table created successfully!")
        close_db(conn)