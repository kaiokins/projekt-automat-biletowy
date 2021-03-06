import math
from datetime import datetime
from decimal import *
from functools import wraps
from tkinter import *

from oprogramowanie import biletomat
from oprogramowanie.bilet import Bilety
from wyjatki import wyjatki as w

def generujLiczby(x):
    """Funkcja to generator służąca do generowania określonej ilości liczb"""
    i = 0
    while i < x:
        yield i
        i += 1

tekstGuzikaDodaj = "+"
(lambda tekstGuzikaDodaj: print(tekstGuzikaDodaj))

def ktoraGodzina(func):
    now = datetime.now()
    @wraps(func)
    def wrapper(tekst):
        tekst['text'] = "Aktualna godzina to " + now.strftime("%H:%M") + "\n" + func(tekst)
    return wrapper

@ktoraGodzina
def powitaj(tekst):
    """Funkcja wyświetla prośbę o wybór biletu oraz aktualną godzinę (funkcja opakowna)"""
    return "Proszę wybrać rodzaj biletu"


def zwrocCene(listaBiletow):
    """Funkcja zwraca cenę biletów wybranych przez użytkownika (sumuje)"""
    suma = 0
    for i in range(len(listaBiletow)):
        suma = suma + listaBiletow[i].zwrocCene() * listaBiletow[i].zwrocIlosc()
    return suma



def kosztZakupow(etykieta):
    """Funkcja pokazuje ile użytkownik musi zapłacić"""
    etykieta['text'] = "Do zapłacenia: " + str(zwrocCene(bilet)) + " zł"


def informacjaZakupowa(zamknijOknoBiletow, zamknijOknoPlatnosci):
    """
    Funkcja odpowiedzialna za otwieranie okna po kliknięciu przycisku zapłać.
    Wyświetla informację na temat zakupów.
    """

    def zamknijOkno():
        """Zamyka okno biletów oraz płatności po naciśnięciu przycisku zapłać"""
        zamknijOknoBiletow.destroy()
        zamknijOknoPlatnosci.destroy()

    oknoZakupowe = Tk()

    oknoZakupowe.title("Zaplac za bilet")
    oknoZakupowe.geometry("600x300")

    czyKupil = Label(oknoZakupowe, text="", font=30)
    jakieBiletyZakupil = Label(oknoZakupowe, font=15)

    czyKupil.pack()
    jakieBiletyZakupil.pack()

    if biletomat.pobierzInformacje() == 1:
        # Wyświetla podsumowanie zakupów. Ile biletów danego rodzaju użytkownik zakupił oraz ile zwrócono mu reszty

        czyKupil['text'] = "Dziękujemy za zakup biletów. Zakupiłeś:"
        info = ''
        for i in range(6):
            if bilet[i].zwrocIlosc() > 0:
                info += "Bilet " + bilet[i].zwrocNazwe() + " " + bilet[i].zwrocRodzaj() + " w ilości sztuk: " + str(bilet[i].zwrocIlosc()) + "\n"

        if biletomat.czyZostalaReszta() == 1:
            biletomat.zwrocReszte()
            jakieBiletyZakupil['text'] = info + "\n Wydano " + str(biletomat.sumaDepo() - zwrocCene(bilet)) + " zł reszty"
            jakieBiletyZakupil.pack()
        else:
            jakieBiletyZakupil['text'] = info
            jakieBiletyZakupil.pack()

        zamknijOkno()
    elif biletomat.pobierzInformacje() == 2:
        # W przypadku gdy automat nie może wydać reszty informuje użytkownika oraz zostają mu zwrócone pieniądze

        jakieBiletyZakupil['text'] = "Tylko odliczona kwota. Zwracam " + str(biletomat.sumaDepo()) + " zł reszty"
        jakieBiletyZakupil.pack()

        biletomat.oddajMonety()
        biletomat.wyczyscDepozyt()

        zamknijOkno()
    elif biletomat.pobierzInformacje() == 3:
        # Gdy klient wrzuci za mało banknotów to zostanie o tym poinformowany.
        # Wyświetli się informacje ile jeszcze należy wrzucić.

        jakieBiletyZakupil['text'] = "Wrzuciłeś za mało banknotów. Brakuje " + str(math.fabs(biletomat.sumaDepo() - zwrocCene(bilet))) + " zł"
    else:
        jakieBiletyZakupil['text'] = "Upsss... coś poszło źle"
        jakieBiletyZakupil.pack()

        zamknijOkno()

    oknoZakupowe.mainloop()

