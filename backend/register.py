import os
import bcrypt
import sqlite3
from pydantic import ValidationError

from models.user import User

def register_user(name, email, password, repeatPassword):

    try:
        if password != repeatPassword:
            return 'Ambas contraseñas no coinciden'

        user = User(name=name, email=email, password=password, repeatPassword=repeatPassword)
        
    except ValidationError as e:
        print("Error de validación:", e)
        return f"Error de validación: {e}"

    try:
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user.name = user.name.lower()
        
        cursor.execute("""
            INSERT INTO users (user, password, email)
                VALUES (?, ?, ?)
            """, (user.name, hashed_password, user.email))
        connect.commit()
        
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connect.close()

    return "Usuario registrado con éxito"

# Probar la función
print(register_user('victor', 'victor@gmail.com', 'Victor10#', 'Victor10#'))
