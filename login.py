import flet as ft

def login(page: ft.Page):

    def click(e):
        
        print(user.value, password.value)
        page.go("/segunda")

    title = ft.Text("Iniciar sesion", size=25, text_align=ft.TextAlign.CENTER, color='#000000')
    user = ft.TextField(label="Usuario", width=300)
    password = ft.TextField(label="Contraseña ", width=300)
    login = ft.ElevatedButton(
        "Iniciar Sesión", 
        color='#ffffff',
        height=40,
        width=300,
        bgcolor='#1d2126', 
        on_click=click, 
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            
        )
    )
    text_register = ft.Row(
        [
            ft.Text("¿No tienes cuenta?", size=20, color='#000000'),
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
        bgcolor='#ffffff',
        border_radius=10,
        padding=50,
        width=500,
    ))