def sprawdzLiczbe(zmienna, blad):
    """
    Funkcja odpowiedzialna za sprawdzenie, czy użytkownik podał odpowiednią
    liczbę przy wprowadzaniu liczby biletów lub nominałów.
    """

    # Gdy podana zostanie wartośc mniejsza od zera zostanie wyświetlony błąd w konsoli
    # dla administratora (użycie klasy wyjątku). Gdy użytkownik poda dowolną inną wartość
    # na przykład literę to zostanie wyświetlony błąd o nieprawidłowej wartości. Dodatkowo
    # użytkownik zostanie poinformowany o takim błędzie w okienku biletów/płatności.
    try:
        blad['text'] = ""
        if int(zmienna.get()) < 0:
            raise w.bladUjemnaWartosc("LOG: Podano ujemną wartość")
        return int(zmienna.get())
    except w.bladUjemnaWartosc as e:
        print(e)
        blad['text'] = "Podałeś ujemną wartość"
        return 0
    except:
        blad['text'] = "Podałeś błędną wartość"
        return 0


def otworzPlatnosci():
    """
    Funkcja odpowiada za otwarcie okienka z płatnościami,
    gdzie użytkownik może wybrać nominały oraz ilość, którymi chce zapłacić
    """

    def wplaconychDoDepo():
        """Funkcja informująca w okienku użytkownika o sumie wpłaconych pieniędzy"""
        wplacono['text'] = "Wpłaciłeś " + str(biletomat.sumaDepo()) + " zł"

    # Utworzenie okienka z płatnościami
    root2 = Tk()

    root2.title("Zaplac za bilet")
    root2.geometry("500x650")

    label = Label(root2, text="Proszę wybrać monety/banknoty do zapłacenia", font=30)
    label.grid(row=1, column=0)

    blad_platnosci = Label(root2, text="", font=30)
    blad_platnosci.grid(row=2, column=0)

    wplacono = Label(root2, text="Wpłaciłeś " + str(biletomat.sumaDepo()) + " zł", font=30)
    wplacono.grid(row=3, column=0)

    # Poniżej utworzone są przyciski/pola "input", które wywołują odpowiednie funkcje po naciśnięciu ich. Pozostałe są tworzone na podobne zasadzie.
    # Zmienne tworzyłem by bylo potem lepiej identyfikować dany przycisk dla przykładu gr1b oznacza gr - grosz, 1 - 1 zł, b - button.
    # zl20i to zl - złotówka, 20 - 20 zł, i - pole typu input. Na przykładzie jednego przycisku opiszę ich działanie. Zmienna gr1b zawiera przycisk,
    # która wywołuje funkcję dodajDoDepozytu z obiektu biletomat. Do funkcji podawane są odpowiednie parametry, dzięki którym można zidentyfikować,
    # które dane mają być przekazane oraz na jakich należy operować. W dwóch pierwszych parametrach podaję rodzaje nominału, a na końcu z pola input
    # odczytuję ilość tych monet. Funkcja wpłaconychDoDepo odpowiedzialna jest za wyświetlenie sumy wpłaconych pieniędzy. Zmienna wstawgr1b to zmienna
    # zawierająca gucik z napisem "+". Użytkownik, gdy chce wprowadzić dowolną ilość biletów to może wpisać je do pola input i potem dodać przyciskiem "+".
    # Zawiera funkcję dodajmonetePole, do której przekazuje kolejno pole "input" (ponieważ ciało ten funkcji jest odpowiedzialne za poprawne wyświetlanie wartości
    # w polu input po dodaniu pieniędzy) oraz funkcję sprawdź liczbę odpowiedzialną za walidację wprowadzanych danych. Dodatkowo przekazujemy etykietę blad_platnosci,
    # aby wyświetił do niej informację po tym jak użytkownik poda nieprawidłową wartość.

    # ----------------------------1 grosz----------------------------
    gr1b = Button(root2, width=25, height=2, text="1 grosz", command=lambda: [biletomat.dodajDoDepozytu('1', 1, gr1i), wplaconychDoDepo()])
    wstawgr1b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(gr1i, '1', sprawdzLiczbe(gr1i, blad_platnosci)), wplaconychDoDepo()])
    gr1i = Entry(root2, width=5)

    gr1b.grid(row=4, column=0)
    gr1i.grid(row=4, column=1)
    wstawgr1b.grid(row=4, column=2)

    # ----------------------------2 grosze----------------------------
    gr2b = Button(root2, width=25, height=2, text="2 grosze", command=lambda: [biletomat.dodajDoDepozytu('2', 1, gr2i), wplaconychDoDepo()])
    wstawgr2b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(gr2i, '2', sprawdzLiczbe(gr2i, blad_platnosci)), wplaconychDoDepo()])
    gr2i = Entry(root2, width=5)

    gr2b.grid(row=6, column=0)
    gr2i.grid(row=6, column=1)
    wstawgr2b.grid(row=6, column=2)

    # ----------------------------5 groszy----------------------------
    gr5b = Button(root2, width=25, height=2, text="5 groszy",command=lambda: [biletomat.dodajDoDepozytu('5', 1, gr5i), wplaconychDoDepo()])
    wstawgr5b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(gr5i, '5', sprawdzLiczbe(gr5i, blad_platnosci)), wplaconychDoDepo()])
    gr5i = Entry(root2, width=5)

    gr5b.grid(row=8, column=0)
    gr5i.grid(row=8, column=1)
    wstawgr5b.grid(row=8, column=2)

    # ----------------------------10 groszy----------------------------
    gr10b = Button(root2, width=25, height=2, text="10 groszy",command=lambda: [biletomat.dodajDoDepozytu('10', 1, gr10i), wplaconychDoDepo()])
    wstawgr10b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(gr10i, '10', sprawdzLiczbe(gr10i, blad_platnosci)), wplaconychDoDepo()])
    gr10i = Entry(root2, width=5)

    gr10b.grid(row=10, column=0)
    gr10i.grid(row=10, column=1)
    wstawgr10b.grid(row=10, column=2)

    # ----------------------------20 groszy----------------------------
    gr20b = Button(root2, width=25, height=2, text="20 groszy", command=lambda: [biletomat.dodajDoDepozytu('20', 1, gr20i), wplaconychDoDepo()])
    wstawgr20b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(gr20i, '20', sprawdzLiczbe(gr20i, blad_platnosci)), wplaconychDoDepo()])
    gr20i = Entry(root2, width=5)

    gr20b.grid(row=12, column=0)
    gr20i.grid(row=12, column=1)
    wstawgr20b.grid(row=12, column=2)

    # ----------------------------50 groszy----------------------------
    gr50b = Button(root2, width=25, height=2, text="50 groszy", command=lambda: [biletomat.dodajDoDepozytu('50', 1, gr50i), wplaconychDoDepo()])
    wstawgr50b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(gr50i, '50', sprawdzLiczbe(gr50i, blad_platnosci)), wplaconychDoDepo()])
    gr50i = Entry(root2, width=5)

    gr50b.grid(row=14, column=0)
    gr50i.grid(row=14, column=1)
    wstawgr50b.grid(row=14, column=2)

    # ----------------------------1 złoty----------------------------
    zl1b = Button(root2, width=25, height=2, text="1 złoty", command=lambda: [biletomat.dodajDoDepozytu('100', 1, zl1i), wplaconychDoDepo()])
    wstawzl1b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(zl1i, '100', sprawdzLiczbe(zl1i, blad_platnosci)), wplaconychDoDepo()])
    zl1i = Entry(root2, width=5)

    zl1b.grid(row=16, column=0)
    zl1i.grid(row=16, column=1)
    wstawzl1b.grid(row=16, column=2)

    # ----------------------------2 złote----------------------------
    zl2b = Button(root2, width=25, height=2, text="2 złote", command=lambda: [biletomat.dodajDoDepozytu('200', 1, zl2i), wplaconychDoDepo()])
    wstawzl2b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(zl2i, '200', sprawdzLiczbe(zl2i, blad_platnosci)), wplaconychDoDepo()])
    zl2i = Entry(root2, width=5)

    zl2b.grid(row=18, column=0)
    zl2i.grid(row=18, column=1)
    wstawzl2b.grid(row=18, column=2)

    # ----------------------------5 złotych----------------------------
    zl5b = Button(root2, width=25, height=2, text="5 złotych", command=lambda: [biletomat.dodajDoDepozytu('500', 1, zl5i), wplaconychDoDepo()])
    wstawzl5b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(zl5i, '500', sprawdzLiczbe(zl5i, blad_platnosci)), wplaconychDoDepo()])
    zl5i = Entry(root2, width=5)

    zl5b.grid(row=20, column=0)
    zl5i.grid(row=20, column=1)
    wstawzl5b.grid(row=20, column=2)

    # ----------------------------10 złotych----------------------------
    zl10b = Button(root2, width=25, height=2, text="10 złotych", command=lambda: [biletomat.dodajDoDepozytu('1000', 1, zl10i), wplaconychDoDepo()])
    wstawzl10b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(zl10i, '1000', sprawdzLiczbe(zl10i, blad_platnosci)), wplaconychDoDepo()])
    zl10i = Entry(root2, width=5)

    zl10b.grid(row=22, column=0)
    zl10i.grid(row=22, column=1)
    wstawzl10b.grid(row=22, column=2)

    # ----------------------------20 złotych----------------------------
    zl20b = Button(root2, width=25, height=2, text="20 złotych", command=lambda: [biletomat.dodajDoDepozytu('2000', 1, zl20i), wplaconychDoDepo()])
    wstawzl20b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(zl20i, '2000', sprawdzLiczbe(zl20i, blad_platnosci)), wplaconychDoDepo()])
    zl20i = Entry(root2, width=5)

    zl20b.grid(row=24, column=0)
    zl20i.grid(row=24, column=1)
    wstawzl20b.grid(row=24, column=2)

    # ----------------------------50 złotych----------------------------
    zl50b = Button(root2, width=25, height=2, text="50 złotych", command=lambda: [biletomat.dodajDoDepozytu('5000', 1, zl50i), wplaconychDoDepo()])
    wstawzl50b = Button(root2, text=tekstGuzikaDodaj, command=lambda: [biletomat.dodajMonetePole(zl50i, '5000', sprawdzLiczbe(zl50i, blad_platnosci)), wplaconychDoDepo()])
    zl50i = Entry(root2, width=5)

    zl50b.grid(row=26, column=0)
    zl50i.grid(row=26, column=1)
    wstawzl50b.grid(row=26, column=2)

    zaplac = Button(root2, text="Zapłać", command=lambda: [biletomat.zaplac(zwrocCene(bilet)), informacjaZakupowa(root, root2)])
    zaplac.grid(row=28, column=0)

    root2.mainloop()


