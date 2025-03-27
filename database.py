import sqlite3
import os

DATABASE_FILE = "librarymy_db.db"


def connect_db():
    """Connects to the library database, creating it if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # Allows access to results as dictionaries
    return conn


def add_book(isbn, title, author, language, publication_year, pdf_path=None):
    """Adds a new book to the database, including an optional PDF file."""
    with connect_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO Books (ISBN, Title, Author, Language, PublicationYear, pdf_path)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (isbn, title, author, language, publication_year, pdf_path),
            )
            conn.commit()
            print("✅ Book added successfully!")
        except sqlite3.IntegrityError:
            print(f"❌ Error: Book with ISBN {isbn} already exists.")


def search_books(query, publication_year=None, language=None):
    """Searches for books matching the query."""
    with connect_db() as conn:
        cursor = conn.cursor()

        sql = "SELECT * FROM Books WHERE (Title LIKE ? OR Author LIKE ?)"
        params = ["%" + query + "%", "%" + query + "%"]

        if publication_year:
            sql += " AND PublicationYear = ?"
            params.append(publication_year)

        if language:
            sql += " AND Language = ?"
            params.append(language)

        print("🔍 SQL Query:", sql)
        print("📌 Parameters:", params)

        cursor.execute(sql, params)
        books = cursor.fetchall()
        return [dict(book) for book in books]


def search_books(query, publication_year=None, language=None):
    # ... (rest of the code)

    print("SQL Query:", sql)
    print("Parameters:", params)

    cursor.execute(sql, params)
    books = cursor.fetchall()

    print("Query Results:", books)  # Add this line to debug

    return [dict(book) for book in books]


def get_all_books():
    """Retrieves all books from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        return [dict(book) for book in books]


def create_books_table():
    """Creates the Books table if it doesn't exist."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Books (
                ISBN TEXT PRIMARY KEY,
                Title TEXT NOT NULL,
                Author TEXT NOT NULL,
                Language TEXT,
                PublicationYear INTEGER,
                pdf_path TEXT
            )
        """
        )
        conn.commit()
        print("📚 Books table created successfully!")
