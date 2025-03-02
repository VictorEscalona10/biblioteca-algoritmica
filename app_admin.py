import flet as ft
from screens.add_book import add_book_page
from screens.update_books import update_book_page
from backend.books.get_books import get_books

def app(page: ft.Page):
    page.bgcolor = '#1d2126'

    # Función para manejar el cambio de destino en el NavigationRail
    def on_navigation_change(e):
        # Limpia el contenido actual del body
        body_column.controls.clear()

        # Agrega el contenido correspondiente al índice seleccionado
        if e.control.selected_index == 0:
            add_book_content = add_book_page(page)
            body_column.controls.append(add_book_content)  # Añade el contenido al body
        elif e.control.selected_index == 1:
            update_book_content = update_book_page(page)
            body_column.controls.append(update_book_content)
            print(update_book_content)
        elif e.control.selected_index == 2:
            body_column.controls.append(ft.Text("Contenido de la Pantalla de Configuración"))

        # Actualiza la página
        page.update()

    # NavigationRail
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=56,
        min_extended_width=2160,
        leading=ft.FloatingActionButton(icon=ft.Icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.ADD,
                selected_icon=ft.Icons.ADD,
                label="Agregar libro",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=on_navigation_change,  # Asigna la función de manejo de cambios
    )

    # Columna para el body
    books = get_books()

    body_column = ft.Column(
        [
            ft.Text(f"Libro: {book[1]}, Autor: {book[2]}") for book in books
        ],  # Contenido inicial
        alignment=ft.MainAxisAlignment.START,
        expand=True,
    )

    # Diseño de la página
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                body_column,  # Usa la columna del body
            ],
            alignment=ft.MainAxisAlignment.START,
            width=3840,
            height=2160,
        )
    )
    page.update()