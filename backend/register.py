import sqlite3
import os
import bcrypt

def register(name, email, password, repeatPassword):
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')

    try:
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        
    except sqlite3.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")
    finally:
        if connect:
            connect.close()
