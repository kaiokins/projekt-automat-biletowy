import math
from datetime import datetime
from decimal import *
from functools import wraps
from tkinter import *

import biletomat
from oprogramowanie.bilet import Bilety
from wyjatki import wyjatki as w

# Utworzenie obiektu biletomat
biletomat = biletomat.Biletomat()
print(biletomat.suma())

tekstGuzikaDodaj = "+"
(lambda tekstGuzikaDodaj: print(tekstGuzikaDodaj))


def generujLiczby(x):
    i = 0
    while i < x:
        yield i
        i += 1


generujLiczbeBiletow = generujLiczby(6)

# Tworzenie obiektów klasy Bilet
bilet = [None for _ in range(6)]
bilet[next(generujLiczbeBiletow)] = Bilety("20 minutowy", "ulgowy", Decimal('1.50'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("40 minutowy", "ulgowy", Decimal('2.50'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("60 minutowy", "ulgowy", Decimal('3'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("20 minutowy", "normalny", Decimal('2.25'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("40 minutowy", "normalny", Decimal('4.40'), 0)
bilet[next(generujLiczbeBiletow)] = Bilety("60 minutowy", "normalny", Decimal('6'), 0)


def ktoraGodzina(func):
    now = datetime.now()

    @wraps(func)
    def wrapper(tekst):
        tekst['text'] = "Jest godzina " + now.strftime("%H:%M") + "\n" + func(tekst)

    return wrapper


@ktoraGodzina
def powitaj(tekst):
    """Funkcja wyświetla prośbę o wybór biletu oraz aktualną godzinę (funkcja opakowna)"""
    return "Proszę wybrać rodzaj biletu"


def zwrocCene():
    """Funkcja zwraca cenę biletów wybranych przez użytkownika (sumuje)"""
    suma = 0
    for i in range(len(bilet)):
        suma = suma + bilet[i].zwrocCene() * bilet[i].zwrocIlosc()
    return suma


def kosztZakupow(etykieta):
    """Funkcja pokazuje ile użytkownik musi zapłacić"""
    etykieta['text'] = "Do zapłacenia: " + str(zwrocCene()) + " zł"


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
    czyKupil = Label(
        oknoZakupowe, text="", font=30)
    jakieBiletyZakupil = Label(oknoZakupowe, font=15)
    czyKupil.pack()
    jakieBiletyZakupil.pack()

    if biletomat.pobierzInformacje() == 1:
        # Wyświetla podsumowanie zakupów. Ile biletów danego rodzaju użytkownik zakupił oraz ile zwrócono mu reszty
        czyKupil['text'] = "Dziękujemy za zakup biletów. Zakupiłeś:"
        info = ''
        for i in range(6):
            if bilet[i].zwrocIlosc() > 0:
                info += "Bilet " + bilet[i].zwrocNazwe() + " " + \
                        bilet[i].zwrocRodzaj() + " w ilości sztuk: " + \
                        str(bilet[i].zwrocIlosc()) + "\n"

        biletomat.zwrocReszte()
        jakieBiletyZakupil['text'] = info + "\n Wydano " + \
                                     str(biletomat.sumaDepo() - zwrocCene()) + " zł reszty"
        jakieBiletyZakupil.pack()

        zamknijOkno()
    elif biletomat.pobierzInformacje() == 2:
        # W przypadku gdy automat nie może wydać reszty informuje użytkownika
        # oraz zostają mu zwrócone pieniądze
        jakieBiletyZakupil['text'] = "Tylko odliczona kwota. Zwracam " + \
                                     str(biletomat.sumaDepo()) + " zł reszty"
        jakieBiletyZakupil.pack()
        biletomat.oddajMonety()
        # biletomat.wyczyscDepozyt()
        # print("ODDAJE: ", biletomat.oddajMonety())
        zamknijOkno()
    elif biletomat.pobierzInformacje() == 3:
        # Gdy klient wrzuci za mało banknotów to zostanie o tym poinformowany.
        # Wyświetli się informacje ile jeszcze należy wrzucić.
        jakieBiletyZakupil['text'] = "Wrzuciłeś za mało banknotów. Brakuje " + \
                                     str(math.fabs(biletomat.sumaDepo() - zwrocCene())) + " zł"
    else:
        jakieBiletyZakupil['text'] = "Upsss... coś poszło źle"
        jakieBiletyZakupil.pack()
        zamknijOkno()

    oknoZakupowe.mainloop()


# def doZaplaty(i):
# if bilet[i].zwrocIlosc() == 0:
# pass
# elif bilet[i].zwrocIlosc() < 0:
# bilet[i].dodajBilet(i)
# else:
# print(round(bilet[i].zwrocIlosc()*bilet[i].zwrocCene(), 5))


# def doZaplatyPole(i, ilosc):
# if bilet[i].zwrocIlosc() == 0:
# pass
# elif bilet[i].zwrocIlosc() < 0:
# bilet[i].dodajBilet(i)
# else:
# print(round(int(ulg20i.get())*bilet[i].zwrocCene(), 5))

# window_status = 0

# Funkcje po stronie wpłacania


#  def doZaplatyDepo(i, ilosc):
# if bilet[i].zwrocIlosc() == 0:
# pass
# elif bilet[i].zwrocIlosc() < 0:
#  bilet[i].dodajbilet(i)
# else:
#  print(round(int(ulg20i.get())*bilet[i].zwrocCene(), 5))


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
        blad['text'] = "Podałeś nieprawidłową wartość"
        return 0


def otworzPlatnosci():
    """
    Funkcja odpowiada za otwarcie okienka z płatnościami,
    gdzie użytkownik może wybrać nominały oraz ilośc,którymi chce zapłacić.
    """

    def wplaconychDoDepo():
        """Funkcja informująca w okienku użytkownika o sumie wpłaconych pieniędzy"""
        wplacono['text'] = "Wpłaciłeś " + str(biletomat.sumaDepo()) + " zł"

    # Utworzenie okienka z płatnościami
    root2 = Tk()
    # global window_status
    # if window_status == 0:
    root2.title("Zaplac za bilet")
    root2.geometry("600x1000")
    label = Label(root2, text="Proszę wybrać monety/banknoty do zapłacenia", font=30)
    label.pack()

    blad_platnosci = Label(root2, text="", font=30)
    blad_platnosci.pack()

    wplacono = Label(root2, text="Wpłaciłeś " + str(biletomat.sumaDepo()) + " zł", font=30)
    wplacono.pack()

    # Poniżej utworzone są przyciski/pola "input", które wywołują odpowiednie funkcje po naciśnięciu ich. Pozostałe są tworzone na podobne zasadzie.
    # Zmienne tworzyłem by bylo potem lepiej identyfikować dany przycisk dla przykładu gr1b oznacza gr - grosz, 1 - 1 zł, b - button.
    # zl20i to zl - złotówka, 20 - 20 zł, i - pole typu input. Na przykładzie jednego przycisku opiszę ich działanie. Zmienna gr1b zawiera przycisk,
    # która wywołuje funkcję dodajDoDepozytu z obiektu biletomat. Do funkcji podawane są odpowiednie parametry, dzięki którym można zidentyfikować,
    # które dane mają być przekazane oraz na jakich należy operować. W dwóch pierwszych parametrach podaję rodzaje nominału, a na końcu z pola input
    # odczytuję ilość tych monet. Funkcja wpłaconychDoDepo odpowiedzialna jest za wyświetlenie sumy wpłaconych pieniędzy. Zmienna wstawgr1b to zmienna
    # zawierająca gucik z napisem "+". Użytkownik, gdy chce wprowadzić dowolną ilość biletów to może wpisać je do pola input i potem dodać przyciskiem "+".
    # Zawiera funkcję dodajmonetePole, do której przekazuje kolejno pole "input" (ponieważ ciało ten funkcji jest odpowiedzialne za poprawne wyświetlanie wartości
    # w polu input po dodaniu biletów) oraz funkcję sprawdź liczbę odpowiedzialną za walidację wprowadzanych danych. Dodatkowo przekazujemy etykietę blad_platnosci,
    # aby wyświetił informację do niej po tym jak użytkownik poda nieprawidłową wartość.
    gr1b = Button(root2, text="1 grosz",
                  command=lambda: [biletomat.dodajDoDepozytu('1', 1, gr1i), wplaconychDoDepo()])
    wstawgr1b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(gr1i, '1', sprawdzLiczbe(gr1i, blad_platnosci)), wplaconychDoDepo()])
    gr1i = Entry(root2, width=5)
    gr1b.pack()
    gr1i.pack()
    wstawgr1b.pack()

    gr2b = Button(root2, text="2 grosze", command=lambda: [
        biletomat.dodajDoDepozytu('2', 1, gr2i), wplaconychDoDepo()])
    wstawgr2b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(gr2i, '2', sprawdzLiczbe(gr2i, blad_platnosci)), wplaconychDoDepo()])
    gr2i = Entry(root2, width=5)
    gr2b.pack()
    gr2i.pack()
    wstawgr2b.pack()

    gr5b = Button(root2, text="5 groszy",
                  command=lambda: [biletomat.dodajDoDepozytu('5', 1, gr5i), wplaconychDoDepo()])
    wstawgr5b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(gr5i, '5', sprawdzLiczbe(gr5i, blad_platnosci)), wplaconychDoDepo()])
    gr5i = Entry(root2, width=5)
    gr5b.pack()
    gr5i.pack()
    wstawgr5b.pack()

    gr10b = Button(root2, text="10 groszy",
                   command=lambda: [biletomat.dodajDoDepozytu('10', 1, gr10i), wplaconychDoDepo()])
    wstawgr10b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(gr10i, '10', sprawdzLiczbe(gr10i, blad_platnosci)),
                         wplaconychDoDepo()])
    gr10i = Entry(root2, width=5)
    gr10b.pack()
    gr10i.pack()
    wstawgr10b.pack()

    gr20b = Button(root2, text="20 groszy",
                   command=lambda: [biletomat.dodajDoDepozytu('20', 1, gr20i), wplaconychDoDepo()])
    wstawgr20b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(gr20i, '20', sprawdzLiczbe(gr20i, blad_platnosci)),
                         wplaconychDoDepo()])
    gr20i = Entry(root2, width=5)
    gr20b.pack()
    gr20i.pack()
    wstawgr20b.pack()

    gr50b = Button(root2, text="50 groszy",
                   command=lambda: [biletomat.dodajDoDepozytu('50', 1, gr50i), wplaconychDoDepo()])
    wstawgr50b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(gr50i, '50', sprawdzLiczbe(gr50i, blad_platnosci)),
                         wplaconychDoDepo()])
    gr50i = Entry(root2, width=5)
    gr50b.pack()
    gr50i.pack()
    wstawgr50b.pack()

    zl1b = Button(root2, text="1 złoty",
                  command=lambda: [biletomat.dodajDoDepozytu('100', 1, zl1i), wplaconychDoDepo()])
    wstawzl1b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(zl1i, '100', sprawdzLiczbe(zl1i, blad_platnosci)),
                         wplaconychDoDepo()])
    zl1i = Entry(root2, width=5)
    zl1b.pack()
    zl1i.pack()
    wstawzl1b.pack()

    zl2b = Button(root2, text="2 złote",
                  command=lambda: [biletomat.dodajDoDepozytu('200', 1, zl2i), wplaconychDoDepo()])
    wstawzl2b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(zl2i, '200', sprawdzLiczbe(zl2i, blad_platnosci)),
                         wplaconychDoDepo()])
    zl2i = Entry(root2, width=5)
    zl2b.pack()
    zl2i.pack()
    wstawzl2b.pack()

    zl5b = Button(root2, text="5 złotych",
                  command=lambda: [biletomat.dodajDoDepozytu('500', 1, zl5i), wplaconychDoDepo()])
    wstawzl5b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(zl5i, '500', sprawdzLiczbe(zl5i, blad_platnosci)),
                         wplaconychDoDepo()])
    zl5i = Entry(root2, width=5)
    zl5b.pack()
    zl5i.pack()
    wstawzl5b.pack()

    zl10b = Button(root2, text="10 złotych",
                   command=lambda: [biletomat.dodajDoDepozytu('1000', 1, zl10i), wplaconychDoDepo()])
    wstawzl10b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(zl10i, '1000', sprawdzLiczbe(zl10i, blad_platnosci)),
                         wplaconychDoDepo()])
    zl10i = Entry(root2, width=5)
    zl10b.pack()
    zl10i.pack()
    wstawzl10b.pack()

    zl20b = Button(root2, text="20 złotych",
                   command=lambda: [biletomat.dodajDoDepozytu('2000', 1, zl20i), wplaconychDoDepo()])
    wstawzl20b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(zl20i, '2000', sprawdzLiczbe(zl20i, blad_platnosci)),
                         wplaconychDoDepo()])
    zl20i = Entry(root2, width=5)
    zl20b.pack()
    zl20i.pack()
    wstawzl20b.pack()

    zl50b = Button(root2, text="50 złotych",
                   command=lambda: [biletomat.dodajDoDepozytu('5000', 1, zl50i), wplaconychDoDepo()])
    wstawzl50b = Button(
        root2, text=tekstGuzikaDodaj,
        command=lambda: [biletomat.dodajMonetePole(zl50i, '5000', sprawdzLiczbe(zl50i, blad_platnosci)),
                         wplaconychDoDepo()])
    zl50i = Entry(root2, width=5)
    zl50b.pack()
    zl50i.pack()
    wstawzl50b.pack()

    zaplac = Button(root2, text="Zapłać",
                    command=lambda: [biletomat.zaplac(zwrocCene()), informacjaZakupowa(root, root2)])

    zaplac.pack()

    # window_status = 1
    # print("STATUS:", window_status)
    root2.mainloop()
    # else:
    # window_status = 0
    # root2.destroy()
    # print("STATUS:", window_status)
    # otworzPlatnosci()


