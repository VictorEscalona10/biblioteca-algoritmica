import sqlite3
import os
import bcrypt

def createDB():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')

    try:
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # Crear tablas y realizar inserciones
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )""")
        connect.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                author TEXT NOT NULL,
                link TEXT,
                category TEXT NOT NULL,
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            )""")
        connect.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_books (
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                PRIMARY KEY (user_id, book_id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )""")
        connect.commit()

        password = '1234'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        cursor.execute("""
            INSERT INTO users (user, password, email)
                VALUES ('admin', ?, 'email@email.com')
            """, (hashed_password,))
        connect.commit()

    except sqlite3.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")
    finally:
        if connect:
            connect.close()

createDB()
