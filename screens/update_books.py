import flet as ft
from backend.books.update_book import update_book as update_book_backend

def update_book_page(page: ft.Page):
    def update_book_function(e):
        title = title_input.value
        new_author = new_author_input.value
        new_category = new_category_input.value
        link = link_input.value

        msg.value = update_book_backend(
                title=title,
                new_author=new_author,
                new_category=new_category,
                link=link
                
        )
        page.update()

    # Título de la página
    title = ft.Text("Actualizar libro", size=20, weight="bold")

    # Campos de entrada
    title_input = ft.TextField(label="Título del libro", width=450)
    new_author_input = ft.TextField(label="Nuevo autor", width=450)
    new_category_input = ft.TextField(label="Nueva categoría", width=450)
    link_input = ft.TextField(label="Link", width=450)
    msg = ft.Text("" , size=12, color="green")

    # Botón de actualización
    update_button = ft.ElevatedButton(
        text="Actualizar",
        on_click=update_book_function,
        bgcolor="black",
        color="white",
        width=150,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )

    # Columna que contiene los controles
    column = ft.Column(
        controls=[
            title,
            msg,
            title_input,
            new_author_input,
            new_category_input,
            link_input,
            update_button,
            
        ],
        alignment=ft.MainAxisAlignment.START,  # Alinear al inicio
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
        spacing=20,  # Espacio entre controles
        scroll=ft.ScrollMode.AUTO,  # Habilitar scroll si es necesario
    )

    # Contenedor principal
    container = ft.Container(
        content=column,
        padding=20,
        alignment=ft.alignment.top_center,  # Alinear el contenido en la parte superior
        expand=True,  # Asegurar que el Container se expanda
    )

    return container