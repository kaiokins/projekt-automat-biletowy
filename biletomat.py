from oprogramowanie import pieniadze as p
from tkinter import *
from oprogramowanie import bilet
from decimal import *
from wyjatki import wyjatki


class Biletomat(p.PrzechowywaczMonet):
    def __init__(self):
        super().__init__()
        self._depozyt = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0,
                         '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0}
        self._informacja = 0

    def dodajDoDepozytu(self, rodzaj, ile, typ):
        self._depozyt[rodzaj] = self._depozyt[rodzaj] + ile
        print("DEPO", self._depozyt[rodzaj])
        typ.delete(0, END)
        typ.insert(0, self._depozyt[rodzaj])

    def dodajDoPrzechowywacza(self, i):
        self._pieniadze[i] += self._depozyt[i]

    def dodajMonetePole(self, typ, rodzaj, ilosc):
        if ilosc < 0:
            pass
        else:
            self._depozyt[rodzaj] = ilosc
        typ.delete(0, END)
        typ.insert(0, self._depozyt[rodzaj])

    def sumaDepo(self):  # to potem bedzie mozna nadpisac, sprobowac, dac suma
        """Zwraca sumę monet w złotówkach"""
        suma = 0
        for key, value in self._depozyt.items():
            suma += int(key)*Decimal(value)
        return suma/100

    def wyciagWartosc(self, i):
        return self._depozyt[i]

    def wprowadzWartosc(self, i, wartosc):
        self._wartosc[i] = wartosc

    def zaplac(self, kwotaZakupu):
        if self.sumaDepo() > kwotaZakupu or self.sumaDepo() == kwotaZakupu:

            doWydania = self.sumaDepo() - kwotaZakupu

            if self.wydajReszte(doWydania) != -1:
                self._informacja = 1
                print("Dziekujemy za zakup")
                for i in self._pieniadze.keys():
                    self._pieniadze[i] = self._pieniadze[i] + self._depozyt[i]
                self.zapiszPlik()
                print("OSTATECZNIE: ", self._pieniadze)
            else:
                self._informacja = 2
                print("Tylko odliczona kwota, zwracam pieniądze")
        else:
            self._informacja = 3
            print("Wrzuciłeś za mało banknotów")

    def pobierzInformacje(self):
        return self._informacja

    def oddajMonety(self):
        return self._depozyt

    def wyczyscDepozyt(self):
        for key in self._depozyt.keys():
            self._depozyt[key] = 0
