
import sqlite3

conn = sqlite3.connect('usuarios.db')
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)''')
conn.close()

print('Base de datos creada exitosamente.')
