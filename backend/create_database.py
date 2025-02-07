import sqlite3
import os

def createDB():
    
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    connect = sqlite3.connect(db_path)

    cursor = connect.cursor()

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
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )""")
    connect.commit()

    connect.close()

createDB()

