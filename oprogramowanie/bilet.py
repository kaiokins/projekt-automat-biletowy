from tkinter import *


class Bilety:
    def __init__(self, nazwa, rodzaj, cena, ile):
        self._nazwa = nazwa
        self._rodzaj = rodzaj
        self._cena = cena
        self._ile = ile

    def zwrocIlosc(self):
        return self._ile

    def zwrocCene(self):
        return self._cena

    def dodajIlosc(self):
        self._ile += 1

    def dodajbilet(self, i):
        self._ile += 1

    def dodajbilet(self, i, rodzaj):
        self._ile += 1
        rodzaj.delete(0, END)
        rodzaj.insert(0, self._ile)

    def dodajBiletPole(self, i, typ, ilosc):
        if ilosc < 0:
            pass
        else:
            self._ile = ilosc
        typ.delete(0, END)
        typ.insert(0, self._ile)
