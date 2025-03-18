import sqlite3
import os

DATABASE_FILE = 'librarymy_db.db'

def connect_db():
    """Connects to the library database."""
    if not os.path.exists(DATABASE_FILE):
        print(f"Error: Database file '{DATABASE_FILE}' not found.")
        return None
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def close_db(conn):
    """Closes the database connection."""
    if conn:
        conn.close()

def add_book(isbn, title, author, language, publication_year):
    """Adds a new book to the database."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Books (ISBN, Title, Author, Language, PublicationYear)
                VALUES (?, ?, ?, ?, ?)
            ''', (isbn, title, author, language, publication_year))
            conn.commit()
            print("Book added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Book with ISBN {} already exists.".format(isbn))
        finally:
            close_db(conn)

def search_books(query, publication_year, language):
    """Searches for books with required language and publication year."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM Books WHERE (Title LIKE ? OR Author LIKE ?) AND PublicationYear = ? AND Language = ?"
        params = ('%' + query + '%', '%' + query + '%', publication_year, language)

        print("SQL:", sql)  # Print the SQL query
        print("Params:", params) # Print the parameters

        cursor.execute(sql, params)
        books = cursor.fetchall()
        close_db(conn)
        return books
    return []
