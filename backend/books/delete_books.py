import sqlite3
import os
from pydantic import ValidationError

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.book import Book

def delete_book(title, author, category, link=''):
    try:
        book = Book(title=title, author=author, category=category)
    except ValidationError as e:
        error = e.errors()[0]
        field = error['loc'][0]
        msg = error['msg']
        return f"Error en {field}: {msg}"
    
    try:
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        
        title = title.lower()
        author = author.lower()
        category = category.lower()
        link = link.lower() if link else link

        # Corrected SQL query with proper WHERE clause and parameters
        cursor.execute(
            """DELETE FROM books 
            WHERE title = ? AND author = ? AND category = ? AND link = ?""", 
            (book.title, book.author, book.category, link)
        )
        
        connect.commit()  # Don't forget to commit the changes
        
        # Check if any row was affected
        if cursor.rowcount == 0:
            return "No se encontró el libro para eliminar"
            
        return "Libro eliminado exitosamente"
        
    except sqlite3.IntegrityError:
        return "Error de integridad al eliminar el libro"
    except Exception as e:
        print(f"Error inesperado: {e}")
        return f"Error al eliminar el libro: {str(e)}"
    finally:
        if 'connect' in locals():
            connect.close()