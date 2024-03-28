from libretto import Libretto
from voto import Voto
import flet as ft
from view import View
import datetime


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
        nomeEsame = self._view.txtIn.value
        if nomeEsame == "":
            self._view.lvOut.controls.append(ft.Text("Il campo nome non può essere vuoto", color="red"))
            self._view.page.update()
            return
        cfu = self._view.txtCFU.value
        try:
            intCFU = int(cfu)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Il campo CFU deve essere un intero", color="red"))
            self._view.page.update()
            return
        punteggio = self._view.ddVoto.value
        if punteggio is None:
            self._view.lvOut.controls.append(ft.Text("Il campo punteggio va selezionato", color="red"))
            self._view.page.update()
            return
        if punteggio == "30L":
            punteggio = 30
            lode = True
        else:
            punteggio = int(punteggio)
            lode = False
        data = self._view.datePicker.value
        if data is None:
            self._view.lvOut.controls.append(ft.Text("Seleziona la data", color="red"))
            self._view.page.update()
            return
        self._model.append(Voto(nomeEsame, intCFU, punteggio, lode, f"{data.year}-{data.month}-{data.day}"))
        self._view.lvOut.controls.append(ft.Text("Voto correttamente aggiunto", color="green"))
        self._view.page.update()

    def handlePrint(self, e):
        outList = self._model.stampa()
        for elem in outList:
            self._view.lvOut.controls.append(ft.Text(elem))
        self._view.page.update()
