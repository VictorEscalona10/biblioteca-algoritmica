import sqlite3
import os

def get_books_user(username):
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM users where user = ?", (username,))
        user = cursor.fetchone()
        user_id = user[0]
        cursor.execute("SELECT * FROM user_books where user_id = ?", (user_id,))
        books = cursor.fetchall()
        return books
    except Exception as e:
        print(e)
        return "Error al obtener los libros"
    
# print(get_books_user('victor'))