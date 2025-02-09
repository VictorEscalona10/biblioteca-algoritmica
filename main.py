import flet as ft
from login import login
from app import app
#pipeline
def main(page: ft.Page):
    page.bgcolor = '#0f1114'
    page.title = "Biblioteca"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(e):
        page.clean()
        if page.route == "/":
            login(page)
        if page.route == "/segunda":
            page.clean()
            app(page)

    page.on_route_change = route_change
    page.go("/")
        
ft.app(target=main)

