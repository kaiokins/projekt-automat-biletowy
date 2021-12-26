from types import LambdaType
from decimal import *
import math
import biletomat
from tkinter import *
from oprogramowanie import pieniadze as p
from oprogramowanie.bilet import Bilety
from wyjatki import wyjatki as w

biletomat = biletomat.Biletomat()
print(biletomat.suma())

bilet = [None for _ in range(6)]
bilet[0] = Bilety("20 minut", "ulgowy", 1.50, 0)
bilet[1] = Bilety("40 minut", "ulgowy", 2.50, 0)
bilet[2] = Bilety("60 minut", "ulgowy", 3, 0)
bilet[3] = Bilety("20 minut", "normalny", 2.25, 0)
bilet[4] = Bilety("40 minut", "normalny", 4.40, 0)
bilet[5] = Bilety("60 minut", "normalny", 6, 0)


def action2():
    print("Działa")


def doZaplaty(i):
    if bilet[i].zwrocIlosc() == 0:
        pass
    elif bilet[i].zwrocIlosc() < 0:
        bilet[i].dodajbilet(i)
    else:
        print(round(bilet[i].zwrocIlosc()*bilet[i].zwrocCene(), 5))


def zwrocCene():
    suma = 0
    for i in range(len(bilet)):
        suma = suma + bilet[i].zwrocCene()*bilet[i].zwrocIlosc()
    return suma


def doZaplatyPole(i, ilosc):
    if bilet[i].zwrocIlosc() == 0:
        pass
    elif bilet[i].zwrocIlosc() < 0:
        bilet[i].dodajbilet(i)
    else:
        print(round(int(ulg20i.get())*bilet[i].zwrocCene(), 5))


def sprawdzLiczbe(zmienna):
    try:
        return int(zmienna.get())
    except:
        return 0

# window_status = 0


def otworzPlatnosci():
    # Okienka odpowiedzialne za platnosci
    root2 = Tk()
    # global window_status
    # if window_status == 0:
    root2.title("Zaplac za bilet")
    root2.geometry("600x700")
    label2 = Label(
        root2, text="Do zapłacenia: " + str(zwrocCene()) + " zł", font=30)
    label2.pack()
    label = Label(
        root2, text="Proszę wybrać monety/banknoty do zapłacenia", font=30)
    label.pack()

    gr1b = Button(root2, text="1 grosz", command=action2)
    gr1i = Entry(root2, width=5)
    gr1b.pack()
    gr1i.pack()

    gr2b = Button(root2, text="2 grosze", command=action2)
    gr2i = Entry(root2, width=5)
    gr2b.pack()
    gr2i.pack()

    gr5b = Button(root2, text="5 groszy", command=action2)
    gr5i = Entry(root2, width=5)
    gr5b.pack()
    gr5i.pack()

    gr10b = Button(root2, text="10 groszy", command=action2)
    gr10i = Entry(root2, width=5)
    gr10b.pack()
    gr10i.pack()

    gr20b = Button(root2, text="20 groszy", command=action2)
    gr20i = Entry(root2, width=5)
    gr20b.pack()
    gr20i.pack()

    gr50b = Button(root2, text="50 groszy", command=action2)
    gr50i = Entry(root2, width=5)
    gr50b.pack()
    gr50i.pack()

    zl1b = Button(root2, text="1 złoty", command=action2)
    zl1i = Entry(root2, width=5)
    zl1b.pack()
    zl1i.pack()

    zl2b = Button(root2, text="2 złote", command=action2)
    zl2i = Entry(root2, width=5)
    zl2b.pack()
    zl2i.pack()

    zl5b = Button(root2, text="5 złotych", command=action2)
    zl5i = Entry(root2, width=5)
    zl5b.pack()
    zl5i.pack()

    zl10b = Button(root2, text="10 złotych", command=action2)
    zl10i = Entry(root2, width=5)
    zl10b.pack()
    zl10i.pack()

    zl20b = Button(root2, text="20 złotych", command=action2)
    zl20i = Entry(root2, width=5)
    zl20b.pack()
    zl20i.pack()

    zl50b = Button(root2, text="50 złotych", command=action2)
    zl50i = Entry(root2, width=5)
    zl50b.pack()
    zl50i.pack()

    zaplac = Button(root2, text="Zapłać", command=action2)
    zaplac.pack()

    oblicz = Button(root2, text="Oblicz", command=action2)
    oblicz.pack()
    # window_status = 1
    # print("STATUS:", window_status)
    root2.mainloop()
    # else:
    # window_status = 0
    # root2.destroy()
    # print("STATUS:", window_status)
    # otworzPlatnosci()


