import flet as ft
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.books.add_book_user import add_book_to_user as add_book_user_backend

def add_book_user_page(page: ft.Page, user: str):

    def click(e):
        title_value = title_input.value
        error.value = add_book_user_backend(user, title_value)
        page.update()

    title = ft.Text("Agregar Libro", size=20, color=ft.colors.WHITE)
    
    title_input = ft.TextField(label="Titulo del libro", color=ft.colors.WHITE)
    button = ft.ElevatedButton("Agregar", on_click=click)
    error = ft.Text("",color=ft.colors.GREEN)

    column = ft.Column(
        [
            title,
            error,
            title_input,
            button
        ],
        alignment="center",  # Cambiado a cadena
        spacing=20
    )

    container = ft.Container(
        content=column,
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BLUE_700,
        alignment=ft.alignment.center  # Cambiado a ft.alignment.center
    )

    return container  # Devuelve el contenedor en lugar de agregarlo a la página
