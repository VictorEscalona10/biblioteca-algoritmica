import flet as ft
from backend.books import add_book
from backend.models.book import Book

def add_book_page(page: ft.Page):
    form_container = ft.Container()

    title = ft.TextField(label="Agregar Libro")
    

add_book_page()