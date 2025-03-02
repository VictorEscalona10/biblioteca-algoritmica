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

    title = ft.Text("Registrarse")
    username_input = ft.TextField(label="Nombre de usuario")
    email_input = ft.TextField(label="Correo electrónico")
    password_input = ft.TextField(label="Contraseña")
    repeat_password_input = ft.TextField(label="Repetir contraseña")
    button = ft.ElevatedButton("Registrarse", on_click=click)

    column = ft.Column([
        title,
        username_input,
        email_input,
        password_input,
        repeat_password_input,
        button
    ])

    container = ft.Container(content=column)
    page.add(container)


