import sqlite3
import os

def add_book(title, author, link = ''):
    try:
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        if title == '' or author == '':
            return False

        cursor.execute("""
            INSERT INTO books (title, author, link)
                VALUES (?, ?, ?)
            """, (title, author, link))
        
        connect.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connect.close()

# probar la funcion
# add_book('El libro de mari', 'mari')
        