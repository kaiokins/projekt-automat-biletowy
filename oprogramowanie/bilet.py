from tkinter import *
from oprogramowanie import przedmiot


class Bilety(przedmiot.Przedmiot):
    def __init__(self, nazwa, rodzaj, cena, ile):
        """
        Klasa Bilety jest odpowiedzialna za dodawanie nowych biletów (tworzenie kolejnych obiektów).
        Dziedziczy ona pola oraz metody po klasie przedmiot.
        :param nazwa: nazwa biletu
        :param rodzaj: rodaj biletu
        :param cena: cena biletu
        :param ile: ile sztuk danego biletu
        """
        przedmiot.Przedmiot.__init__(self, nazwa, rodzaj, cena, ile)
        self._podsumowanie = 0

    def zwrocNazwe(self):
        """Zwraca nazwę danego biletu"""
        return self._nazwa

    def zwrocRodzaj(self):
        """Zwraca rodzaj biletu"""
        return self._rodzaj

    def zwrocIlosc(self):
        """Zwraca ilość biletu"""
        return self._ile

    def zwrocCene(self):
        """Zwraca cenę biletu"""
        return self._cena

    def dodajIlosc(self):
        """Dodaje bilet"""
        self._ile += 1

    def dodajbilet(self, i):
        self._ile += 1

    def dodajbilet(self, i, rodzaj):
        """
        Metoda dodająca bilet.
        Wykorzystywana jest podczas dodawania biletu za pomocą przycisku.
        """
        self._ile += 1
        # Poniższe dwie linie kodu używane są do poprawnego wyświetlania danych w polu typu "input"
        # Podczas dodawania ilości biletów zamiast zmiany wartości np. z 1 na 2 wystąpiłoby doklejenie do poprzedniej wartości czyli "12".
        rodzaj.delete(0, END)
        rodzaj.insert(0, self._ile)

    def dodajBiletPole(self, i, typ, ilosc):
        """
        Metoda dodająca bilet. Wywoływana jest przy naciśnięciu przycisku "+" na interfejsie.
        Dzięki niej użytkownik może wprowadzić dowolną ilość biletów do pola typu "input",
        a następnie wysłać informację do obiektu o ilości wprowadzonych biletów.
        """
        if ilosc < 0:
            pass
        else:
            self._ile = ilosc
        typ.delete(0, END)
        typ.insert(0, self._ile)

    def jakiKoszt(self):
        """Zwraca koszt danego biletu."""
        return self._ile * self._cena
