from tkinter import *


class Bilety:
    def __init__(self, nazwa, rodzaj, cena, ile):
        self._nazwa = nazwa
        self._rodzaj = rodzaj
        self._cena = cena
        self._ile = ile

    def zwrocIlosc(self):
        return self._ile

    def dodajIlosc(self):
        self._ile += 1

    def dodajbilet(self, i, rodzaj):
        self._ile += 1
        rodzaj.delete(0, END)
        rodzaj.insert(0, self._ile)
