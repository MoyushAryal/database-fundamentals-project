import sqlite3

connection = sqlite3.connect("people.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT,
        score REAL

    )
""")

connection.commit()

