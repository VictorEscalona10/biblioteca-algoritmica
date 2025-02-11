import sqlite3
import os

def update_book(title, new_title=None, author=None, category=None, link=None):
    try:
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # Validar que el título no esté vacío
        if not title:
            print("El título no puede estar vacío.")
            return False

        # Obtener el registro actual del libro
        cursor.execute("SELECT title, author, category, link FROM books WHERE title = ?", (title,))
        current_book = cursor.fetchone()

        if not current_book:
            print("Libro no encontrado.")
            return False

        # Preparar los nuevos valores, manteniendo los actuales si no se proporciona un nuevo valor
        updated_title = new_title if new_title is not None and new_title != '' else current_book[0]
        updated_author = author if author is not None and author != '' else current_book[1]
        updated_category = category if category is not None and category != '' else current_book[2]
        updated_link = link if link is not None and link != '' else current_book[3]

        # Actualizar el registro en la base de datos
        cursor.execute("""
            UPDATE books
            SET title = ?, author = ?, category = ?, link = ?
            WHERE title = ?
        """, (updated_title, updated_author, updated_category, updated_link, title))

        connect.commit()
        print("Libro actualizado correctamente.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connect.close()

# Ejemplo de uso
update_book('El libro de mari', new_title='El libro de Mari actualizado', author='Mari Sánchez')