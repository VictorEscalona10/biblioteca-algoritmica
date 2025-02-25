import flet as ft
from backend.books.add_book import add_book as add_book_backend

def add_book_page(page: ft.Page):
    def add_book(e):
        title = title_input.value
        author = author_input.value
        category = category_input.value
        link = link_input.value
        result = add_book_backend(title, author, category, link)
        print(result)

    title_container = ft.Text("Agregar Libro")
    error = ft.Text("", color=ft.colors.RED)
    title_input = ft.TextField(label="Titulo del libro")
    author_input = ft.TextField(label="Autor del libro")
    link_input = ft.TextField(label="Link del libro (opcional)")
    category_input = ft.TextField(label="Categoria del libro")

    submit_button = ft.ElevatedButton("Agregar", on_click=add_book)

    column = ft.Column([
        title_container,
        error,
        title_input,
        author_input,
        link_input,
        category_input,
        submit_button
    ])

    container = ft.Container(content=column, padding=20, border=ft.border.all(1, ft.colors.BLACK))

    return container  # Devuelve el contenedor en lugar de añadirlo a la página