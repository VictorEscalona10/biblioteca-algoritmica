import flet as ft

def user_profile_page(page: ft.Page):
    # Botón para regresar a la página anterior
    back_button = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        on_click=lambda e: page.go('/segunda'),  # Simular navegación
        tooltip="Regresar",
    )

    # Espacio para la foto de perfil (usamos un círculo como placeholder)
    profile_picture = ft.CircleAvatar(
        radius=50,  # Tamaño del círculo
        foreground_image_src="https://via.placeholder.com/150",  # URL de una imagen de placeholder
    )

    # Texto "User Profile" debajo de la foto
    user_profile_text = ft.Text("User Profile", size=20, text_align=ft.TextAlign.CENTER)

    # Contenedores para los libros (más grandes verticalmente y con colores más oscuros)
    book1_container = ft.Container(
        content=ft.Text("Book 1", size=18, color=ft.colors.WHITE),
        padding=20,
        height=150,  # Altura del contenedor
        border_radius=10,
        bgcolor=ft.colors.BLUE_700,  # Color más oscuro
        alignment=ft.alignment.center,  
    )

    book2_container = ft.Container(
        content=ft.Text("Book 2", size=18, color=ft.colors.WHITE),
        padding=20,
        height=150,  # Altura del contenedor
        border_radius=10,
        bgcolor=ft.colors.GREEN_700,  # Color más oscuro
        alignment=ft.alignment.center,
    )

    # Fila para los libros (centrada)
    book_row = ft.Row(
        [book1_container, book2_container],
        alignment=ft.MainAxisAlignment.CENTER,  # Centra los libros
        spacing=20  # Espacio entre los contenedores de los libros
    )

    # Línea divisora
    divider = ft.Divider(height=1, thickness=1, color=ft.colors.GREY_400)

    # Columna principal para organizar el contenido (todo centrado)
    main_content = ft.Column(
        [
            # Foto de perfil y texto centrados
            ft.Column(
                [
                    profile_picture,  # Foto de perfil
                    user_profile_text,  # Texto "User Profile"
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra horizontalmente
                alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente
            ),
            divider,  # Línea divisora
            # Libros centrados
            book_row,
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centra todo verticalmente
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra todo horizontalmente
        expand=True,  # Ocupa todo el espacio disponible
    )

    # Usar un Stack para superponer la flecha de regresar
    stack = ft.Stack(
        [
            main_content,  # Contenido principal (centrado)
            ft.Row(
                [back_button],
                alignment=ft.MainAxisAlignment.START,  # Flecha en la esquina superior izquierda
            ),
        ],
        expand=True,  # Ocupa todo el espacio disponible
    )

    # Añadir el contenido a la página
    return stack
