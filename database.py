import sqlite3

conn = sqlite3.connect("bodyprogress.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS measurements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    weight REAL,
    bodyfat REAL,
    muscle REAL,
    visceral_fat REAL
)
""")

conn.commit()
conn.close()

print("Database initialized.")