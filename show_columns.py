import sqlite3

conn = sqlite3.connect("bodyprogress.db")

cursor = conn.cursor()

rows = cursor.execute(
    "PRAGMA table_info(measurements)"
).fetchall()

for row in rows:
    print(row)

conn.close()