class Przedmiot:
    def __init__(self, nazwa, rodzaj, cena, ile):
        """
        Klasa przedmiot jest to ogólna klasa, po której inne klasy mogą dziedziczyć pola oraz metody. W tym programie po tej klasie dziedziczyła będzie klasa bilet
        :param nazwa: nazwa przedmiotu
        :param rodzaj: rodzaj przedmiotu
        :param cena: cena przedmiotu
        :param ile: ilosc przedmiotu
        """
        self._nazwa = nazwa
        self._rodzaj = rodzaj
        self._cena = cena
        self._ile = ile

    def zwrocNazwe(self):
        """Wyświetla nazwę przedmiotu"""
        print("Nazwa przedmiotu to: ", self._nazwa)

    def zwrocRodzaj(self):
        """"Wyświetla rodzaj przedmiotu"""
        print("Rodzaj przedmiotu to: ", self._rodzaj)

    def zwrocIlosc(self):
        """Wyświetla ilość przedmiotu"""
        print("Ilosc przedmiotu wynosi: ", self._ile)

    def zwrocCene(self):
        """Wyświetla cenę przedmiotu"""
        print("Cena przedmiotu wynosi: ", self._cena)
