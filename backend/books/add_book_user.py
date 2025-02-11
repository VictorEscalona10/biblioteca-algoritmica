import sqlite3
import os

def add_book_to_user(user_id, book_id):
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')

    try:
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # Insertar un registro en la tabla user_books
        cursor.execute("""
            INSERT INTO user_books (user_id, book_id)
                VALUES (?, ?)
            """, (user_id, book_id))
        connect.commit()

    except sqlite3.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")
    finally:
        if connect:
            connect.close()

# Ejemplo de uso: Agregar el libro con ID 1 al usuario con ID 1
# add_book_to_user(1, 1)
