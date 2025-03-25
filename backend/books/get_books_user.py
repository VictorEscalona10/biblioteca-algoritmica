import sqlite3
import os

def get_books_user(username):
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
    
    try:
        # Conexión a la base de datos
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # Obtén el ID del usuario según el nombre de usuario
        cursor.execute("SELECT id FROM users WHERE user = ?", (username,))
        user = cursor.fetchone()

        if not user:
            return f"Usuario '{username}' no encontrado."

        user_id = user[0]

        # Obtén los libros asociados al usuario
        query = """
            SELECT books.title, books.author, books.link, books.category
            FROM user_books
            JOIN books ON user_books.book_id = books.id
            WHERE user_books.user_id = ?
        """
        cursor.execute(query, (user_id,))
        books = cursor.fetchall()

        if not books:
            return f"El usuario '{username}' no tiene libros registrados."
        
        # Devuelve los libros en un formato más legible
        return [
            {"title": book[0], "author": book[1], "link": book[2], "category": book[3]}
            for book in books
        ]

    except Exception as e:
        print(f"Error: {e}")
        return "Error al obtener los libros"

    finally:
        # Asegúrate de cerrar la conexión
        connect.close()

# Prueba la función
result = get_books_user('user')
print(result)
