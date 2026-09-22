import sqlite3


def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            city_name TEXT UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS people_new (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            city_id INTEGER,
            score REAL,
            FOREIGN KEY (city_id) REFERENCES cities(id)
        )
    """)


def populate_cities(cursor):
    cursor.execute("""
        SELECT DISTINCT city
        FROM people
    """)

    cities = cursor.fetchall()

    for row in cities:
        city = row[0]

        cursor.execute("""
            INSERT OR IGNORE INTO cities (city_name)
            VALUES (?)
        """, (city,))


def migrate_people(cursor):
    cursor.execute("""
        SELECT *
        FROM people
    """)

    people = cursor.fetchall()

    for row in people:
        city_name = row[3]

        cursor.execute("""
            SELECT id
            FROM cities
            WHERE city_name = ?
        """, (city_name,))

        city = cursor.fetchone()
        city_id = city[0]

        cursor.execute("""
            INSERT INTO people_new (id, name, age, city_id, score)
            VALUES (?, ?, ?, ?, ?)
        """, (row[0], row[1], row[2], city_id, row[4]))


def verify_migration(cursor):
    cursor.execute("""
        SELECT COUNT(*)
        FROM people
    """)

    old_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM people_new
    """)

    new_count = cursor.fetchone()[0]

    print("Old people count:", old_count)
    print("New people count:", new_count)

    if old_count == new_count:
        print("Migration successful!")
    else:
        print("Migration failed!")


def show_joined_data(cursor):
    cursor.execute("""
        SELECT
            people_new.name,
            people_new.age,
            cities.city_name,
            people_new.score
        FROM people_new
        JOIN cities
            ON people_new.city_id = cities.id
    """)

    people = cursor.fetchall()

    for person in people:
        print(person)


connection = sqlite3.connect("people.db")
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS people_new")
cursor.execute("DROP TABLE IF EXISTS cities")

create_tables(cursor)
populate_cities(cursor)
migrate_people(cursor)

connection.commit()

verify_migration(cursor)
show_joined_data(cursor)

connection.close()

