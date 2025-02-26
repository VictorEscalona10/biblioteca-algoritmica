import sqlite3
from pydantic import ValidationError
from typing import Optional
import os

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.book import Book

# Ruta a la base de datos (ajusta según tu configuración)
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')

def update_book(title: str, new_title: Optional[str] = None, new_author: Optional[str] = None, new_category: Optional[str] = None, link: Optional[str] = None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Obtener el libro existente
    cursor.execute("SELECT title, author, category, link FROM books WHERE title = ?", (title,))
    existing_book = cursor.fetchone()

    if not existing_book:
        raise ValueError("El libro no existe en la base de datos.")

    # 2. Actualizar solo los campos proporcionados
    updated_title = new_title if new_title is not None else existing_book[0]
    updated_author = new_author if new_author is not None else existing_book[1]
    updated_category = new_category if new_category is not None else existing_book[2]
    update_link = link if link is not None else existing_book[3]

    # 3. Validar los datos con el modelo Pydantic
    try:
        book = Book(title=updated_title, author=updated_author, category=updated_category)
    except ValidationError as e:
        raise ValueError(f"Datos inválidos: {e}")

    # 4. Ejecutar la actualización en la base de datos
    cursor.execute("""
        UPDATE books
        SET title = ?, author = ?, category = ?, link = ?
        WHERE title = ?
    """, (book.title, book.author, book.category, update_link, title))

    conn.commit()
    conn.close()
    print("Libro actualizado correctamente.")

# Ejemplo de uso
""" update_book(
        title="El Principito",  # Título obligatorio (identificador único)
        new_author="Victor",  # Nuevo autor (opcional)
        new_category="Literatura Infantil"  # Nueva categoría (opcional)
    ) """
