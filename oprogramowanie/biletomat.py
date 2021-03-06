from decimal import *
from tkinter import *

from oprogramowanie import pieniadze as p


class Biletomat(p.PrzechowywaczMonet):
    def __init__(self):
        """Klasa Biletomat odpowiedzialna jest za funkcjonalność biletomatu. Dziedziczy ona po klasie PrzechowywaczMonet"""

        super().__init__()

        # Słownik depozyt przechowuje monety, które zostały wrzucone przez użytkownika
        self._depozyt = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0}
        self._informacja = 0

    def dodajDoDepozytu(self, rodzaj, ile, typ):
        """
        Dodaje monete do depozytu wrzuconą przez użytkownika.
        Metoda używana jest w intefejsie przy przyciśnięciu guzika o danym nominale.
        """

        self._depozyt[rodzaj] = self._depozyt[rodzaj] + ile

        # Poniższe dwie linie kodu używane są do poprawnego wyświetlania danych w polu typu "input".
        # Podczas dodawania ilości nominałów zamiast zmiany wartości np. z 1 na 2 wystąpiłoby doklejenie do poprzedniej wartości czyli "12".
        typ.delete(0, END)
        typ.insert(0, self._depozyt[rodzaj])


    def dodajMonetePole(self, typ, rodzaj, ilosc):
        """
        Metoda dodająca monetę/banknot. Wywoływana jest przy naciśnięciu przycisku "+" na interfejsie.
        Dzięki niej użytkownik może wprowadzić dowolną ilość nominałów do pola typu "input",
        a następnie wysłać informację do obiektu o ilości.
        """

        # if ilosc < 0:
        #    pass
        # else:
        self._depozyt[rodzaj] = ilosc
        typ.delete(0, END)
        typ.insert(0, self._depozyt[rodzaj])

    def sumaDepo(self):
        """Zwraca sumę monet w złotówkach"""
        suma = 0
        for key, value in self._depozyt.items():
            suma += int(key) * Decimal(value)
        return suma / 100


    def zaplac(self, kwotaZakupu):
        """
        Metoda obsługi płatności. Sprawdzane jest czy użytkownik wrzucił wystarczającą ilość pieniędzy
        oraz czy transakcja się powiedzie czy nie.
        """

        # Sprawdzamy czy użytkownik wrzucił odpowiednią ilość monet. Jeśli wrzucił dokładnie tyle
        # lub więcej sprawdzane jest czy może wydać resztę.
        if self.sumaDepo() > kwotaZakupu or self.sumaDepo() == kwotaZakupu:

            # Obliczamy ile musimy wydać pieniędzy użytkownikowi
            doWydania = self.sumaDepo() - kwotaZakupu

            # Jeżeli funkcja reszta, zwróci wartość -1 to transakcja się powiedzie,
            # w przeciwnym wypadku zostaniemy poproszeni o wprowadzenie wyliczonej kwoty
            if self.reszta(doWydania) != -1:
                # Dziękujemy za zakup
                self._informacja = 1

                # Pieniądze zostają wrzucone z depozytu do przechowywacza monet
                # oraz zostaje wywołana funkcja zapiszPlik zapisująca stan przechowywacza w pliku.
                self._pieniadze = {i: self._pieniadze[i] + self._depozyt[i] for i in self._pieniadze.keys()}
                self.zapiszPlik()
            else:
                # Tylko odliczona kwota, zwracam pieniądze
                self._informacja = 2
        else:
            # Wrzuciłeś za mało banknotów
            self._informacja = 3


    def pobierzInformacje(self):
        """
        Zmienną informacja wykorzystuje się w interfejsie,
        która przekazuje jakie okienko po dokonaniu płatności pokazać
        """
        return self._informacja

    def oddajMonety(self):
        """Odpowiada za zwrócenie wrzuconych monet do depozytu"""
        return self._depozyt

    def wyczyscDepozyt(self):
        """Czyści depozyt z monet"""
        self._depozyt = {key: 0 for key in self._depozyt}
