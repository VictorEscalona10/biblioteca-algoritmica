import flet as ft
from login import login
from app_admin import app as app_admin
from app_user import app as app_user
from backend.register_front import register_page

#pipeline
def main(page: ft.Page):
    page.window_size = (1280, 720)
    page.window.alwais_on_top = True
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src="resources/images/P2210039.JPG" ,fit=ft.ImageFit.COVER, opacity=0.5))
    page.title = "Biblioteca"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.user_authenticated = None

    def route_change(e):
        page.clean()
        if page.route == "/":
            login(page)
        if page.route == "/segunda":
            if page.user_authenticated == 'admin':
                page.clean()
                app_admin(page)
            elif page.user_authenticated != 'admin':
                page.clean()
                app_user(page)
            else:
                page.clean()
                login(page)

        if page.route == "/registro":
            page.clean()
            register_page(page)

    page.on_route_change = route_change
    page.go("/")
        
ft.app(target=main)
