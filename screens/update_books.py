import flet as ft

def update_book_page(page: ft.Page):
    def update_book_function(e):
        new_title = new_title_input.value
        new_author = new_author_input.value
        new_category = new_category_input.value
        link = link_input.value

        try:
            # Llama a la función de backend para actualizar el libro
            update_book_backend(
                title=title.value,  # Asegúrate de que `title` esté definido
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
            new_title_input,
            new_author_input,
            new_category_input,
            link_input,
            update_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
        spacing=20,  # Espacio entre controles
    )

    # Contenedor principal
    container = ft.Container(
        content=column,
        padding=20,
        alignment=ft.alignment.center,  # Centrar el contenido dentro del Container
        expand=True,  # Asegurar que el Container se expanda
    )

    return container