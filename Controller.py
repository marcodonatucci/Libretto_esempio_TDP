from libretto import Libretto
from voto import Voto
import flet as ft
from view import View

# ci mettiamo tutti i metodi che lavorano con l'interfaccia grafica


class Controller(object):

    def __init__(self, view: View):  # con i due punti indichi di che tipo è l'oggetto
        self._view = view  # controller è l'unico che parla con il modello e si riferisce a una view
        self._model = Libretto()
        self.startupLibretto()

    def startupLibretto(self):
        self._model.append(Voto('Fisica 1', 10, 25, False, '2022-07-12'))
        self._model.append(Voto("Analisi 2", 8, 30, True, '2023-02-15'))

    def handleAdd(self, e):
        pass

    def handlePrint(self, e):
        outList = self._model.stampa()
        for elem in outList:
            self._view.lvOut.controls.append(ft.Text(elem))
        self._view.page.update()