#----------------------------GŁÓWNA CZĘŚĆ PROGRAMU----------------------------

# Utworzenie obiektu biletomat
biletomat = biletomat.Biletomat()
print(biletomat.suma())

# Tworzenie obiektów klasy Bilet
generujLiczbeBiletow = generujLiczby(6)
bilet = [None for _ in range(6)]

bilet[next(generujLiczbeBiletow)] = Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("40 minutowy", "ulgowy", Decimal('2.50'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("60 minutowy", "ulgowy", Decimal('3'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("20 minutowy", "normalny", Decimal('2.25'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("40 minutowy", "normalny", Decimal('4.40'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("60 minutowy", "normalny", Decimal('6'), 0)

# Okienko odpowiedzialne za biletomat
root = Tk()

root.title("Automat biletowy MPK")
root.geometry("400x400")

label = Label(root, font=30)
powitaj(label)
label.grid(row=1, column=0)

blad_biletow = Label(root, text="", font=30)
blad_biletow.grid(row=2, column=0)

label2 = Label(root, text="Do zapłacenia: " + str(zwrocCene(bilet)) + " zł", font=30, anchor='s')
label2.grid(row=3, column=0)

# Zmienne dla przycisków w biletomacie zostały utworzone w podobnej zasadzie. Przycisk ulg20b odpowiedzialny jest za dodanie biletu
# ulgowego 20-minutowego. Przycisk ten wywołuje funkcje dodajbilet, który przekazuje ilość biletów pobranych z inputa do danego obiektu,
# oraz kosztZakupow, która aktualizuje etykietę z sumą pieniędzy do zapłacenia.
# Zmienna wstawulg20b to zmienna zawierająca guzik z napisem "+". Użytkownik, gdy chce wprowadzić dowolną ilość pieniędzy to może wpisać je do pola input i potem dodać przyciskiem "+".
# Posiada ona funkcję dodajBiletPole, do której przekazywane są 2 parametry: pole "input" (ponieważ ciało ten funkcji jest odpowiedzialne za
# poprawne wyświetlanie wartości w polu input po dodaniu biletów) oraz funkcję sprawdź liczbę odpowiedzialną za walidację wprowadzanych danych.
# Dodatkowo przekazujemy etykietę blad_biletow, aby wyświetił do niej informację po tym jak użytkownik poda nieprawidłową wartość.

# ----------------------------20-minutowy ulgowy----------------------------
ulg20b = Button(root, width=25, height=2, text="20-minutowy ulgowy [1,50 zł]", command=lambda: [bilet[0].dodajBilet(ulg20i), kosztZakupow(label2)])
wstawulg20b = Button(root, text=tekstGuzikaDodaj, command=lambda: [bilet[0].dodajBiletPole(ulg20i, sprawdzLiczbe(ulg20i, blad_biletow)), kosztZakupow(label2)])
ulg20i = Entry(root, width=10)
ulg20b.grid(row=4, column=0)
ulg20i.grid(row=4, column=1)
wstawulg20b.grid(row=4, column=2)

# ----------------------------40-minutowy ulogwy----------------------------
ulg40b = Button(root, width=25, height=2, text="40-minutowy ulgowy [2,50 zł]", command=lambda: [bilet[1].dodajBilet(ulg40i), kosztZakupow(label2)])
wstawulg40b = Button(root, text=tekstGuzikaDodaj, command=lambda: [bilet[1].dodajBiletPole(ulg40i, sprawdzLiczbe(ulg40i, blad_biletow)), kosztZakupow(label2)])
ulg40i = Entry(root, width=10)

ulg40b.grid(row=6, column=0)
ulg40i.grid(row=6, column=1)
wstawulg40b.grid(row=6, column=2)

# ----------------------------60-minutowy ulgowy----------------------------
ulg60b = Button(root, width=25, height=2, text="60-minutowy ulgowy [3 zł]", command=lambda: [bilet[2].dodajBilet(ulg60i), kosztZakupow(label2)])
wstawulg60b = Button(root, text=tekstGuzikaDodaj, command=lambda: [bilet[2].dodajBiletPole(ulg60i, sprawdzLiczbe(ulg60i, blad_biletow)), kosztZakupow(label2)])
ulg60i = Entry(root, width=10)

ulg60b.grid(row=8, column=0)
ulg60i.grid(row=8, column=1)
wstawulg60b.grid(row=8, column=2)

# ----------------------------20-minutowy normalny----------------------------
norm20b = Button(root, width=25, height=2, text="20-minutowy normalny [2,25 zł]", command=lambda: [bilet[3].dodajBilet(norm20i), kosztZakupow(label2)])
wstawnorm20b = Button(root, text=tekstGuzikaDodaj, command=lambda: [bilet[3].dodajBiletPole(norm20i, sprawdzLiczbe(norm20i, blad_biletow)), kosztZakupow(label2)])
norm20i = Entry(root, width=10)

norm20b.grid(row=10, column=0)
norm20i.grid(row=10, column=1)
wstawnorm20b.grid(row=10, column=2)

# ----------------------------40-minutowy normalny----------------------------
norm40b = Button(root, width=25, height=2, text="40-minutowy normalny [4,40 zł]", command=lambda: [bilet[4].dodajBilet(norm40i), kosztZakupow(label2)])
wstawnorm40b = Button(root, text=tekstGuzikaDodaj, command=lambda: [bilet[4].dodajBiletPole(norm40i, sprawdzLiczbe(norm40i, blad_biletow)), kosztZakupow(label2)])
norm40i = Entry(root, width=10)

norm40b.grid(row=12, column=0)
norm40i.grid(row=12, column=1)
wstawnorm40b.grid(row=12, column=2)

# ----------------------------60-mininutowy normalny----------------------------
norm60b = Button( root, width=25, height=2, text="60-minutowy normalny [6 zł]", command=lambda: [bilet[5].dodajBilet(norm60i), kosztZakupow(label2)])
wstawnorm60b = Button(root, text=tekstGuzikaDodaj, command=lambda: [bilet[5].dodajBiletPole(norm60i, sprawdzLiczbe(norm60i, blad_biletow)), kosztZakupow(label2)])
norm60i = Entry(root, width=10)

norm60b.grid(row=14, column=0)
norm60i.grid(row=14, column=1)
wstawnorm60b.grid(row=14, column=2)

# Po kliknięciu przycisku podsumuj zostanie wyświetlone okno z płatnościami
podsumowanie = Button(root, text="Podsumuj", command=lambda: [otworzPlatnosci()])
podsumowanie.grid(row=16, column=0)

root.mainloop()
