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

