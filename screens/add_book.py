import flet as ft
from backend.books.add_book import add_book as add_book_backend

def add_book_page(page: ft.Page):
    def add_book(e):
        title = title_input.value
        author = author_input.value
        category = category_input.value
        link = link_input.value
        result = add_book_backend(title, author, category, link)
        print(result)


        try:
            # Llama a la función de backend para actualizar el libro
            add_book_backend(
                title=title,
                author=author,
                category=category,
                link=link
            )
            # Muestra un mensaje de éxito
            page.snack_bar = ft.SnackBar(ft.Text("Libro agredado correctamente"), bgcolor="green")
        except ValueError as e:
            # Muestra un mensaje de error
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {str(e)}"), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    # Título de la página
    title = ft.Text("Agregar libro", size=20, weight="bold")

    # Campos de entrada
    title_input = ft.TextField(label="Nuevo título", width=450)
    author_input = ft.TextField(label="Nuevo autor", width=450)
    category_input = ft.TextField(label="Nueva categoría", width=450)
    link_input = ft.TextField(label="Link", width=450)

    # Botón de actualización
    update_button = ft.ElevatedButton(
        text="Agregar",
        on_click=add_book,
        bgcolor="#1d2126",
        color="white",
        width=150,
    )

    # Columna que contiene los controles
    column = ft.Column(
        controls=[
            title,
            title_input,
            author_input,
            category_input,
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
