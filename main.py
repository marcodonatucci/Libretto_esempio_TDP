import flet as ft
from view import View
from Controller import Controller


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)  # il controllore lavora su un oggetto di tipo view
    v.setController(c)
    v.loadAll()


ft.app(target=main)
