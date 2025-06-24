import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Usuario de prueba
cursor.execute("INSERT OR IGNORE INTO usuarios (email, password) VALUES (?, ?)", ('admin@mail.com', '1234'))

conn.commit()
conn.close()
