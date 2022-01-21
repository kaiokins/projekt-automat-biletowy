import unittest
import interfejs as i
from decimal import *
from tkinter import *
from oprogramowanie import biletomat

class Testy(unittest.TestCase):
    def test_1(self):
        root = Tk()
        zl5i = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = i.Bilety("60 minutowy", "ulgowy", Decimal('1.50'), 10)
        b.dodajDoDepozytu('500', 1, zl5i)
        b.dodajDoDepozytu('1000', 1, zl5i)
        b.zaplac(bilet.zwrocCene())
        self.assertTrue(b.czyZostalaReszta() != 0)

    def test_2(self):
        root = Tk()
        zl5i = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = i.Bilety("60 minutowy", "ulgowy", Decimal('3'), 1)
        b.dodajDoDepozytu('1000', 1, zl5i)
        b.zaplac(bilet.zwrocCene())
        self.assertTrue(b.czyZostalaReszta() == 1)

    def test_dodatkowy(self):
        # gdy użytkownik wrzuci za małą ilość banknotów zostanie pobrana informacja nr 3,
        # czyli wyskoczy okienko o tym, że nie wrzucił wystarczającej liczby
        root = Tk()
        zl5i = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = i.Bilety("60 minutowy", "ulgowy", Decimal('3'), 1)
        b.dodajDoDepozytu('1', 200, zl5i)
        b.zaplac(bilet.zwrocCene())
        self.assertTrue(b.pobierzInformacje() == 3)


    def test_6(self):
        root = Tk()
        zl5i = Entry(root, width=5)
        b = biletomat.Biletomat()
        bilet = i.Bilety("60 minutowy", "ulgowy", Decimal('1.50'), 10)
        b.dodajDoDepozytu('500', 1, zl5i)
        b.dodajDoDepozytu('1000', 1, zl5i)
        bilet = i.Bilety("60 minutowy", "ulgowy", Decimal('1.50'), 1)
        b.dodajDoDepozytu('100', 1, zl5i)
        b.dodajDoDepozytu('50', 1, zl5i)
        b.zaplac(bilet.zwrocCene())
        self.assertTrue(b.czyZostalaReszta() != 0)

    def test_7(self):
        root = Tk()
        zl5i = Entry(root, width=5)
        zl5i.insert(END, -3)
        blad_platnosci = Label(root, text="", font=30)
        b = biletomat.Biletomat()
        bilet = i.Bilety("60 minutowy", "ulgowy", Decimal('1.50'), 10)
        self.assertTrue(i.sprawdzLiczbe(zl5i, blad_platnosci) == 0)
        b.zaplac(bilet.zwrocCene())

if __name__ == "__main__":
     unittest.main();