from oprogramowanie import pieniadze as p
from tkinter import *
from oprogramowanie import bilet


class Biletomat(p.PrzechowywaczMonet):
    def __init__(self):
        super().__init__()
        self._depozyt = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0,
                         '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0}

    def dodajDoDepozytu(self, rodzaj, ile, typ):
        self._depozyt[rodzaj] = self._depozyt[rodzaj] + ile
        print("DEPO", self._depozyt[rodzaj])
        typ.delete(0, END)
        typ.insert(0, self._depozyt[rodzaj])

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
            suma += int(key)*value
        return suma/100

    def wyciagWartosc(self, i):
        return self._depozyt[i]

    def wprowadzWartosc(self, i, wartosc):
        self._wartosc[i] = wartosc

    def zaplac(self, function):
        if self.sumaDepo() == function:
            print('TYLE SAMO')
        else:
            print('NIE TYLE SAMO')
