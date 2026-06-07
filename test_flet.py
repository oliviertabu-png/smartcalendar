import flet as ft

def main(page):
    page.title = "Test"
    page.add(ft.Text("Bonjour SmartCalendar"))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)