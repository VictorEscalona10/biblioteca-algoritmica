import flet as ft

def app(page: ft.Page):
    page.bgcolor = '#0f1114'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    button_addBook = ft.ElevatedButton('Agregar Libro')
    container_components_header = ft.Row([
        button_addBook
    ])
    header = ft.Container(content=ft.Row([container_components_header]), bgcolor='#ffffff')

    page.add(header)
    



    page.update()