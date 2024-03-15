from libretto import Libretto
from voto import Voto

lib = Libretto()
v1 = Voto("Analisi 1", 10, 28, False, '2022-01-30')
lib.append(v1)
lib.append(Voto('Fisica 1', 10, 25, False, '2022-07-12'))
lib.append(Voto("Analisi 2", 8, 30, True, '2023-02-15'))

print(lib.findByPunti(25, False))

voto_analisi2 = lib.findByEsame("Analisi 2")
print(voto_analisi2.punteggio)
