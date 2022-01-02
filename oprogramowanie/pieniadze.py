import csv
import os
from pathlib import Path

class PrzechowywaczMonet:
    def wczytajPlik(self):
        """Metoda odpowiedzialna za wczytywanie z pliku .csv rodzajów oraz ilości monet/banknotów"""

        try:
            file = Path(__file__).with_name("pieniadze.csv")
            with open(file) as f:
                reader = csv.reader(f)
                for row in reader:
                    k, v = row
                    self._pieniadze[str(k)] = int(v)
        except:
            print("Wystąpił błąd przy wczytywaniu pliku")
        finally:
            f.close()

    def zapiszPlik(self):
        """Metoda odpowiedzialna za zapisywanie do pliku ilości monet/banknotów po poprawnym wykonaniu wszystkich operacji transakcyjnych"""

        try:
            file = Path(__file__).with_name("pieniadze.csv")
            with open(file, "w") as f:
                [f.write('{0},{1}\n'.format(key, value)) for key, value in self._pieniadze.items()]
        except:
            print("Wystąpił błąd przy zapisywaniu pliku")
        finally:
            f.close()

    def __init__(self):
        """
        Klasa PrzechowywaczMonet służy do przechowywania rodzajów oraz ilości monet/banknotów. Posiada metody odpowiedzialne za zapisanie oraz wczytanie monet/banknotów.
        """

        self._pieniadze = {}  # Pojemnik (w postaci słownika) służący do przechowywania monet/banknotów (rodzaj:ilość)
        # self._pieniadze = {'1': 55, '2': 55, '5': 55, '10': 55, '20': 55, '50': 55, '100': 55, '200': 55, '500': 55, '1000': 55, '2000': 55, '5000': 55}
        self.wczytajPlik()  # Wywołanie funkcji wczytującej monety/banknoty
        self._reszta = {} # Przechowuje resztę dla użytkownika

    def suma(self):
        """Zwraca sumę monet w złotówkach"""

        suma = 0
        for key, value in self._pieniadze.items():
            suma += int(key) * value
        return suma / 100

    def reszta(self, doWydania):
        """Metoda odpowiedzialna za obliczanie reszty"""

        # Na poczatku rozdzielam rodzaj oraz ilość na dwie zmienne
        moneta = list(self._pieniadze.keys())
        ilosc = list(self._pieniadze.values())

        # Odwracam słownik by wartości były segregowane od największej do najmniejszej.
        # Jeśli ktoś zakupi bilet za 6 złotych i zapłaci 50 złotową monetą do należy sprawdzić
        # w późniejszych etapach czy można mu wydać jak największymi nominałami.
        moneta.reverse()
        ilosc.reverse()

        doWydania = doWydania * 100
        reszta = [0] * 12

        # Pętla, która iteruje po ilości rodzajów monet/banknotów. Dopóki w przechowywaczu mamy dostępne nominały
        # lub możemy wydać to wydajemy w ten sposób resztę użytkownikowi. Dla przykładu użytkownik kupi 2 bilety
        # o sumie 12 złotych i zapłaci 50-złotówką to wydamy mu 20, 10, 5, 2, 1 zł reszty.
        for i in range(12):
            while not ((int(moneta[i])) > doWydania) and ilosc[i] > 0:
                doWydania -= int(moneta[i])
                ilosc[i] -= 1
                reszta[i] += 1

        moneta.reverse()
        ilosc.reverse()
        reszta.reverse()

        # Łączymy rodzaj oraz ilość nominałów za pomocą funkcji zip do słownika
        zostalo = dict(zip(moneta, ilosc))
        reszta = dict(zip(moneta, reszta))

        # Jeśli pieniadze uda się wydać to przypisujemy je do zmiennych (słowników), a w przeciwnym wypadku zwracamy -1
        if doWydania == 0:
            self._pieniadze = zostalo
            self._reszta = reszta
        else:
            return -1

    def zwrocReszte(self):
        """Zwrócenie reszty do użytkownika"""
        return self._reszta
