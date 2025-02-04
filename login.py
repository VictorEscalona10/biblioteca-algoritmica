import flet as ft

def login(page: ft.Page):

    def click(e):
        print(user.value, password.value)
        page.go("/segunda")

    title = ft.Text("Iniciar sesion", size=25, text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
    user = ft.TextField(label="Usuario", width=300)
    password = ft.TextField(label="Contraseña ", width=300)
    login = ft.ElevatedButton(
        "Iniciar Sesión", 
        color='#d3c4be', 
        bgcolor='#00264d', 
        on_click=click, 
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            
        )
    )
    text_register = ft.Row(
        [
            ft.Text("¿No tienes cuenta?", size=20, color=ft.colors.WHITE),
            ft.TextButton("Regístrate", on_click=click)
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar horizontalmente
        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar verticalmente
    )

    column = ft.Column(
        [
            title,
            user,
            password,
            login,
            text_register,
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
    )

    

    page.add(ft.Container(
        content=column,
        bgcolor='#003f80',
        border_radius=20,
        padding=20,
        width=400,
    ))