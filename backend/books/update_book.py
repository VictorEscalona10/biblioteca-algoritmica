import sqlite3
import os

def update_book(title, author=None, link=None, isCheckedOut=None):
    try:
        # Ruta a la base de datos
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # Verificar si el libro existe en la base de datos
        cursor.execute("SELECT title FROM books WHERE title = ?", (title,))
        if not cursor.fetchone():
            print(f"Error: El libro '{title}' no existe en la base de datos.")
            return False

        # Construir la consulta de actualización dinámicamente
        update_query = "UPDATE books SET"
        update_params = []

        if author is not None:
            update_query += " author = ?,"
            update_params.append(author)
        if link is not None:
            update_query += " link = ?,"
            update_params.append(link)
        if isCheckedOut is not None:
            update_query += " is_checked_out = ?,"
            update_params.append(isCheckedOut)

        # Eliminar la última coma y agregar la condición WHERE
        update_query = update_query.rstrip(',') + " WHERE title = ?"
        update_params.append(title)

        # Ejecutar la consulta de actualización
        cursor.execute(update_query, tuple(update_params))
        connect.commit()

        print(f"El libro '{title}' ha sido actualizado correctamente.")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        # Cerrar la conexión a la base de datos
        if 'cursor' in locals():
            cursor.close()
        if 'connect' in locals():
            connect.close()

# Para probar la funcion
# update_book('El libro de mari', 'mariangela', isCheckedOut=1)