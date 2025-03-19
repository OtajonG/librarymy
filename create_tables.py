import sqlite3

conn = sqlite3.connect(r"C:\Users\OTAJON\Desktop\librarymy\librarymy_db.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Books (
        ISBN TEXT PRIMARY KEY,
        Title TEXT,
        Language TEXT,
        Author TEXT,
        PublicationYear INTEGER
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Members (
        MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Address TEXT,
        Phone TEXT
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Loans (
        LoanID INTEGER PRIMARY KEY AUTOINCREMENT,
        MemberID INTEGER,
        ISBN TEXT,
        LoanDate TEXT,
        ReturnDate TEXT,
        FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
        FOREIGN KEY (ISBN) REFERENCES Books(ISBN)
    )
"""
)

conn.commit()
conn.close()

print("Tables created successfully!")
