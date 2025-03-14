import sqlite3

try:
    import sqlite3
    print("sqlite3 module is available.")
    print(f"SQLite version: {sqlite3.sqlite_version}")
except ImportError:
    print("sqlite3 module is not available.")
    #text