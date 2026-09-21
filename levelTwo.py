import sqlite3

connection = sqlite3.connect("people.db")
cursor = connection.cursor()


city = "Kathmandu"

cursor.execute("""
    SELECT * FROM people
    WHERE city = ?
""", (city,))

people = cursor.fetchall()

print(people)
cursor.execute("""
    SELECT * FROM people
    WHERE score >50
""")
people = cursor.fetchall()

print(people)
cursor.execute("""
    SELECT * FROM people
    ORDER BY score DESC
    LIMIT 5
""")
people = cursor.fetchall()

print(people)
cursor.execute("""
    SELECT * FROM people
    ORDER BY age ASC
""")


people = cursor.fetchall()

print(people)