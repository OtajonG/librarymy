import sqlite3
import os

# Database and upload folder configurations
DATABASE_FILE = "librarymy_db.db"
UPLOAD_FOLDER = "uploads"

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def add_book(isbn, title, author, language, publication_year, pdf_file=None):
    """Add a new book to the database with an optional PDF file."""
    conn = connect_db()
    cursor = conn.cursor()

    pdf_path = None  # Default to None if no file is uploaded
    if pdf_file:
        pdf_path = os.path.join(UPLOAD_FOLDER, f"{isbn}.pdf")
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())  # Save the PDF file

    try:
        cursor.execute(
            """
            INSERT INTO Books (ISBN, Title, Author, Language, PublicationYear, PDFPath)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (isbn, title, author, language, publication_year, pdf_path),
        )
        conn.commit()
        print("Book added successfully!")
    except sqlite3.IntegrityError:
        print(f"Error: Book with ISBN {isbn} already exists.")
    finally:
        conn.close()


def get_book(isbn):
    """Retrieve a book's details by ISBN."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books WHERE ISBN = ?", (isbn,))
    book = cursor.fetchone()
    conn.close()
    return dict(book) if book else None


def get_all_books():
    """Retrieve all books from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    conn.close()
    return [dict(book) for book in books]


def update_book(isbn, title, author, language, publication_year, pdf_file=None):
    """Update book details including optional PDF file."""
    conn = connect_db()
    cursor = conn.cursor()

    pdf_path = None
    if pdf_file:
        pdf_path = os.path.join(UPLOAD_FOLDER, f"{isbn}.pdf")
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())  # Save the new PDF file

        cursor.execute(
            """
            UPDATE Books 
            SET Title=?, Author=?, Language=?, PublicationYear=?, PDFPath=?
            WHERE ISBN=?
            """,
            (title, author, language, publication_year, pdf_path, isbn),
        )
    else:
        cursor.execute(
            """
            UPDATE Books 
            SET Title=?, Author=?, Language=?, PublicationYear=?
            WHERE ISBN=?
            """,
            (title, author, language, publication_year, isbn),
        )

    conn.commit()
    conn.close()
    print(f"Book {isbn} updated successfully!")


def delete_book(isbn):
    """Delete a book from the database by ISBN."""
    conn = connect_db()
    cursor = conn.cursor()

    # Check if the book exists before deleting
    cursor.execute("SELECT PDFPath FROM Books WHERE ISBN = ?", (isbn,))
    book = cursor.fetchone()

    if book:
        pdf_path = book["PDFPath"]
        if pdf_path and os.path.exists(pdf_path):
            os.remove(pdf_path)  # Delete the associated PDF file

        cursor.execute("DELETE FROM Books WHERE ISBN = ?", (isbn,))
        conn.commit()
        print(f"Book {isbn} deleted successfully!")
    else:
        print(f"No book found with ISBN {isbn}.")

    conn.close()


def search_books(query):
    """Search for books by title, author, or language."""
    conn = connect_db()
    cursor = conn.cursor()

    query = f"%{query}%"  # Prepare for SQL LIKE search
    cursor.execute(
        """
        SELECT * FROM Books 
        WHERE Title LIKE ? OR Author LIKE ? OR Language LIKE ?
        """,
        (query, query, query),
    )

    books = cursor.fetchall()
    conn.close()
    return [dict(book) for book in books]