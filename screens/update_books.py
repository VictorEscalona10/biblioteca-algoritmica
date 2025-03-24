import flet as ft
from backend.books.update_book import update_book as update_book_backend

def update_book_page(page: ft.Page):
    def update_book_function(e):
        title = title_input.value
        new_title = new_title_input.value
        new_author = new_author_input.value
        new_category = new_category_input.value
        link = link_input.value

        try:
            # Llama a la función de backend para actualizar el libro
            update_book_backend(
                title=title.value,
                new_title=new_title,
                new_author=new_author,
                new_category=new_category,
                link=link
            )
            # Muestra un mensaje de éxito
            page.snack_bar = ft.SnackBar(ft.Text("Libro actualizado correctamente"), bgcolor="green")
        except ValueError as e:
            # Muestra un mensaje de error
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {str(e)}"), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    # Título de la página
    title = ft.Text("Actualizar libro", size=20, weight="bold")

    # Campos de entrada
    title_input = ft.TextField(label="Título del libro", width=450)
    new_title_input = ft.TextField(label="Nuevo título", width=450)
    new_author_input = ft.TextField(label="Nuevo autor", width=450)
    new_category_input = ft.TextField(label="Nueva categoría", width=450)
    link_input = ft.TextField(label="Link", width=450)

    # Botón de actualización
    update_button = ft.ElevatedButton(
        text="Actualizar libro",
        on_click=update_book_function,
        bgcolor="#1d2126",
        color="white",
        width=150,
    )

    # Columna que contiene los controles
    column = ft.Column(
        controls=[
            title,
            title_input,
            new_title_input,
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