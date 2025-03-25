import flet as ft

def home(page: ft.Page):
    page.window_size = (1280, 720)
    title = ft.Text("Bienvenido a la Biblioteca", size=60, weight="bold", color="white")
    text = ft.Text("Seleccione una opción del menú", size=25, color="white")

    container = ft.Container(
        content=ft.Column(
            [title, text],
            alignment=ft.MainAxisAlignment.CENTER, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        ),
        alignment=ft.alignment.center, 
        expand=True,
        bgcolor=ft.colors.BLUE_700,
        border_radius=10,
    )

    return container
