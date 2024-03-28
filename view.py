from datetime import datetime
import flet as ft


# ci mettiamo tutti gli oggetti grafici


class View(object):

    def __init__(self, page: ft.Page):  # il view si riferisce a una pagina
        self._lvOut = None
        self._btnPrint = None
        self._btnAdd = None
        self._titolo = None
        self._btnCalendar = None
        self._datePicker = None
        self._ddVoto = None
        self._txtCFU = None
        self._txtIn = None
        self._controller = None
        self._page = page
        self._page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    def loadAll(self):
        self._titolo = ft.Text("Il mio libretto voti", color="blue", size=24,
                               text_align=ft.TextAlign.CENTER)
        # Row1
        self._txtIn = ft.TextField(label="Nome", width=300)
        self._txtCFU = ft.TextField(label="CFU", width=100)
        self._ddVoto = ft.Dropdown(label="Voto", width=100)
        self.fillDdVoto()
        self._datePicker = ft.DatePicker(first_date=datetime(2022, 11, 1),
                                         last_date=datetime(2025, 10, 31))

        self._btnCalendar = ft.ElevatedButton("Pick date", icon=ft.icons.CALENDAR_MONTH,
                                              on_click=lambda _: self._datePicker.pick_date())

        self._page.overlay.append(self._datePicker)

        row1 = ft.Row([self._txtIn, self._txtCFU, self._ddVoto, self._btnCalendar], alignment=ft.MainAxisAlignment.CENTER)

        # Row2
        self._btnAdd = ft.ElevatedButton(text="Add", on_click=self._controller.handleAdd)
        self._btnPrint = ft.ElevatedButton(text="Print", on_click=self._controller.handlePrint)

        row2 = ft.Row([self._btnAdd, self._btnPrint], alignment=ft.MainAxisAlignment.CENTER)

        # Row3
        self._lvOut = ft.ListView()

        self._page.add(self._titolo, row1, row2, self._lvOut)

    def setController(self, controller):
        self._controller = controller  # comunica con un controllore

    def fillDdVoto(self):
        for i in range(18, 31):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))

    @property
    def lvOut(self):
        return self._lvOut

    @property
    def page(self):
        return self._page

    @property
    def txtIn(self):
        return self._txtIn

    @property
    def txtCFU(self):
        return self._txtCFU

    @property
    def ddVoto(self):
        return self._ddVoto

    @property
    def datePicker(self):
        return self._datePicker
