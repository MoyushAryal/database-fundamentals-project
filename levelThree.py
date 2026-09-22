import sqlite3

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

cursor.execute("""
SELECT city,AVG(score)
FROM people
GROUP BY city """ )

people =cursor.fetchall()
print(people)

cursor.execute("""
SELECT city,COUNT(city)
FROM people
GROUP BY city """ )

people =cursor.fetchall()
print(people)

cursor.execute("""
SELECT city,MAX(age)
FROM people
GROUP BY city """ )

people =cursor.fetchall()
print(people)