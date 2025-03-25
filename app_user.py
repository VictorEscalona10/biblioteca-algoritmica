import flet as ft
from screens.user_profile import user_profile_page
from screens.add_book_user import add_book_user_page
from screens.home import home

def app(page: ft.Page):
    page.bgcolor = '#1d2126'
    page.title = f"Biblioteca {page.user_authenticated}"
    # Función para manejar el cambio de destino en el NavigationRail
    def on_navigation_change(e):
        # Limpia el contenido actual del body
        body_column.controls.clear()

        # Agrega el contenido correspondiente al índice seleccionado
        if e.control.selected_index == 0:
            body_column.controls.append(home(page))
        elif e.control.selected_index == 1:
            add_book_user_content = add_book_user_page(page, page.user_authenticated)  # Obtiene el contenido de add_book_user_page
            body_column.controls.append(add_book_user_content)  # Añade el contenido al body
        elif e.control.selected_index == 2:
            user_profile_content = user_profile_page(page, page.user_authenticated)
            body_column.controls.append(user_profile_content)

        # Actualiza la página
        page.update()

    # Función para manejar el clic en el FloatingActionButton
    def on_fab_click(e):
        # Simula el cambio de destino seleccionando el primer destino
        rail.selected_index = 0
        on_navigation_change(ft.ControlEvent(control=rail))

    # NavigationRail
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=56,
        min_extended_width=2160,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
                label="Home",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD,
                selected_icon=ft.icons.ADD,
                label="Agregar libro",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CONTACTS_OUTLINED,
                selected_icon=ft.icons.CONTACTS,
                label_content=ft.Text("Profile"),
            ),
        ],
        on_change=on_navigation_change,
    )

    # Columna para el body
    body_column = ft.Column(
        [
            home(page)
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
            expand=True,  # Ocupa todo el espacio disponible
        )
    )
    page.update()