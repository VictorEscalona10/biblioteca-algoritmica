import sqlite3
import os
from pydantic import ValidationError

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.book import Book

def add_book(title, author, category, link = ''):
    try:
        book = Book(title=title, author=author, category=category)
    except ValidationError as e:
        print("Error de validación:", e)
        return f"Error de validación: {e}"

    try:
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        if title == '' or author == '':
            return False

        cursor.execute("""
            INSERT INTO books (title, author, category, link)
                VALUES (?, ?, ?, ?)
            """, (book.title, book.author, book.category, link))
        
        connect.commit()
        return 'Libro agregado correctamente'
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connect.close()

# probar la funcion
add_book('El Principito', 'victor', "fantasia")
        