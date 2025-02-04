import flet as ft

def main(page: ft.Page):
    page.title = "Mi aplicación con Flet"
    page.bgcolor = ft.colors.BLUE_GREY_900

    def click(e):
        print("Click!")

    button = ft.ElevatedButton("Click me",  on_click=click)
    page.add(button)
    

ft.app(target=main)