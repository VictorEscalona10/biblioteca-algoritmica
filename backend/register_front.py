import flet as ft
from register import register_user as register_backend

def register_page(page: ft.Page):

    def click(e):
        print('La funcion ha sido llamada')
        username = username_input.value
        email = email_input.value
        password = password_input.value
        repeat_password = repeat_password_input.value
        result = register_backend(username, email, password, repeat_password)
        if result.get('status') == True:
            print(result.get('message'))
            page.go('/')

    title = ft.Text("Registrarse" , size=25, text_align=ft.TextAlign.CENTER, color='#000000')
    username_input = ft.TextField(label="Nombre de usuario", width=300)
    email_input = ft.TextField(label="Correo electrónico", width=300)
    password_input = ft.TextField(label="Contraseña", width=300)
    repeat_password_input = ft.TextField(label="Repetir contraseña", width=300)
    button = ft.ElevatedButton("Registrarse", on_click=click, color='#ffffff', height=40, width=300, bgcolor='#1d2126', style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    

    column = ft.Column([
        title,
        username_input,
        email_input,
        password_input,
        repeat_password_input,
        button,
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    container = ft.Container(
        content=column,
        bgcolor='#ffffff',
        padding=50,
        border_radius=10,
        width=500,

        )
    page.add(container)


