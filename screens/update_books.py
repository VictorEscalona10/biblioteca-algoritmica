import flet as ft
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.books.update_book import update_book as update_book_backend
def main(page: ft.Page):
    page.title = "Update Books"


    def update_book(e):
        new_title = title_input.value
        new_author = author_input.value
        new_category = category_input.value
        link = link_input.value
        update_books = update_book_backend(new_title, new_author, new_category, link)
        print(update_books)

    title_input = ft.TextField(label="New Title", width=450)
    author_input = ft.TextField(label="New Author", width=450)
    category_input = ft.TextField(label="New Category", width=450)
    link_input = ft.TextField(label="New Link", width=450)
    update_button = ft.ElevatedButton(
        text="Update Book",
        on_click=update_book,
        color='#ffffff',
        height=56,
        width=150,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2)
        ))
    column = ft.Column (
       
        [
            title_input,
            author_input,
            category_input,
            link_input,
            update_button,
        ],

        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        
    )

    container = ft.Container (
        content=column,
        bgcolor='#000000',
        border_radius=10,
        padding=50,
        width=800,
        height=505,
    )
    centered_container = ft.Container(
        content=container,
        alignment=ft.alignment.center,
        expand=True,
    )

    page.add(centered_container)

ft.app(target=main)