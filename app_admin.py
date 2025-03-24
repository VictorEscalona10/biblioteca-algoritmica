import flet as ft
from screens.add_book import add_book_page
from screens.update_books import update_book_page
from screens.home_admin import home_admin

def app(page: ft.Page):
    page.bgcolor = '#1d2126'

    # Crea una columna para el contenido dinámico
    body_column = ft.Column(expand=True)

    # Función para manejar el cambio de destino en el NavigationRail
    def on_navigation_change(e):
        # Limpia el contenido actual del body
        body_column.controls.clear()

        # Agrega el contenido correspondiente al índice seleccionado
        if e.control.selected_index == 0:
            body_column.controls.append(home_admin(page))
        elif e.control.selected_index == 1:
            add_book_content = add_book_page(page)
            body_column.controls.append(add_book_content)
        elif e.control.selected_index == 2:
            update_book_content = update_book_page(page)
            body_column.controls.append(update_book_content)

        # Actualiza la página
        page.update()

    # NavigationRail
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=56,
        min_extended_width=2160,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Home",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ADD,
                selected_icon=ft.Icons.ADD,
                label="Agregar libro",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.ACCESSIBLE),
                selected_icon=ft.Icon(ft.Icons.ACCESSIBLE),
                label="Actualizar libro",
            ),
        ],
        on_change=on_navigation_change,
    )

    # Diseño de la página
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Container(
                    content=body_column,
                    expand=True,  # Asegura que el contenido del body ocupe el espacio restante
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            width=3840,
            height=2160,
        )
    )
    page.update()

