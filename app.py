import flet as ft

name = "NavigationRail Example"

def app(page: ft.Page):
    page.bgcolor='#1d2126'
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=56,
        min_extended_width=2160,
        leading=ft.FloatingActionButton(icon=ft.Icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="First",
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
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                [ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True
            ),
        ],
        alignment=ft.MainAxisAlignment.START,  # Asegura que la fila se alinee al inicio (izquierda)
        width=3840, #With se basa en pixeles al ancho
        height=2160, #height se basa en pixeles al alto
        #Usé resolución 4k porque es la menos usada en el mercado, y así no tenemos problemas con la responsividad (Creo que es una mala solución)
    ))
    page.update()