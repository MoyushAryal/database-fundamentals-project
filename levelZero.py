import sqlite3

connection = sqlite3.connect(
    r"C:\everything\Internship\Task\Task-5\people.db"
)

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

cursor.execute("SELECT * FROM people")

rows = cursor.fetchall()

print(rows)


cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
""")

print(cursor.fetchall())