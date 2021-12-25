import biletomat
from tkinter import *
from oprogramowanie import pieniadze as p
from oprogramowanie.bilet import Bilety
from wyjatki import wyjatki as w

biletomat = biletomat.Biletomat()
print(biletomat.suma())

bilet = [None for _ in range(6)]
bilet[0] = Bilety("20 minut", "ulgowy", 1.50)
bilet[1] = Bilety("40 minut", "ulgowy", 2.50)
bilet[2] = Bilety("60 minut", "ulgowy", 3)
bilet[3] = Bilety("20 minut", "normalny", 2.50)
bilet[4] = Bilety("40 minut", "normalny", 4.30)
bilet[5] = Bilety("60 minut", "normalny", 6)


def action2():
    print("Działa")


def otworzPlatnosci():
    # Okienka odpowiedzialne za platnosci
    root2 = Tk()
    root2.title("Zaplac za bilet")
    root2.geometry("600x650")
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

    root2.mainloop()


root = Tk()
root.title("Automat biletowy MPK")
root.geometry("600x400")

# Okienka odpowiedzialne za automat biletowy
label = Label(root, text="Proszę wybrać rodzaj biletu", font=30)
label.pack()

ulg20b = Button(root, text="20-minutowy ulgowy [1,50 zł]", command=action2)
ulg20i = Entry(root, width=5)
ulg20b.pack()
ulg20i.pack()

ulg40b = Button(root, text="40-minutowy ulgowy [2,50 zł]", command=action2)
ulg40i = Entry(root, width=5)
ulg40b.pack()
ulg40i.pack()

ulg60b = Button(root, text="60-minutowy ulgowy [3 zł]", command=action2)
ulg60i = Entry(root, width=5)
ulg60b.pack()
ulg60i.pack()

norm20b = Button(root, text="20-minutowy normalny [2,50 zł]", command=action2)
norm20i = Entry(root, width=5)
norm20b.pack()
norm20i.pack()

norm40b = Button(root, text="40-minutowy normalny [4,30 zł]", command=action2)
norm40i = Entry(root, width=5)
norm40b.pack()
norm40i.pack()

norm60b = Button(root, text="60-minutowy normalny [6 zł]", command=action2)
norm60i = Entry(root, width=5)
norm60b.pack()
norm60i.pack()

podsumowanie = Button(root, text="Podsumuj", command=otworzPlatnosci)
podsumowanie.pack()

root.mainloop()
