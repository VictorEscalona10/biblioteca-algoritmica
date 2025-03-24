import sqlite3
import os
from pydantic import ValidationError

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.book import Book

def add_book(title, author, category, link=''):
    # Primero validamos con Pydantic
    try:
        book = Book(title=title, author=author, category=category)
    except ValidationError as e:
        error = e.errors()[0]
        field = error['loc'][0]  # Obtiene el nombre del campo (title/author/category)
        msg = error['msg']       # Obtiene el mensaje de error
        return f"Error en {field}: {msg}"  # Ej: "Error en author: Solo debe contener letras"
    
    # Si pasa la validación, procedemos con la base de datos
    try:
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # Validación adicional (aunque Pydantic ya lo hizo)
        if not title.strip() or not author.strip():
            return "El título y autor son obligatorios"

        # Normalizamos los datos
        title = title.lower()
        author = author.lower()
        category = category.lower()

        # Insertamos en la base de datos
        cursor.execute("""
            INSERT INTO books (title, author, category, link)
            VALUES (?, ?, ?, ?)
            """, (book.title, book.author, book.category, link))
        
        connect.commit()
        return 'Libro agregado correctamente'
    
    except sqlite3.IntegrityError:
        return "El libro ya existe en la base de datos"
    except Exception as e:
        print(f"Error inesperado: {e}")
        return f"Error al guardar el libro: {str(e)}"
    finally:
        if 'connect' in locals():
            connect.close()