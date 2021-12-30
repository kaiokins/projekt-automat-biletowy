class Przedmiot:
    def __init__(self, nazwa, rodzaj, cena, ile):
        self._nazwa = nazwa
        self._rodzaj = rodzaj
        self._cena = cena
        self._ile = ile
        self._kolor = ''


    def zwrocNazwe(self):
        print("Nazwa przedmiotu to: ", self._nazwa)

    def zwrocRodzaj(self):
        print("Rodzaj przedmiotu to: ", self._rodzaj)

    def zwrocIlosc(self):
        print("Ilosc przedmiotu wynosi: ", self._ile)

    def zwrocCene(self):
        print("Cena przedmiotu wynosi: ", self._cena)
