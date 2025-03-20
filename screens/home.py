import flet as ft

def home(page: ft.Page):
    page.window_size = (1280, 720)
    title = ft.Text("Bienvenido a la Biblioteca", size=34, weight="bold")
    page.add(title)
    page.add(ft.Text("Seleccione una opción del menú", size=15))
ft.app(target=home)

