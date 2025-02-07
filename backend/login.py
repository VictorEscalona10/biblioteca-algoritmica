import sqlite3
import os
import bcrypt

def login(user, password):
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        password = str(password).encode('utf-8')  # Convierte la contraseña a bytes

        cursor.execute("SELECT password FROM users WHERE user = ?", (user,))
        result = cursor.fetchone()
        
        if result and bcrypt.checkpw(password, result[0]):
            return True  # Usuario y contraseña correctos
        else:
            return False  # Usuario o contraseña incorrectos
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connect.close()
