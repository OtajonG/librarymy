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
                (isbn, title, author, language, publication_year, os.path.basename(pdf_path) if pdf_path else None),
            )
            conn.commit()
            print("✅ Book added successfully!")
        except sqlite3.IntegrityError:
            print(f"❌ Error: Book with ISBN {isbn} already exists.")


def search_books(query, language=None, publication_year=None):
    """Searches for books based on a query and optional filters."""
    sql = "SELECT * FROM Books WHERE (Title LIKE ? OR Author LIKE ?)"
    params = ["%" + query + "%", "%" + query + "%"]

    if language:
        sql += " AND Language = ?"
        params.append(language)

    if publication_year:
        sql += " AND PublicationYear = ?"
        params.append(publication_year)

    print("SQL Query:", sql)
    print("Parameters:", params)

    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        books = cursor.fetchall()

    print("Query Results:", books)

    return [dict(book) for book in books]


def get_all_books():
    """Retrieves all books from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ISBN, Title, Author, Language, PublicationYear, pdf_path FROM Books")
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


if __name__ == "__main__":
    create_books_table()
