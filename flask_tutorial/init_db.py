import sqlite3

connection = sqlite3.connect("database.db")


with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO notes (title, description) VALUES (?, ?)",
    ("Note 1", "my first note!"),
)

cur.execute(
    "INSERT INTO notes (title, description) VALUES (?, ?)",
    ("Note 2", "my second note?"),
)

connection.commit()
connection.close()
