import flet as ft
from backend.books.get_books import get_books

def user_profile_page(page: ft.Page):
    books = get_books()

    grid = ft.GridView(
        runs_count=5,  # Máximo 5 elementos por fila
        max_extent=200,  # Ancho máximo de cada elemento
        child_aspect_ratio=0.7,  # Relación alto/ancho
        spacing=10,  # Espacio entre elementos
        run_spacing=10,  # Espacio entre filas
    )

    for book in books:
        grid.controls.append(
            ft.Column(
                controls=[
                    ft.Container(
                        width=100,
                        height=150,
                        bgcolor=ft.colors.GREY,
                    ),
                    ft.Text(f"Libro: {book[1]}", size=16, weight="bold"),
                    ft.Text(f"Autor: {book[2]}", size=14),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5,
            )
        )
        
        
        

    return grid