root = Tk()
root.title("Automat biletowy MPK")
root.geometry("600x650")

# Okienka odpowiedzialne za automat biletowy
label = Label(root, text="Proszę wybrać rodzaj biletu", font=30)
label.pack()

ulg20b = Button(
    root, text="20-minutowy ulgowy [1,50 zł]", command=lambda: [bilet[0].dodajbilet(0, ulg20i), doZaplaty(0)])
wstawulg20b = Button(
    root, text="Dodaj z pola wpisania", command=lambda: [bilet[0].dodajBiletPole(0, ulg20i, sprawdzLiczbe(ulg20i)), doZaplatyPole(0, int(ulg20i.get()))])
ulg20i = Entry(root, width=5)
ulg20b.pack()
ulg20i.pack()
wstawulg20b.pack()

ulg40b = Button(
    root, text="40-minutowy ulgowy [2,50 zł]", command=lambda: [bilet[1].dodajbilet(1, ulg40i), doZaplaty(1)])
wstawulg40b = Button(
    root, text="Dodaj z pola wpisania", command=lambda: [bilet[1].dodajBiletPole(1, ulg40i, sprawdzLiczbe(ulg40i)), doZaplatyPole(1, int(ulg40i.get()))])
ulg40i = Entry(root, width=5)
ulg40b.pack()
ulg40i.pack()
wstawulg40b.pack()

ulg60b = Button(
    root, text="60-minutowy ulgowy [3 zł]", command=lambda: [bilet[2].dodajbilet(2, ulg60i), doZaplaty(2)])
wstawulg60b = Button(
    root, text="Dodaj z pola wpisania", command=lambda: [bilet[2].dodajBiletPole(2, ulg60i, sprawdzLiczbe(ulg60i)), doZaplatyPole(2, int(ulg60i.get()))])
ulg60i = Entry(root, width=5)
ulg60b.pack()
ulg60i.pack()
wstawulg60b.pack()

norm20b = Button(
    root, text="20-minutowy normalny [2,25 zł]", command=lambda: [bilet[3].dodajbilet(3, norm20i), doZaplaty(3)])
wstawnorm20b = Button(
    root, text="Dodaj z pola wpisania", command=lambda: [bilet[3].dodajBiletPole(3, norm20i, sprawdzLiczbe(norm20i)), doZaplatyPole(3, int(norm20i.get()))])
norm20i = Entry(root, width=5)
norm20b.pack()
norm20i.pack()
wstawnorm20b.pack()

norm40b = Button(
    root, text="40-minutowy normalny [4,40 zł]", command=lambda: [bilet[4].dodajbilet(4, norm40i), doZaplaty(4)])
wstawnorm40b = Button(
    root, text="Dodaj z pola wpisania", command=lambda: [bilet[4].dodajBiletPole(4, norm40i, sprawdzLiczbe(norm40i)), doZaplatyPole(4, int(norm40i.get()))])
norm40i = Entry(root, width=5)
norm40b.pack()
norm40i.pack()
wstawnorm40b.pack()

norm60b = Button(
    root, text="60-minutowy normalny [6 zł]", command=lambda: [bilet[5].dodajbilet(5, norm60i), doZaplaty(5)])
wstawnorm60b = Button(
    root, text="Dodaj z pola wpisania", command=lambda: [bilet[5].dodajBiletPole(5, norm60i, sprawdzLiczbe(norm60i)), doZaplatyPole(5, int(norm60i.get()))])
norm60i = Entry(root, width=5)
norm60b.pack()
norm60i.pack()
wstawnorm60b.pack()

podsumowanie = Button(root, text="Podsumuj",
                      command=lambda: [otworzPlatnosci()])
podsumowanie.pack()

root.mainloop()