# Okienko odpowiedzialne za biletomat
root = Tk()
root.title("Automat biletowy MPK")
root.geometry("600x650")
label = Label(root, font=30)
powitaj(label)
label.pack()
blad_biletow = Label(root, text="", font=30)
blad_biletow.pack()

label2 = Label(root, text="Do zapłacenia: " + str(zwrocCene()) + " zł", font=30, anchor='s')
label2.pack()

# Zmienne dla przycisków w biletomacie zostały utworzone w podobnej zasadzie. Przycisk ulg20b odpowiedzialny jest za dodanie biletu
# ulgowego 20-minutowego. Przycisk ten wywołuje funkcje dodajbilet, który przekazuje ilość biletów pobranych z inputa do danego obiektu,
# funkcję doZapłaty, która pokazuje sumę pieniędzy ...................... oraz kosztZakupow, która aktualizuje etykietę z sumą pieniędzy do zapłacenia.
# Zmienna wstawulg20b to zmienna zawierająca gucik z napisem "+". Użytkownik, gdy chce wprowadzić dowolną ilość pieniędzy to może wpisać je do pola input i potem dodać przyciskiem "+".
# Posiada ona funkcję dodajBiletPole, która przekazuje ilość biletów pobranych z inputa biletów do danego obiekt funkcję, która sprawdza czy została podana poprawna wartość,
# funkcję doZaplatyPole, które przyjmuje wartość wyciągniętą z inputa.
ulg20b = Button(
    root, text="20-minutowy ulgowy [1,50 zł]", command=lambda: [bilet[0].dodajBilet(ulg20i), kosztZakupow(label2)])
