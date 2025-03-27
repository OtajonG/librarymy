import sqlite3

try:
    import sqlite3
    print("sqlite3 module is available.")
    print(f"SQLite version: {sqlite3.sqlite_version}")
except ImportError:
    print("sqlite3 module is not available.")
 Otajon, [3/25/2025 3:17 PM]
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


def add_book(isbn, title, author, language, publication_year, pdf_path=None):
    """Add a new book to the database with an optional PDF file."""
    with connect_db() as conn:
        cursor = conn.cursor()

        pdf_file_path = None  # Default to None if no file is uploaded
        if pdf_path:
            pdf_file_path = os.path.join(UPLOAD_FOLDER, f"{isbn}.pdf")
            try:
                with open(pdf_file_path, "wb") as f:
                    f.write(pdf_path.read())  # Save the PDF file
            except Exception as e:
                print(f"Error saving PDF: {e}")
                return

        try:
            cursor.execute(
                """
                INSERT INTO Books (ISBN, Title, Author, Language, PublicationYear, PDFPath)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (isbn, title, author, language, publication_year, pdf_file_path),
            )
            conn.commit()
            print("Book added successfully!")
        except sqlite3.IntegrityError:
            print(f"Error: Book with ISBN {isbn} already exists.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")


def get_book(isbn):
    """Retrieve a book's details by ISBN."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE ISBN = ?", (isbn,))
        book = cursor.fetchone()
        return dict(book) if book else None


def get_all_books():
    """Retrieve all books from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        return [dict(book) for book in books]


def update_book(isbn, title, author, language, publication_year, pdf_path=None):
    """Update book details including optional PDF file."""
    with connect_db() as conn:
        cursor = conn.cursor()

        pdf_file_path = None
        if pdf_path:
            pdf_file_path = os.path.join(UPLOAD_FOLDER, f"{isbn}.pdf")
            try:
                with open(pdf_file_path, "wb") as f:
                    f.write(pdf_path.read())  # Save the new PDF file
            except Exception as e:
                print(f"Error saving PDF: {e}")
                return

            cursor.execute(
                """
                UPDATE Books 
                SET Title=?, Author=?, Language=?, PublicationYear=?, PDFPath=?
                WHERE ISBN=?
                """,
                (title, author, language, publication_year, pdf_file_path, isbn),
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
        print(f"Book {isbn} updated successfully!")
    except sqlite3.Error as e:
        print(f"Database error: {e}")


def delete_book(isbn):
    """Delete a book from the database by ISBN."""
    with connect_db() as conn:
        cursor = conn.cursor()

        # Check if the book exists before deleting
        cursor.execute("SELECT PDFPath FROM Books WHERE ISBN = ?", (isbn,))
        book = cursor.fetchone()

        if book:
            pdf_path = book["PDFPath"]
            if pdf_path and os.path.exists(pdf_path):
                try:
                    os.remove(pdf_path)  # Delete the associated PDF file
                except Exception as e:
                    print(f"Error deleting PDF: {e}")

Otajon, [3/25/2025 3:17 PM]
cursor.execute("DELETE FROM Books WHERE ISBN = ?", (isbn,))
            conn.commit()
            print(f"Book {isbn} deleted successfully!")
        else:
            print(f"No book found with ISBN {isbn}.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")


def search_books(query, publication_year=None): # Add publication_year parameter
    """Search for books by title, author, language, or publication year."""
    with connect_db() as conn:
        cursor = conn.cursor()

        query = f"%{query}%"  # Prepare for SQL LIKE search
        sql = "SELECT * FROM Books WHERE Title LIKE ? OR Author LIKE ? OR Language LIKE ?"
        params = [query, query, query]

        if publication_year:  # Add this block to include publication year
            sql += " AND PublicationYear = ?"
            params.append(publication_year)

        cursor.execute(sql, params)
        books = cursor.fetchall()

        return [dict(book) for book in books]