import sqlite3
import os

# Define database path dynamically
DATABASE_FILE = os.path.join(os.path.dirname(__file__), "librarymy_db.db")

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

# Commit and close connection
conn.commit()
conn.close()

print("✅ Tables created successfully!")