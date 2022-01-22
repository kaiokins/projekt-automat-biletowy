import unittest
import interfejs as i
from decimal import *
from tkinter import *
from oprogramowanie import biletomat

class Testy(unittest.TestCase):
    def test_1(self):
        """Bilet kupiony za odliczoną kwotę - oczekiwany brak reszty"""
        root = Tk()
        input = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = []
        bilet.append(i.Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 10))
        b.dodajDoDepozytu('500', 1, input)
        b.dodajDoDepozytu('1000', 1, input)
        b.zaplac(i.zwrocCene(bilet))
        self.assertTrue(b.czyZostalaReszta() == 0)

    def test_2(self):
        """Bilet kupiony płacąc więcej - oczekiwana reszta"""
        root = Tk()
        input = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = []
        bilet.append(i.Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 10))
        b.dodajDoDepozytu('500', 1, input)
        b.dodajDoDepozytu('1000', 5, input)
        b.zaplac(i.zwrocCene(bilet))
        self.assertTrue(b.czyZostalaReszta() == 1)

    def test_4(self):
        """
        Zakup biletu płacąc po 1gr - suma stu monet 1gr ma być równa 1 zł (dla floatów suma
        sto razy 0.01+0.01+...+0.01 nie będzie równa 1.0). Płatności można okonać za pomocą pętli
        for w interpreterze.
        """
        root = Tk()
        input = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = []
        bilet.append(i.Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 1))
        b.dodajDoDepozytu('1', 150, input)
        self.assertEqual(i.zwrocCene(bilet), 1.50)
        b.zaplac(i.zwrocCene(bilet))
        self.assertTrue(b.czyZostalaReszta() == 0)

    def test_5(self):
        """Zakup dwóch różnych biletów naraz - cena powinna być sumą"""
        bilet = []
        bilet.append(i.Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 1))
        bilet.append(i.Bilety("60 minutowy", "normalny", Decimal('6'), 1))
        self.assertEqual(i.zwrocCene(bilet), 7.50)

    def test_6(self):
        """
        Dodanie biletu, wrzucenie kilku monet, dodanie drugiego biletu, wrzucenie
        pozostałych monet, zakup za odliczoną kwotę - oczekiwany brak reszty
        (wrzucone monety nie zerują się po dodaniu biletu).
        """
        root = Tk()
        input = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = []
        bilet.append(i.Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 10))
        b.dodajDoDepozytu('500', 1, input)
        b.dodajDoDepozytu('1000', 1, input)
        bilet.append(i.Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 1))
        b.dodajDoDepozytu('100', 1, input)
        b.dodajDoDepozytu('50', 1, input)
        self.assertEqual(i.zwrocCene(bilet), 16.50)
        b.zaplac(i.zwrocCene(bilet))
        self.assertTrue(b.czyZostalaReszta() == 0)

    def test_7(self):
        "Próba wrzucenia ujemnej oraz niecałkowitej liczby monet (oczekiwany komunikat o błędzie)."
        root = Tk()
        input = Entry(root, width=5)
        input.insert(END, -3)
        blad_platnosci = Label(root, text="", font=30)
        self.assertTrue(i.sprawdzLiczbe(input, blad_platnosci) == 0)

    def test_dodatkowy(self):
        """Użytkownik wrzucił za małą ilość banknotów (oczekiwany komunikat o błędzie)"""
        root = Tk()
        input = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = i.Bilety("60 minutowy", "ulgowy", Decimal('3'), 1)
        b.dodajDoDepozytu('1', 200, input)
        b.zaplac(bilet.zwrocCene())
        self.assertTrue(b.pobierzInformacje() == 3)

if __name__ == "__main__":
     unittest.main();