'''
ESTE ARCHIVO ESTA SOLO SI LA BASE DE DATOS NO ESTA EN SU REPOSITORIO LOCAL O EL ARCHIVO ESTA CORRUPTO.
POR FAVOR NO DESPLEGAR ESTE ARCHIVO A PRODUCCION, SE SUBIRA A PRODUCCION LA BASE DE DATOS CON EL USUARIO
ADMINISTRADOR YA REGISTRADO EN ELLA
'''

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
                password TEXT NOT NULL
            )""")
        connect.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                author TEXT NOT NULL,
                link TEXT,
                is_checked_out INTEGER CHECK(is_checked_out IN (0, 1)) DEFAULT 0,
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            )""")
        connect.commit()

        password = '1234'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        cursor.execute("""
            INSERT INTO users (user, password)
                VALUES ('admin', ?)
            """, (hashed_password,))
        connect.commit()

    except sqlite3.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")
    finally:
        if connect:
            connect.close()

createDB()