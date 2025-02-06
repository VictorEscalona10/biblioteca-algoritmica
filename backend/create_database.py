import sqlite3
import os

def createDB():
    
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    connect = sqlite3.connect(db_path)

    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (user TEXT, password INTEGER)")
    connect.commit()

    cursor.execute("INSERT INTO users (user, password) VALUES (?, ?)", ('admin', 1234))
    connect.commit()

    connect.close()

createDB()
