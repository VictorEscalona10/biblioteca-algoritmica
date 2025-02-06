import sqlite3
import os

def login(user, password):
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM users WHERE user = ? AND password = ?", (user, password))
        result = cursor.fetchone()
        if result:
            return True  # Usuario y contraseña correctos
        else:
            return False  # Usuario o contraseña incorrectos
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connect.close()
    
    


