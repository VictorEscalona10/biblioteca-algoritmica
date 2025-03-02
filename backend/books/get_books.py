import os 
import sqlite3

def get_books():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        return books
    except:
        return "Error al obtener los libros"
    
# print(get_books())

