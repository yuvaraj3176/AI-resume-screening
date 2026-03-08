import sqlite3

conn = sqlite3.connect("instance/database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
email TEXT,
password TEXT,
role TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")