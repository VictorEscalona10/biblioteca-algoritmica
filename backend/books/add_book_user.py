import sqlite3
import os

def add_book_to_user(username, title_book):
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')

    try:
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        cursor.execute("SELECT id FROM users WHERE user = ?", (username,))
        user_id = cursor.fetchone()[0]
        print(user_id)

        cursor.execute("SELECT id FROM books WHERE title = ?", (title_book,))
        book_id = cursor.fetchone()[0]
        print(book_id)

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
# add_book_to_user('victor', 'El Principito')