wstawulg20b = Button(
    root, text=tekstGuzikaDodaj,
    command=lambda: [bilet[0].dodajBiletPole(ulg20i, sprawdzLiczbe(ulg20i, blad_biletow)), kosztZakupow(label2)])
ulg20i = Entry(root, width=5)
ulg20b.pack()
ulg20i.pack()
wstawulg20b.pack()

ulg40b = Button(
    root, text="40-minutowy ulgowy [2,50 zł]", command=lambda: [bilet[1].dodajBilet(ulg40i), kosztZakupow(label2)])
wstawulg40b = Button(
    root, text=tekstGuzikaDodaj,
    command=lambda: [bilet[1].dodajBiletPole(ulg40i, sprawdzLiczbe(ulg40i, blad_biletow)), kosztZakupow(label2)])
ulg40i = Entry(root, width=5)
ulg40b.pack()
ulg40i.pack()
wstawulg40b.pack()

ulg60b = Button(
    root, text="60-minutowy ulgowy [3 zł]", command=lambda: [bilet[2].dodajBilet(ulg60i), kosztZakupow(label2)])
wstawulg60b = Button(
    root, text=tekstGuzikaDodaj,
    command=lambda: [bilet[2].dodajBiletPole(ulg60i, sprawdzLiczbe(ulg60i, blad_biletow)), kosztZakupow(label2)])
