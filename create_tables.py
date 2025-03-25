import sqlite3
import os

# Define database path dynamically
script_dir = os.path.dirname(os.path.abspath(file)) #get the absolute directory of the script
DATABASE_FILE = os.path.join(script_dir, "librarymy_db.db")

try:
    # Connect to the database
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Create Books table with a PdfPath column
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            ISBN TEXT PRIMARY KEY,
            Title TEXT NOT NULL,
            Author TEXT NOT NULL,
            Language TEXT,
            PublicationYear INTEGER,
            PdfPath TEXT  -- Column to store PDF file path
        )
    """)

    # Create Members table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Members (
            MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Address TEXT,
            Phone TEXT
        )
    """)

    # Create Loans table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Loans (
            LoanID INTEGER PRIMARY KEY AUTOINCREMENT,
            MemberID INTEGER NOT NULL,
            ISBN TEXT NOT NULL,
            LoanDate TEXT,
            ReturnDate TEXT,
            FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
            FOREIGN KEY (ISBN) REFERENCES Books(ISBN)
        )
    """)

    # Commit the changes
    conn.commit()
    print(f"✅ Tables created successfully in {DATABASE_FILE}!")

except sqlite3.Error as e:
    print(f"❌ An error occurred: {e}")

finally:
    if conn:
        conn.close()