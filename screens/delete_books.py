import flet as ft
from backend.books.delete_books import delete_book as delete_book_backend
from pydantic import ValidationError

def delete_books_page(page: ft.Page):
    def delete_books(e):
        title = del_title_input.value
        author = del_author_input.value
        category = del_category_input.value
        link = del_link_input.value

        try:
            result = delete_book_backend(title, author, category, link)
            error.value = result if result else "Libro eliminado correctamente"
            del_title_input.value = ''
            del_author_input.value = ''
            del_category_input.value = ''
            del_link_input.value = ''
        except ValidationError as e:
            error.value = e.errors()[0]["msg"]
        except Exception as e:
            error.value = str(e)

        page.update

        try:
            delete_book_backend(
                title=title,
                author=author,
                category=category,
                link=link
            )
            page.snack_bar = ft.SnackBar(ft.Text("Libro eliminado correctamente"), bgcolor="green")
        except ValueError as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {str(e)}"), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    
    title = ft.Text("Eliminar libro", size=20, weight="bold")
    error = ft.Text("", size=12, color="red")
    del_title_input = ft.TextField(label="Título del libro", width=450)
    del_author_input = ft.TextField(label="Autor del libro", width=450)
    del_category_input = ft.TextField(label="Categoría del libro", width=450)
    del_link_input = ft.TextField(label="Link", width=450)
    
    delete_button = ft.ElevatedButton(
        text="Eliminar",
        on_click=delete_books,
        bgcolor="#1d2126",
        color="white",
        width=150,
    )

    column = ft.Column(
        controls=[
            title,
            error,
            del_title_input,
            del_author_input,
            del_category_input,
            del_link_input,
            delete_button,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
    )

    container = ft.Container(
        content=column,
        padding=20,
        alignment=ft.alignment.top_center,
        expand=True,

    )

    return container