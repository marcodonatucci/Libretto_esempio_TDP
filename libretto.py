"""
Gestione libretto universitario con la classe voto che rappresenta un esame e una classe libretto che contiene i voti
"""
from dataclasses import dataclass

'''
class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.esame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data
        # tutti gli attributi della classe in python sono PUBLIC

        if self.lode and self.punteggio != 30:
            raise ValueError("Lode non applicabile")  # posso lanciare un messaggio quando scateno l'eccezione
            # raise sarebbe throws di java

    def __str__(self):
        # metodi DUNDER (double under score) sono i metodi speciali delle classi
        return f"Esame {self.esame} superato con {self.punteggio}"

    # la fString è la stringa formattata, puoi inserire valori con le parentesi graffe

    def __repr__(self):
        # rappresentazione dell'oggetto utile al programmatore, la stampa è uguale a una chiamata del costruttore
        # tipo Car(model = audi...)
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"
'''


class Libretto:

    def __init__(self):
        self._voti = []  # il _ rende l'attributo voti protetto, se ne metti __ diventa privato ed è difficile da usare

    def append(self, voto):  # delegation, un metodo delega il suo lavoro a un metodo builtin
        self._voti.append(voto)

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        # costruisco una lista trasformando gli element di una lista esistente !
        return sum(punteggi) / len(punteggi)

    def findByPunti(self, punteggio, lode):
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)
        return corsi

    def findByEsame(self, esame):
        """
        Ricerca l'esame nel libretto con lo stesso nome
        :param esame:  dell'esame da cercare
        :return: oggetto voto con il nome cercato
        """
        for v in self._voti:  # questo commento qua sopra è la documentazione del metodo (sintassi param e return)!!
            if v.esame == esame:
                return v

    def stampa(self):
        outList = []
        outList.append(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            outList.append(v)
        outList.append(f"La media vale {self.media()}")
        return outList
'''
@dataclass  # è un decoratore, trasforma la classe, costruisce da solo i metodi di base che la definiscono 
class Voto:
    esame: str  # gli attributi vengono specificati in questo modo
    cfu: int
    punteggio: int
    lode: bool
    data: str
    
    # i metodi che vuoi definirti da solo o come vuoi li scrivi, guarda la documentazione per personalizzare
'''
'''
voto_1 = Voto("Analisi Matematica 1", 10, 28, False, "2022-02-10")
# la data in anno-mese-giorno conviene in informatica perché se la metti in ordine alfabetico ti viene anche in ordine!
voto_2 = Voto("Basi di dati", 8, 30, True, "2023-06-15")
print(voto_1, voto_2)  # si stampa da solo se definisci il __str__
# print(voto_1.__str__())

print(voto_1.__repr__())  # se definisco un repr e non definisco str usa il repr, sennò usa sempre str
miei_voti = [voto_1, voto_2]  # nella lista viene usato il repr (il repr stampa la rappresentazione dei riferimenti?)
print(miei_voti)

mio_libretto = Libretto()
mio_libretto.append(voto_1)
mio_libretto.append(voto_2)

print(mio_libretto.media())
'''
# puoi usare un metodo @property con il nome della variabile privata, è un getter
# poi puoi definire un metodo @name.setter anche per modificare l'attributo privato (deve essere definito il setter)
# __eq__ è un metodo equals, lo chiami con ==
# __lt__ è un compareTo, lo chiami con gli operatori < > <= >= !=
# i metodi dunder ridefiniscono le operazioni predefiniti sugli oggetti della classe
# @dataclasses.dataclass(order=True) implementa l'ordinamento in base ai parametri della classe
# se non vuoi includere un parametro nei criteri di ordinamento lo scrivi nel init parametro = field(compare=False)
# nel sort posso usare il parametro key = metodo cioè una chiave che usa una funzione:
# questa funzione prende un oggetto ed estrae un campo sulla base di cui vuoi ordinare (attribute getter):
# sort(key = operator.attrgetter('nome attributo'))
# puoi anche usare key = lambda valore: funzione, cioè una funzione usa e getta