ulg60i = Entry(root, width=5)
ulg60b.pack()
ulg60i.pack()
wstawulg60b.pack()

norm20b = Button(
    root, text="20-minutowy normalny [2,25 zł]", command=lambda: [bilet[3].dodajBilet(norm20i), kosztZakupow(label2)])
wstawnorm20b = Button(
    root, text=tekstGuzikaDodaj,
    command=lambda: [bilet[3].dodajBiletPole(norm20i, sprawdzLiczbe(norm20i, blad_biletow)), kosztZakupow(label2)])
norm20i = Entry(root, width=5)
norm20b.pack()
norm20i.pack()
wstawnorm20b.pack()

norm40b = Button(
    root, text="40-minutowy normalny [4,40 zł]", command=lambda: [bilet[4].dodajBilet(norm40i), kosztZakupow(label2)])
wstawnorm40b = Button(
    root, text=tekstGuzikaDodaj,
    command=lambda: [bilet[4].dodajBiletPole(norm40i, sprawdzLiczbe(norm40i, blad_biletow)), kosztZakupow(label2)])
norm40i = Entry(root, width=5)
norm40b.pack()
norm40i.pack()
wstawnorm40b.pack()

norm60b = Button(
    root, text="60-minutowy normalny [6 zł]", command=lambda: [bilet[5].dodajBilet(norm60i), kosztZakupow(label2)])
wstawnorm60b = Button(
    root, text=tekstGuzikaDodaj,
    command=lambda: [bilet[5].dodajBiletPole(norm60i, sprawdzLiczbe(norm60i, blad_biletow)), kosztZakupow(label2)])
norm60i = Entry(root, width=5)
norm60b.pack()
norm60i.pack()
wstawnorm60b.pack()

# Po kliknięciu przycisku podsumuj zostanie wyświetlone okno z płatnościami
podsumowanie = Button(root, text="Podsumuj",
                      command=lambda: [otworzPlatnosci()])
podsumowanie.pack()

root.mainloop()
