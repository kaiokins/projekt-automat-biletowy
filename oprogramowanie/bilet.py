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
